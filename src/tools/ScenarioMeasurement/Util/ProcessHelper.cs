using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Threading;

namespace ScenarioMeasurement
{
    public class ProcessHelper
    {
        /// <summary>
        /// Specifies whether the app exits on its own
        /// true: App will exit, Timeout specifies how long to wait before terminating the process.
        /// false: App will be closed after MeasurementDelay.
        /// </summary>
        public bool ProcessWillExit { get; set; } = false;
        /// <summary>
        /// Max time to wait for app to close (seconds)
        /// </summary>
        public int Timeout { get; set; } = 60;
        /// <summary>
        /// Time to wait before closing app (seconds)
        /// </summary>
        public int MeasurementDelay { get; set; } = 15;

        public string Executable { get; set; }

        public string Arguments { get; set; } = String.Empty;
        public string WorkingDirectory { get; set; } = String.Empty;

        public bool GuiApp { get; set; } = false;

        public Logger logger;

        public ProcessHelper(Logger logger)
        {
            this.logger = logger;
        }

        /// <summary>
        /// Runs the specified process and waits for it to exit.
        /// </summary>
        /// <param name="appExe">Full path to executable</param>
        /// <param name="appArgs">Optional arguments</param>
        /// <param name="workingDirectory">Optional working directory (defaults to current directory)</param>
        /// <returns></returns>
        public (Result result, int pid) Run()
        {
            var psi = new ProcessStartInfo();

            psi.EnvironmentVariables["DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR"] = "E:\\sdk-perf\\artifacts\\bin\\Release\\Sdks";
            psi.EnvironmentVariables["DOTNET_MULTILEVEL_LOOKUP"] = "0";
            psi.EnvironmentVariables["DOTNET_SKIP_FIRST_TIME_EXPERIENCE"] = "1";
            psi.EnvironmentVariables["MSBuildSDKsPath"] = "E:\\sdk-perf\\artifacts\\bin\\Release\\Sdks";
            psi.EnvironmentVariables["MSBUILDTARGETOUTPUTLOGGING"] = "true";
            psi.EnvironmentVariables["DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR"] = "E:\\sdk-perf\\artifacts\\bin\\Release\\Sdks";
            psi.EnvironmentVariables["GenerateResourceMSBuildArchitecture"] = "CurrentArchitecture";
            psi.EnvironmentVariables["GenerateResourceMSBuildRuntime"] = "CurrentRuntime";
            psi.EnvironmentVariables["MicrosoftNETBuildExtensionsTargets"] = "E:\\sdk-perf\\artifacts\\bin\\Release\\Sdks\\Microsoft.NET.Build.Extensions\\msbuildExtensions\\Microsoft\\Microsoft.NET.Build.Extensions\\Microsoft.NET.Build.Extensions.targets";
            psi.EnvironmentVariables["MSBuildExtensionsPath"] = "E:\\sdk-perf\\.dotnet\\sdk\\3.0.100";
            psi.EnvironmentVariables["MSBuildLoadMicrosoftTargetsReadOnly"] = "true";
            psi.EnvironmentVariables["MSBUILDLOGIMPORTS"] = "1";
            psi.EnvironmentVariables["MSBUILDNODEHANDSHAKESALT "] = "Test Environment for dotnet/sdk";
            psi.EnvironmentVariables["NUGET_PACKAGES"] = "= E:\\sdk-perf\\artifacts\\.nuget\\packages";
            psi.EnvironmentVariables["NUGET_PLUGIN_HANDSHAKE_TIMEOUT_IN_SECONDS"] = "20";
            psi.EnvironmentVariables["NUGET_PLUGIN_REQUEST_TIMEOUT_IN_SECONDS"] = "20";


            psi.FileName = Executable;
            psi.Arguments = Arguments;
            psi.WorkingDirectory = WorkingDirectory;
            psi.UseShellExecute = GuiApp;

            if (!GuiApp)
            {
                psi.RedirectStandardOutput = true;
                psi.RedirectStandardError = true;
            }
            else
            {
                psi.WindowStyle = ProcessWindowStyle.Maximized;
            }
            StringBuilder output = new StringBuilder();
            StringBuilder error = new StringBuilder();
            using (var process = new Process())
            {
                process.StartInfo = psi;
                if (!GuiApp)
                {
                    process.OutputDataReceived += (s, e) =>
                    {
                        output.AppendLine(e.Data);
                    };
                    process.ErrorDataReceived += (s, e) =>
                    {
                        error.AppendLine(e.Data);
                    };
                }
                process.Start();
                int pid = process.Id;
                if (!GuiApp)
                {
                    process.BeginOutputReadLine();
                    process.BeginErrorReadLine();
                }

                if (ProcessWillExit)
                {
                    bool exited = process.WaitForExit(Timeout * 1000);
                    if (!exited)
                    {
                        process.Kill();
                        return (Result.TimeoutExceeded, pid);
                    }
                }
                else
                {
                    Thread.Sleep(MeasurementDelay * 1000);
                    if (!process.HasExited) { process.CloseMainWindow(); }
                    else
                    {
                        return (Result.ExitedEarly, pid);
                    }
                    bool exited = process.WaitForExit(5000);
                    if (!exited)
                    {
                        process.Kill();
                        return (Result.CloseFailed, pid);
                    }
                }

                logger.Log(output.ToString());
                logger.Log(error.ToString());

                // Be aware a successful exit could be non-zero
                if (process.ExitCode != 0)
                {
                    return (Result.ExitedWithError, pid);
                }
                return (Result.Success, pid);
            }
        }
        public enum Result
        {
            Success,
            TimeoutExceeded,
            ExitedEarly,
            CloseFailed,
            ExitedWithError
        }
    }
}
