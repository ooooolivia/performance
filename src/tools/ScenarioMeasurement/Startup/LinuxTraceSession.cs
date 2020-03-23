using System;
using System.Collections.Generic;
using System.Text;

namespace ScenarioMeasurement
{
    class LinuxTraceSession : ITraceSession
    {
        private PerfCollect perfcollect;
        private Dictionary<TraceSessionManager.KernelKeyword, PerfCollect.KernelKeyword> linKwMapKernel;
        private Dictionary<TraceSessionManager.ClrKeyword, PerfCollect.ClrKeyword> linKwMapClr;

        public LinuxTraceSession(string sessionName, string traceName, string traceDirectory, Logger logger)
        {
            perfcollect = new PerfCollect(traceName, traceDirectory, logger);
            InitLinuxKeywordMaps();
        }

        public void EnableProviders(IParser parser)
        {
            // Enable both providers and start the session
            parser.EnableKernelProvider(this);
            parser.EnableUserProviders(this);
            perfcollect.Start();
        }

        public void Dispose()
        {
            perfcollect.Stop();
        }

        public void EnableKernelProvider(params TraceSessionManager.KernelKeyword[] keywords)
        {
            // Create keyword list for linux events
            var pcKernelKeywords = new List<PerfCollect.KernelKeyword>();
            foreach (var keyword in keywords)
            {
                pcKernelKeywords.Add(linKwMapKernel[keyword]);
            }
            perfcollect.KernelEvents = pcKernelKeywords;
        }

        public void EnableUserProvider(params TraceSessionManager.ClrKeyword[] keywords)
        {
            // Create keyword list for linux events
            var pcClrKeywords = new List<PerfCollect.ClrKeyword>();
            foreach (var keyword in keywords)
            {
                pcClrKeywords.Add(linKwMapClr[keyword]);
            }
            perfcollect.ClrEvents = pcClrKeywords;
        }

        private void InitLinuxKeywordMaps()
        {
            // initialize linux kernel keyword map
            linKwMapKernel = new Dictionary<TraceSessionManager.KernelKeyword, PerfCollect.KernelKeyword>();
            linKwMapKernel[TraceSessionManager.KernelKeyword.Process] = PerfCollect.KernelKeyword.ProcessLifetime;
            linKwMapKernel[TraceSessionManager.KernelKeyword.Thread] = PerfCollect.KernelKeyword.Thread;
            linKwMapKernel[TraceSessionManager.KernelKeyword.ContextSwitch] = PerfCollect.KernelKeyword.ContextSwitch;

            // initialize linux clr keyword map
            linKwMapClr = new Dictionary<TraceSessionManager.ClrKeyword, PerfCollect.ClrKeyword>();
            linKwMapClr[TraceSessionManager.ClrKeyword.Startup] = PerfCollect.ClrKeyword.DotNETRuntimePrivate_StartupKeyword;
        }

        public void EnableUserProvider(string provider)
        {
        }
    }
}
