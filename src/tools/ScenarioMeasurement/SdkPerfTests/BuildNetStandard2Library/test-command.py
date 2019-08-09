import os


def __main():
    project = "..\\..\\Startup\\Startup.csproj"
    app_exe = "dotnet.exe"
    app_args = "\"build -c release -f netstandard2.0 NetCoreApp\\NetCoreApp.csproj\""
    command = 'dotnet run -c release -f netcoreapp2.2 --project %s -- \
    --app-exe %s \
    --app-args %s \
    --metric-type ProcessTime \
    --scenario-name test-process-time \
    --process-will-exit \
    --trace-file-name process-time-trace-file.etl \
    --iterations 3 \
    --skip-profile-iteration \
    --gui-app false' % (project, app_exe, app_args)

    print("======== build no clean ==========")
    os.system(command+' --warmup true')

    print("======== clean build =============")
    iteration_setup = "dotnet.exe"
    # setup_args = "\"clean NetCoreApp\\NetCoreApp.csproj\""
    # os.system(command+' --warmup false'+' --iteration-setup %s' % iteration_setup + ' --setup-args %s' % setup_args)


if __name__ == '__main__':
    __main()
