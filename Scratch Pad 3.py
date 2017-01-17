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

print (psutil.disk_partitions())

print ("this is a spacer")

#print (psutil.disk_usage("/"))


usage = psutil.disk_usage("/")
print ("Total Space: ", (filesize(usage[0])))
print ("Used Space: ", (filesize(usage[1])))
print ("Free Space: ", (filesize(usage[2])))

# print (filesize(usage[0]))
# print (filesize(usage[1]))
# print (filesize(usage[2]))
