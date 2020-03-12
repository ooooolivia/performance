using System;
using Startup;
using ScenarioMeasurement;

namespace PerfcollectTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Perfcollect perfcollect = new Perfcollect("wrapper-kernel-1", new Logger("name.log"));
            perfcollect.Events = Perfcollect.EventOptions.ProcessLifetime;
            var result = perfcollect.Start();
            Console.WriteLine(result);
        }
    }
}