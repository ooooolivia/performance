from shutil import copytree, rmtree
import os
from shared import const
from logging import getLogger
import sys
import dotnet


# prerequisite: the asset has been copied to tmp in pre.py
def main():
    sys.stdout.write("Shutting down dotnet servers...\n")
    dotnet.shutdown_server(verbose=True)

    sys.stdout.write("Cleaning project folder...\n")
    tmp = os.path.join(const.TMPDIR, const.APPDIR)
    # check if a copy exists before deleting the folder
    if not os.path.isdir(tmp):
        sys.stderr.write("Please run pre.py to copy the asset first.\n")
        sys.exit(1)
    rmtree(const.APPDIR)
    copytree(tmp, const.APPDIR)


if __name__ == "__main__":
    main()
