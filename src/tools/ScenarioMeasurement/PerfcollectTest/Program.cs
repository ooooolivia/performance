using System;
using Startup;
using ScenarioMeasurement;
using System.Diagnostics;

namespace PerfcollectTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Perfcollect perfcollect = new Perfcollect("wrapper-kernel-3", "trace", new Logger("name.log"));
            perfcollect.Events = Perfcollect.EventOptions.ProcessLifetime;
            var startResult = perfcollect.Start();
            RunTest();
            var stopResult = perfcollect.Stop();
        }

        static void RunTest()
        {
            var startInfo = new ProcessStartInfo();
            startInfo.FileName = "python3";
            startInfo.Arguments = "--version";
            var testProcess = new Process();
            testProcess.StartInfo = startInfo;
            testProcess.Start();
            Console.WriteLine("test process started.");
            testProcess.WaitForExit();
            Console.WriteLine("test process end.");
        }
    }
}