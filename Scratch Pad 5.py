
import os
from os.path import join, getsize



def root_info():
    #uses os.walk to scan the selected dir, returns 3 arguments.

    #creats empty totalsize attribute
    totalsize = 0

    #dir = []

    while True:
         for filepath, directorys, files in os.walk("C:\\Users\Grant\Downloads\Test"):

            #prints the filepath argument
            #print(filepath)
            #print(filepath[:])
            """print(directorys)
            print(directorys[0:0])
            print(directorys[0:1])
            print(directorys[0:2])
            print(directorys[0:3])"""
            #print(files)
            #print(files[:])
            #print(files[0:((len(files)))])
            #print(os.walk("C:\\Users\Grant\Downloads\Test"))

            """uses os.path.join to append all files in filepath to a single argument called name,
                os.path.getsize queries using os.stat to return the bytesize value for each segment
                    of the name argument. sum adds the values, which is then assigned the identifier
                        "filesize" """
            #filesize = sum([getsize(join(filepath, name)) for name in files])
            #print("consumes", filesize, "bytes", )

            #the len function then counts all values in the list "files", then prints with byt
            #print("in", (len(files)), "files")

            #totalsize.append(filesize)
            #totalsize += filesize
            #print (totalsize)



         break

    return files, totalsize

files, totalsize = root_info()


"""this function works, it finds the total of the files in the directory
    then seperatly calculates the space information of directorys under
    the root dir specified

    need to work out how to append all the values into a concise total
    which can then be passed to filesize() function"""

print(files)

#print()
#fs = root_info()

#print (root_info())