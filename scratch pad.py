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

# from os import scandir

# path = "C:\\"
#
# def scantree(path):
#     """Recursively yield DirEntry objects for given directory."""
#     for entry in scandir(path):
#         if entry.is_dir(follow_symlinks=False):
#             yield from scantree(entry.path)  # see below for Python 2.x
#         else:
#             yield entry
#
# if __name__ == '__main__':
#     import sys
#     for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
#         print(entry.path)

# import os
#
# # path = os.walk("C:\\")
# #
# # print (path)
#
# #
# # for path, dirs, files in os.walk("C:\\Users\Admin\Desktop\Test"):
# #   print (path)
#
#   # for d in dirs:
#   #   print (d)
#   #
#   # for f in files:
#   #   print (f)



import os
from os.path import join, getsize
#file path for QA
#fs = os.walk("C:\\Users\Admin\Desktop\Test")

#filepath for home
fs = os.walk("C:\\Users\grant\Desktop\Training")
print (fs)

for a, b, c in fs:
    print (fs.a)
    print (fs.b, fs.c )
#    print [getsize() for a]
# import os
# from os.path import join, getsize
#
# for root, dirs, files in os.walk("C:\\Users\Admin\Desktop\Test"):
#  # print(root, "consumes ", end="")
#    print(sum([getsize(join(root, name)) for name in files]), end="")
# #  print(" bytes in", len(files), "non-directory files")
#
#    print ([getsize for files in ])
#
# #  print (root ,"consumes", )
#  # print(dirs)

#   #print (files)




#working code extracted from help(os.walk)

import os
    from os.path import join, getsize

    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum([getsize(join(root, name)) for name in files]), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories














import os
from os.path import join, getsize


for root, dirs, files in os.walk("C:\\Users\Admin\Desktop\Test"):
#
#   print(root, "consumes",)
#
#    print(
#        sum([getsize(join(root, name)) for name in files]),)
#
#   print("bytes in", len(files), "non-directory files")


    print ([getsize for files in "C:\\"])
    print("bytes in", len(files), "non-directory files")

    print("break")

    print([getsize(join(root, name)) for name in files])