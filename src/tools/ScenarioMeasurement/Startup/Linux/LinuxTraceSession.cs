using System.Diagnostics;

namespace Linux{
    class LinuxTraceSession : ITraceSession{

        string perfCollectScript = "perfcollect.sh";

        public LinuxTraceSession(string sessionName, string fileName){
            bool installed = CheckInstalled(); 
            if(!installed){
                var psi = CreateProcessStartInfo();
                psi.Arguments = "install";  
                Process.Start(psi);
            }
            
        }

        public void EnableUserProvider(string[] keywords){
            
        }

        public void EnableKernelProvider(string[] keywords){

        }

        private ProcessStartInfo CreateProcessStartInfo(){
            var psi = new ProcessStartInfo();
            psi.FileName = perfCollectScript;
            return psi;
        }

        private bool CheckInstalled(){
            return false;
        }
    }
}