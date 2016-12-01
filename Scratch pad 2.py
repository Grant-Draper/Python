
#function for filepath, directorys, files, usedspace in windows


import os
from os.path import join, getsize
#
#
#
#
# def win_fs:
#     """function for filepath, directorys, files, usedspace in windows"""
#     for filepath, directorys, files in os.walk("C:\\Users\Admin\Desktop\Test"):
#
#         print(filepath, "consumes",)
#         print(sum([getsize(join(filepath, name)) for name in files]),)
#         print("bytes in", len(files), "non-directory files")
#
#
#         return filepath
#
#
# win_fs
#
#
# filepath = fp
# print ("my ", fp)




#uses os.walk to scan the selected dir, returns 3 argumennts.
for filepath, directorys, files in os.walk("C:\\Users\Admin\Desktop\Test"):

    #prints the filepath argument
    print(filepath,)

    """uses os.path.join to append all files in filepath to a single argument called name,
        os.path.getsize queries using os.stat to return the bytesize value for each segment
         of the name argument. sum adds the values, which is then printed"""
    print("consumes", (sum([getsize(join(filepath, name)) for name in files])), "bytes", )

    #the len function then counts all values in the list "files", then prints with byt
    print("in", (len(files)), "files", "\n ")

