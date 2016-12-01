
#function for filepath, directorys, files, usedspace in windows


# import os
# from os.path import join, getsize
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


"""Complete working formatted operation with comments for creating filepath,
    directory, file and usedspace values - yet to be defined as a function"""
# import os
# from os.path import join, getsize
#
# #uses os.walk to scan the selected dir, returns 3 argumennts.
# for filepath, directorys, files in os.walk("C:\\Users\Admin\Desktop\Test"):
#
#     #prints the filepath argument
#     print(filepath,)
#
#     """uses os.path.join to append all files in filepath to a single argument called name,
#         os.path.getsize queries using os.stat to return the bytesize value for each segment
#          of the name argument. sum adds the values, which is then assigned the identifier
#          "filesize" """
#     filesize = sum([getsize(join(filepath, name)) for name in files])
#     print("consumes", filesize, "bytes", )
#
#     #the len function then counts all values in the list "files", then prints with byt
#     print("in", (len(files)), "files", "\n ")
#
#
#



"""function for converting filesize in bytes to kb, mb, gb"""


#need to test and remove the floating point values
# bitesize = int(input("enter bytes"))
#
# def filesize(bytesize):
#
#     divided = (bytesize / 1024)
#
#     if divided <= 1024:
#         return str(divided) + "Kb"
#
#     elif divided >= 1025 and divided <= 1024000:
#         return str(divided) + "Mb"
#
#     elif divided >= 1024001 and divided <= 1024000000:
#         return str(divided) + "Gb"
#
# filesize(bitesize)
# divided = filesize(bitesize)
# print (divided)

#lookup psutil for total drive space
# and statvfs for linux


#working, need to get the data sizes correct.
#outputs to 2 dec places
#change the function to divide by 1024 at each threshold
#this will correct the values

bitesize = int(input("enter bytes"))

def filesize(bytesize):

    divided = (bytesize / 1020)

    if divided < 1024:
        return "%.2f" % divided + "Kb"

    elif divided <= 1024:
        return "%.2f" % divided + "Mb"

    elif divided >= 1025 and divided <= 1024000:
        return "%.2f" % divided + "Gb"

    elif divided >= 1024001 and divided <= 1024000000:
        return "%.2f" % divided + "Tb"



filesize(bitesize)
divided = filesize(bitesize)
print (divided)
