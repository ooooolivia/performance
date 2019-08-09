import os
import shutil


def __copy_assets():
    asset = "../assets/NetCoreApp"
    try:
        shutil.copytree(asset, os.path.basename(asset))
        print("Copied asset %s to the test directory" % asset)
    except shutil.Error as e:
        print("Asset not copied. Error: %s" % e)
    except OSError as e:
        print("Asset not copied. Error: %s" % e)


def __build_tool():
    # proj_working_dir = "..\\..\\Startup"
    # proj_file = os.path.join(proj_working_dir, "Startup.csproj")
    # bin_dir = proj_working_dir
    #
    # proj = dotnet.CSharpProject(
    #     project=dotnet.CSharpProjFile(file_name=proj_file, working_directory=proj_working_dir),
    #     bin_directory=bin_dir,
    # )
    #
    # proj.build(
    #     configuration="release",
    #     target_framework_monikers="netcoreap2.2",
    #     verbose=False,
    #     packages_path="",
    # )\
    # TODO: a oneline code is doable in my env; however more arguments will be needed to determine the dotnet version \
    #  on the user's computer or helix machine
    os.system('dotnet build -c release -f netcoreapp2.2 ..\\..\\Startup\\Startup.csproj')


def __main() -> int:
    __copy_assets()
    __build_tool()


if __name__ == '__main__':
    __main()



