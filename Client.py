
#
#
#
# print platform.machine()
# print platform.version()
# print platform.platform()
# print platform.uname()
# print platform.system()
# print platform.processor()
#
# print "break"
#
# #find the version number of any module
# print platform.__version__


import platform
from datetime import datetime

print("Gather system information Y/N")
start = input()
start = start.lower()

if start == "y":
    timestamp = datetime.now()
    platforminfo = platform.uname()

    print ("Sys info capture time: %s:%s" % (timestamp.hour, timestamp.minute))
    print ("Sys info capture date: %s/%s/%s" % (timestamp.day, timestamp.month, timestamp.year))
    print ("Device network name: %s" % (platforminfo[1]))
    print ("Operating system: %s" % (platforminfo[0]))
    print ("Operating system release: %s" % (platforminfo[2]))
    print ("Operating system version: %s" % (platforminfo[3]))
    print ("Machine type: %s" % (platforminfo[4]))
    print ("Processor type: %s" % (platforminfo[5]))


elif start == "n":
    print ("Fine be that way!")
else:
    print ("Please enter a value in range")



