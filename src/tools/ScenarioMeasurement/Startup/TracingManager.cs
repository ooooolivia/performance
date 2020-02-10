using System.OperatingSystem;
using Interfaces;
using Linux;

namespace ScenarioMeasurement{
    // help selects platform-specific objects
    class TracingManager{

        // give platform-specific tracing tool
        public static ITraceSession CreateTraceSession(){
            if (OperatingSystem.Platform == System.PlatformID.Win32NT)
            {
                return new WindowsTraceSession();
            }
            else
            {
                return new LinuxTraceSession();
            }
        }

        // give platform-specific parser
        public static IParser GetParser(string parserName){
            // give platform-specific parser
        }

        
    }
}