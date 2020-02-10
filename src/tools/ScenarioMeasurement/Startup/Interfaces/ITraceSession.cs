namespace Interfaces{
    internal interface ITraceSession{
        void EnableUserProvider();
        void EableKernelProvider();
        void Stop();
    }
}