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


#testing psutil library

import psutil


# print (psutil.disk_partitions())
#
# FS = psutil.disk_partitions()
# print (FS[0])
# print (FS[1])
# print (FS[2])
#
# print (psutil.disk_usage("/"))
# print (psutil.disk_usage("C:\\"))
# print (psutil.disk_usage("F:\\"))

# users = psutil.users()
# print (users)
# print (users[0])
# #print (users[1])
#print (users[2])

PID = psutil.pids()
print (PID[1])
Proc = psutil.Process(PID[1])
print (Proc)
print (Proc.name())

#attempting to create a loop that will iterate through every
#pid outputted from psutil.pids(), getting the process name and info

for i in PID:
    print (psutil.Process(PID)
    #print (.name())

else:
    print("Failed")



# print ("this is a spacer")
#
# #print (psutil.disk_usage("/"))
#
#
# usage = psutil.disk_usage("/")
# print ("Total Space: ", (filesize(usage[0])))
# print ("Used Space: ", (filesize(usage[1])))
# print ("Free Space: ", (filesize(usage[2])))
#
# # print (filesize(usage[0]))
# print (filesize(usage[1]))
# print (filesize(usage[2]))

# print (psutil.net_connections())
# print (psutil.net_if_addrs())
#
# ipaddr = psutil.net_if_addrs()
#
# print (ipaddr{1})