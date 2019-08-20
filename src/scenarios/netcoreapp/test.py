from sdk import SDKRunner

runner = SDKRunner(scenario_name='Build NetCoreApp', project_file='NetCoreApp\\NetCoreApp.csproj')
runner.build_clean()
runner.build_no_changes()