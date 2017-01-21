
"""**********************************************************
            Grant Draper SFC5 - Net Mon Tool (Client)
                Script Pre-Requisites

                Python 3.6 Interpreter
                Modules: psutil 5.01
**********************************************************"""



# #find the version number of any module
#print platform.__version__


import os, platform, psutil, pprint
from datetime import datetime


def SizeConverter(bytesize):

    """Function called SizeConverter to make human readable the output from bytecount operations.
        Input in Bytes, Output is in the most appropriate formmat, depending on size. E.g.
        rather than saying 10240 Mb, it will display 10 Gb"""

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



"""This asks the user if they are ready to run the capture, only accepts Yy or Nn."""

print("Capture System Information Y/N")
start = input()
start = start.lower()



"""This section checks if the user opted to start the capture, if so creates the variables
    timestamp, platforminfo and part. These can then be manipulated into a more human
    readable format in the next section"""

if start == "y":
    timestamp = datetime.now()
    platforminfo = platform.uname()

    part = psutil.disk_partitions()



    """This section extracts and formats the data gathered from the variables into human readable
    fields"""

    print("Sys info capture time: %s:%s" % (timestamp.hour, timestamp.minute))
    print("Sys info capture date: %s/%s/%s" % (timestamp.day, timestamp.month, timestamp.year))
    print("Device network name: %s" % (platforminfo[1]))
    print("Operating system: %s" % (platforminfo[0]))
    print("Operating system release: %s" % (platforminfo[2]))
    print("Operating system version: %s" % (platforminfo[3]))
    print("Machine type: %s" % (platforminfo[4]))
    print("Processor type: %s" % (platforminfo[5]), "\n ", "\n ")


    """Original root file system information gathering section."""
    #usage = psutil.disk_usage("/")
    #print("Root FS, Total Space: ", (SizeConverter(usage[0])))
    #print("Root FS, Used Space: ", (SizeConverter(usage[1])))
    #print("Root FS, Free Space: ", (SizeConverter(usage[2])), "\n ", "\n ")


    """This loop scans for the drive letters or root mount points of each drive. It then passes
        the values to a function to find disk usage information, the returned values are then
        passed through the SizeConverter function. The resultant values are then printed to
        screen. The whole loop has exception handling, this catches empty drive errors etc, and
        displays both the original error message and a more human readable message."""

    for i in part:
        print(i.device + "\\")

        try:
            usage = psutil.disk_usage(i.device + "\\")
            print("Total Space: ", (SizeConverter(usage[0])))
            print("Used Space: ", (SizeConverter(usage[1])))
            print("Free Space: ", (SizeConverter(usage[2])), "\n ", "\n ")

        except Exception as e:
            print(e)
            print("Drive unable to be scanned. Usually empty CDROM or Floppy drive.", "\n", "\n")
            pass



    print ("Currently Active User:", "\n ")
    print (psutil.users(), "\n ", "\n ")



    print ("System Process Table:", "\n ")
    print(psutil.test(), "\n ", "\n ")



    print ("Network Interfaces:", "\n ")
    pprint.pprint (psutil.net_if_stats())
    print (" ", "\n ", "\n ")



    print ("Network Interface Address Information: ", "\n ")
    pprint.pprint(psutil.net_if_addrs())
    print (" ", "\n ", "\n ")



    print ("System Socket Information: ", "\n ")
    pprint.pprint (psutil.net_connections())
    print (" ", "\n ", "\n ")



    #Function to identify platform then run os specific file structure commands
    if platforminfo[0].lower() == "windows":
        print("windows")
        print("Would you like to scan for filesystem directory information? Y/N", "\n ")
        scan = input()
        scan = scan.lower()

        if scan == "y":


            for i in part:
                print(i.device + "\\")


        elif scan == "n":
            print("FS Scan skipped")
        else:
            print("Please enter a value in range")



    elif platforminfo[0].lower() == "linux":
        print("linux")
    elif platforminfo[0].lower() == "unix":
        print("unix")



elif start == "n":
    print("Fine! be that way!")
else:
    print("Please enter a value in range")



