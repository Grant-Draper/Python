def SizeConverter(bytesize):
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


import os, pprint, psutil
from os.path import join, getsize





def root_info(path):

    totalsize = 0

    while True:

        for filepath, directorys, files in os.walk(path):

            print(" ")
            print("Filepath: ", filepath)
            filesize = sum([getsize(join(filepath, name)) for name in files])
            print("Total Size of Files:", SizeConverter(filesize))
            print("Contents:")

            for i in files:
                print(i)
            print(" ")
            print(" ")
            totalsize += filesize

        #States the directory scanned, need to add in the function to identify disks
        #then pass that to this function to scan the dirs. Also need to add that value
        #to the "Directory Scanned:" comment below.
        print("Directory Scanned:", path)
        print("Total Size of Directory:", SizeConverter(totalsize))

        break

    return


#root_info("C:\\Users\Admin\Downloads")

print("Would you like to scan for filesystem directory information? Y/N", "\n ")

scan = input()
scan = scan.lower()

if scan == "y":

    print("Please type the filepath you would like to scan, Not Case Sensitive. E.g. C:\\\\Users\Admin\Downloads")
    dir = input()
    dir = dir.lower()

    root_info(dir)



