
"""Complete working formatted operation with comments for creating filepath,
    directory, file and usedspace values - yet to be defined as a function"""
import os
from os.path import join, getsize

#uses os.walk to scan the selected dir, returns 3 argumennts.
for filepath, directorys, files in os.walk("C:\\Users\Grant\Downloads"):

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



#lookup psutil for total drive space
# and statvfs for linux


"""working function to convert bytes to Kb, Mb, Gb, Tb.
    this works by taking the byte value, and dependant on size will
    divide it to resize to the appropriate value to 2 decimal places"""

#replace this input with the value from os.walk
#bitesize = int(input("enter bytes"))

def filesize(bytesize):

    if bytesize <= 1024:
        divided = bytesize
        return str(divided) + " B"

    elif bytesize >= 1025 and bytesize <= 1048576:
        divided = (bytesize / 1024)
        return "%.2f" % divided + " Kb"

    elif bytesize >= 1048577 and bytesize <= 1073741842:
        divided1 = (bytesize / 1024)
        divided = (divided1 / 1024)
        return "%.2f" % divided + " Mb"

    elif bytesize >= 1073741843 and bytesize <= 1099511600000:
        divided2 = (bytesize / 1024)
        divided1 = (divided2 / 1024)
        divided = (divided1 / 1024)
        return "%.2f" % divided + " Gb"

    elif bytesize >= 1099511600001 and bytesize <= 1125899800000000:
        divided3 = (bytesize / 1024)
        divided2 = (divided3 / 1024)
        divided1 = (divided2 / 1024)
        divided = (divided1 / 1024)
        return "%.2f" % divided + " Tb"

# filesize(bitesize)
# divided = filesize(bitesize)
# print (divided)



"""starting to link the filesize conversion function to the os.walk
    function output, to convert the output before presenting to the user"""

import os
from os.path import join, getsize

"""starting to turn os.walk into a function, outputs needed:
    total bytes from all files. possibly total folders and total files"""

def root_info():
    #uses os.walk to scan the selected dir, returns 3 argumennts.
    for filepath, directorys, files in os.walk("C:\\Users\grant\Downloads\Test"):

        #prints the filepath argument
        #print(filepath,)

        """uses os.path.join to append all files in filepath to a single argument called name,
            os.path.getsize queries using os.stat to return the byte_size value for each segment
            of the name argument. sum adds the values, which is then assigned the identifier
            "byte_size" """
        byte_size = sum([getsize(join(filepath, name)) for name in files])
        #print("consumes", (filesize(byte_size)), "bytes", )

        #the len function then counts all values in the list "files" then prints
        #print("in", (len(files)), "files", "\n ")


    return byte_size
        #
        # """trying to add in exception handling to silence errors as the required data
        #     is partially still outputted, total filesize is not accurate, a number of
        #      files are not being read.
        #
        #      disk image files are not being read and outputted when defined as a function,
        #      verified using the test file structure, C:\\Users\grant\Downloads\Test contains
        #      4 dirs
        #      14 files
        #         6 of which are disk image
        #      totaling 15.2gb when using this as a function 8 files are found totaling 5.23gb """
        # #except Exception
        #pass

#root_info()
## print (root_info(byte_size))
#print (byte_size)
fs = root_info()
print(fs)

print (filesize(fs))


# print (root_info(byte_size))




#
# import os
# from os.path import join, getsize
# #
# # def root_info():
# #uses os.walk to scan the selected dir, returns 3 argumennts.
# for filepath, directorys, files in os.walk("C:\\Users\grant\Downloads\Test"):
#
#     #prints the filepath argument
#     print(filepath,)
#
#     """uses os.path.join to append all files in filepath to a single argument called name,
#         os.path.getsize queries using os.stat to return the byte_size value for each segment
#         of the name argument. sum adds the values, which is then assigned the identifier
#         "byte_size" """
#     byte_size = sum([getsize(join(filepath, name)) for name in files])
#     print("consumes", (filesize(byte_size)), "bytes", )
#
#         #the len function then counts all values in the list "files" then prints
#     print("in", (len(files)), "files", "\n ")
#

        #return
        #
        # """trying to add in exception handling to silence errors as the required data
        #     is partially still outputted, total filesize is not accurate, a number of
        #      files are not being read.
        #
        #      disk image files are not being read and outputted when defined as a function,
        #      verified using the test file structure, C:\\Users\grant\Downloads\Test contains
        #      4 dirs
        #      14 files
        #         6 of which are disk image
        #      totaling 15.2gb when using this as a function 8 files are found totaling 5.23gb
#               when ran not as a function all files are found and calculated correctly"""
        #except Exception
        #pass

# root_info()
