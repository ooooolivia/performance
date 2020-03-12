using ScenarioMeasurement;
using System;
using System.Collections.Generic;
using System.CommandLine;
using System.IO;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.Serialization;
using System.Text;


namespace Startup
{
    public class Perfcollect
    {   
        private readonly string filepath = Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).FullName, @"Startup/perfcollect");
        private ProcessHelper perfcollectProcess;
        public string TraceName { get; private set; }
        public EventOptions Events { get; set; } = EventOptions.Empty;

        public Perfcollect(string traceName, Logger logger)
        {
            if (!File.Exists(filepath))
            {
                throw new FileNotFoundException($"Pefcollect not found at {filepath}. Please rebuild the project to download it.");
            }

            if (String.IsNullOrEmpty(traceName))
            {
                throw new ArgumentException(traceName);
            }

            perfcollectProcess = new ProcessHelper(logger)
            {
                ProcessWillExit = true,
                Executable = filepath,
                Timeout = 300
            };
        }

        public ProcessHelper.Result Start()
        {
            string arguments = $"start {TraceName} ";
            switch (Events)
            {
                case EventOptions.ProcessLifetime:
                    arguments += "-events processlifetime ";
                    break;
                case EventOptions.Threading:
                    arguments += "-events threading ";
                    break;
                case EventOptions.GcCollectOnly:
                    arguments += "-gccollectonly ";
                    break;
                case EventOptions.GcOnly:
                    arguments += "-gconly ";
                    break;
                case EventOptions.GcWithHeap:
                    arguments += "-gcwithheap ";
                    break;
                case EventOptions.Empty: 
                    break;

            }

            perfcollectProcess.Arguments = arguments;
            return perfcollectProcess.Run().Result;
        }

        public ProcessHelper.Result Stop()
        {
            string arguments = $"stop {TraceName} ";
            perfcollectProcess.Arguments = arguments;
            return perfcollectProcess.Run().Result;
        }

        public ProcessHelper.Result Install()
        {
            perfcollectProcess.Arguments = "install";
            return perfcollectProcess.Run().Result;
        }

        public enum EventOptions{ 
            Empty,
            ProcessLifetime,
            Threading,
            GcCollectOnly,
            GcOnly,
            GcWithHeap
        }

    }
}
