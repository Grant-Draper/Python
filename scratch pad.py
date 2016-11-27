# import platform
# print (platform.uname())
# print (platform.processor())
# print (platform.release())
# print (platform.machine())
#
#
# import os
#
# for entry in os.scandir("c:"):
#    print entry.name
#
#
#
#

   # if not entry.name.startswith('.') and entry.is_file():
   #     print

from os import scandir

path = "C:\\"

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

if __name__ == '__main__':
    import sys
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
        print(entry.path)