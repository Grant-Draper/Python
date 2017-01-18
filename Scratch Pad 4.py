# import os
#
# print (os.getlogin())
#
# pid = os.getpid()
# print (os.getpgid(pid))
# print (os.getpgrp(pid))





import os
from os.path import join, getsize

def root_info():
    #uses os.walk to scan the selected dir, returns 3 argumennts.
    for filepath, directorys, files in os.walk("C:\\Users\Grant\Downloads\Test"):

        #prints the filepath argument
        print(filepath,)

        """uses os.path.join to append all files in filepath to a single argument called name,
           os.path.getsize queries using os.stat to return the bytesize value for each segment
            of the name argument. sum adds the values, which is then assigned the identifier
             "filesize" """
        filesize = sum([getsize(join(filepath, name)) for name in files])
        print("consumes", filesize, "bytes", )

        #the len function then counts all values in the list "files", then prints with byt
        print("in", (len(files)), "files", "\n ")

    return filesize

"""this function works, it finds the total of the files in the directory
    then seperatly calculates the space information of directorys under
    the root dir specified

    need to work out how to append all the values into a concise total
    which can then be passed to filesize() function"""



#fs = root_info()

print (root_info())