'''
Iteration setup script for clean build
'''

from shutil import copytree, rmtree
import os
from shared import const
import sys
import dotnet
from performance.logger import setup_loggers
from logging import getLogger


# prerequisite: the asset has been copied to tmp in pre.py
def main():

    setup_loggers(verbose=True)

    getLogger().info("Shutting down dotnet servers...")
    dotnet.shutdown_server(verbose=True)

    getLogger().info("Cleaning project folder...")
    tmp = os.path.join(const.TMPDIR, const.APPDIR)
    # check if a copy exists before deleting the folder
    if not os.path.isdir(tmp):
        getLogger().error("Please run pre.py to copy the asset first.")
        sys.exit(1)
    rmtree(const.APPDIR)
    copytree(tmp, const.APPDIR)


if __name__ == "__main__":
    main()
