using ScenarioMeasurement;
using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization;
using System.Text;

namespace Startup
{
    public class Perfcollect
    {   
        private readonly string filepath = Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).FullName, @"Startup/perfcollect");
        ProcessHelper perfcollectProcess;
        public Perfcollect(Logger logger)
        {
            if (!File.Exists(filepath))
            {
                throw new FileNotFoundException($"Pefcollect not found at {filepath}. Please rebuild the project to download it.");
            }

            perfcollectProcess = new ProcessHelper(logger)
            {
                ProcessWillExit = true,
                Executable = "sudo",
                Timeout = 300
            };

            Install();
        }

        public void StartLttng()
        {

        }

        public void Install()
        {
            perfcollectProcess.Arguments = $"./{filepath} install";
            var runResult = perfcollectProcess.Run();
        }
    }
}
