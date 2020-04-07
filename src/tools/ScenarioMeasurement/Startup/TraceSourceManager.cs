﻿using Microsoft.Diagnostics.Tracing;
using Microsoft.Diagnostics.Tracing.Parsers;
using Microsoft.Diagnostics.Tracing.Parsers.Kernel;
using Microsoft.Diagnostics.Tracing.Parsers.LinuxKernel;
using System;

namespace ScenarioMeasurement
{

    public class TraceSourceManager : IDisposable
    {
        public bool IsWindows { get { return Source?.GetType() == typeof(ETWTraceEventSource);  } }
        public TraceEventDispatcher Source;
        private IKernelParser _kernel;
        public IKernelParser Kernel
        {
            get
            {
                if (_kernel == null)
                {
                    if (IsWindows)
                    {
                        _kernel = new WindowsKernelParser((ETWTraceEventSource)Source);
                    }
                    else
                    {
                        _kernel = new LinuxKernelParser((CtfTraceEventSource)Source);
                    }
                }
                return _kernel;
            }
        }

        public TraceSourceManager(string fileName)
        {
            Source = TraceEventDispatcher.GetDispatcherFromFileName(fileName);
        }

        public void Process()
        {
            Source.Process();
        }

        public void Dispose()
        {
            Source.Dispose();
        }

    }

    public interface IKernelParser
    {
        public event Action<TraceEvent> ProcessStart;
        public event Action<TraceEvent> ProcessStop;
        public event Action<TraceEvent> ContextSwitch;
        public string GetEventCommandLine(TraceEvent evt);
        public int GetPayloadThreadID(TraceEvent evt);
    }

        public sealed class LinuxKernelParser : IKernelParser
    {
        LinuxKernelEventParser parser;
        public event Action<TraceEvent> ProcessStart { add { parser.ProcessStart += value; } remove { parser.ProcessStart -= value; } }
        public event Action<TraceEvent> ProcessStop { add { parser.ProcessStop += value; } remove { parser.ProcessStop -= value; } }
        public event Action<TraceEvent> ContextSwitch { add { } remove { } } // not implemented
        public LinuxKernelParser(CtfTraceEventSource source) {
            parser = new LinuxKernelEventParser(source);
        }

        public string GetEventCommandLine(TraceEvent evt)
        {
            Console.WriteLine("Not applicable to Linux Kernel event payload.");
            return "";
        }

        public int GetPayloadThreadID(TraceEvent evt)
        {
            return ((ProcessStopTraceData)evt).PayloadThreadID;
        }
    }

    public sealed class WindowsKernelParser : IKernelParser
    {
        KernelTraceEventParser parser;
        public event Action<TraceEvent> ProcessStart { add { parser.ProcessStart += value; } remove { parser.ProcessStart -= value; } }
        public event Action<TraceEvent> ProcessStop { add { parser.ProcessEndGroup += value; } remove { parser.ProcessEndGroup -= value; } }
        public event Action<TraceEvent> ContextSwitch { add { parser.ThreadCSwitch += value;  } remove { parser.ThreadCSwitch -= value; } } 
        
        public WindowsKernelParser(ETWTraceEventSource source)
        {
            parser = new KernelTraceEventParser(source);
        }

        public string GetEventCommandLine(TraceEvent evt)
        {
            return ((ProcessTraceData)evt).CommandLine;
        }

        public int GetPayloadThreadID(TraceEvent evt)
        {
            Console.WriteLine("Not applicable to ETW Kernel event payload.");
            return 0;
        }
    }

}
