from shutil import copytree, rmtree
import os
from shared import const
from logging import getLogger
import sys


# prerequisite: the asset has been copied to tmp in pre.py
def main():
    tmp = os.path.join(const.TMPDIR, const.APPDIR)

    # check if a copy exists before deleting the folder
    if not os.path.isdir(tmp):
        getLogger().error("Please run pre.py to copy the asset first.")
        sys.exit(1)

    rmtree(const.APPDIR)
    copytree(tmp, const.APPDIR)


if __name__ == "__main__":
    main()

