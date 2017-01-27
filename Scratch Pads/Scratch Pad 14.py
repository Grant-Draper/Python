import psutil

def SizeConverter(bytesize):

    """Function called SizeConverter to make human readable the output from bytecount operations.
        Input in Bytes, Output is in the most appropriate formmat, depending on size. E.g.
        rather than saying 10240 Mb, it will display 10 Gb

        Converts bytes to Kb, Mb, Gb, Tb to 2 decimal places"""

    if bytesize <= 1024:
        divided = bytesize
        return divided + " B"

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




# fn = "PartUsage"
# host = Host
# part = psutil.disk_partitions()
# null = []
# usage = {}
#
#
#
# for i in part:
#     print(i.device + "\\")
#     usage.update(i.device + "\\")
#     print(usage.keys())
#
#     try:
#         null = psutil.disk_usage(i.device + "\\")
#
#         for i in null:
#
#             if (i.device + "\\") in usage:
#                 usage[i.device + "\\"].append(SizeConverter(i))
#                 print(usage)
#             else:
#                 usage[i.device] = (SizeConverter(i))
#                 print(usage)
#             print(usage)
#
#


# drives = []
# test = {}
# usage = []
# part = psutil.disk_partitions()
#
# for i in part:
#     try:
#     #usage.append(psutil.disk_usage(i.device + "\\"))
#         test[i.device] = (psutil.disk_usage(i.device + "\\"))
#
#     except Exception as e:
#         print(e)
#         pass
#
#
#
#
#
# print (test)
# print(test.keys())

test = {}
part = psutil.disk_partitions()

def PartUsage:

    for i in part:

        try:
            usage = psutil.disk_usage(i.device + "\\")
            for u in usage:
                test[i.device] = (SizeConverter(usage[0])), (SizeConverter(usage[1])), (SizeConverter(usage[2]))

        except Exception as e:
            print(e)
            print("Drive unable to be scanned. Usually empty CDROM or Floppy drive.", "\n")
            test[i.device] = ("exception"), ("Drive unable to be scanned. Usually empty CDROM or Floppy drive")
            pass

    JSONData = json.dumps(test)
    return JSONData


for key in test:
    try:

        value = test[key]

        if value[0] == "exception":
            print(key)
            print(value[1], "\n")

        else:
            print(key)
            print(value[0])
            print(value[1])
            print(value[2], "\n")

    except Exception as e:
        print(e)
        pass




# for i in psutil.disk_partitions():
#     test[i.device] = SizeConverter(int(psutil.disk_usage(i.device + "\\")))
#
# print(test)


#print(psutil.disk_usage())

