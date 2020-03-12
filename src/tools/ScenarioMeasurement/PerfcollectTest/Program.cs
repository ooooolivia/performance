using System;
using Startup;
using ScenarioMeasurement;

namespace PerfcollectTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Perfcollect percollect = new Perfcollect("", new Logger("name.log"));
            
        }
    }
}