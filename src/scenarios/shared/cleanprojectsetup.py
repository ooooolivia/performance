from shutil import copytree, rmtree
import sys
import os
from shared import const


# prerequisite: the asset has been copied to tmp in pre.py
def main():
    src = sys.argv[1]
    tmp = os.path.join(const.TMPDIR, src)
    assert(os.path.isdir(tmp))
    if os.path.isdir(tmp):
        rmtree(src)
        copytree(tmp, src)
    else:
        sys.stderr.write("ERROR: Please run pre.py to copy the asset first.")
        return 1


if __name__ == "__main__":
    exit(main())

