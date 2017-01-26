
"""**********************************************************
            Grant Draper SFC5 - Net Mon Tool (Client)
                Script Pre-Requisites

                Python 3.6 Interpreter
                Modules: psutil 5.01
**********************************************************"""




import os, platform, psutil, pprint, socket, ssl, json
from os.path import join, getsize
from datetime import datetime



def SizeConverter(bytesize):

    """Function called SizeConverter to make human readable the output from bytecount operations.
        Input in Bytes, Output is in the most appropriate formmat, depending on size. E.g.
        rather than saying 10240 Mb, it will display 10 Gb

        Converts bytes to Kb, Mb, Gb, Tb to 2 decimal places"""

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



def FileScan(path):

    """Function called FileScan to read a specified directory 'Path', the function uses
        os.walk() to walk through filepaths, directorys and files. Prints all values for
        each directory and its contents.

        This function also finds the total size of the files in each directory it scans.
        The function will also find the total size consumed by the scans root directory
        (where the scan started)

        This function can take some time to run depending on the complexity of the
        file structure."""

    totalsize = 0
    filelist = []
    sizes = []

    while True:

        # uses os.walk to scan the selected dir, returns 3 arguments.
        for filepath, directorys, files in os.walk(path):

            fn = "FileScan"
            host = ""

            filesize = sum([getsize(join(filepath, name)) for name in files])

            for i in files:
                filelist.append(i)

            sizes.append(SizeConverter(filesize))
            numfiles = (len(files))
            totalsize += filesize

            JSONData = json.dumps((fn, host, path, filelist, numfiles, sizes, SizeConverter(totalsize), filepath))
        break
    return JSONData



#result = FileScan("c:\\users\\admin\\downloads")








def OpenClientConnection(outgoing_data):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_socket = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
        ssl_socket.connect(("localhost", 30000))

    except Exception as e:
        print(e)
        print("Completed with Exception1.", "\n")
        pass

    try:
        # encodes the outgoing data in UTF-8 and writes it to the socket
        ssl_socket.write(outgoing_data.encode("UTF-8"))

        # reads data from the socket and assigns it to a local variable
        incoming_data = ssl_socket.read()

        # decodes the variable from UTF-8 and prints
        print(incoming_data.decode("UTF-8"))

        # pauses the socket
        #ssl_socket.detach()

        # closes the connection
        ssl_socket.close()

    except Exception as e:
        print(e)
        print("Completed with Exception2.", "\n")
        pass
        return







def TimeStamp():
    fn = "TimeStamp"
    host = ""
    timestamp = datetime.now()
    JSONData = json.dumps((fn, host, str(timestamp)))
    return JSONData

def PlatformInfo():
    fn = "PlatformInfo"
    host = ""
    platforminfo = platform.uname()
    JSONData = json.dumps((fn, host, platforminfo))
    return JSONData

def Partitions():
    fn = "Partitions"
    host = ""
    part = psutil.disk_partitions()
    JSONData = json.dumps((fn, host, part))
    return JSONData

def User():
    fn = "User"
    host = ""
    user = psutil.users()
    JSONData = json.dumps((fn, host, user))
    return JSONData

def PSTable():
    fn = "PSTable"
    host = ""
    pstable = psutil.test()
    JSONData = json.dumps((fn, host, pstable))
    return JSONData

def NICs():
    fn = "NICs"
    host = ""
    nics = psutil.net_if_stats()
    JSONData = json.dumps((fn, host, nics))
    return JSONData

def NICAddr():
    fn = "NICAddr"
    host = ""
    nicaddr = psutil.net_if_addrs()
    JSONData = json.dumps((fn, host, nicaddr))
    return JSONData

def Sockets():
    fn = "Sockets"
    host = ""
    sockets = psutil.net_connections()
    JSONData = json.dumps((fn, host, sockets))
    return JSONData




def PartUsage():
    fn = "PartUsage"
    host = ""
    part = psutil.disk_partitions()
    null = []
    usage = {}

    for i in part:
        print(i.device + "\\")

        try:
            null = psutil.disk_usage(i.device + "\\")
            for i in null:
                if key in usage:
                    usage[key1].append(SizeConverter(i))
                else:
                    usage[key1] = (SizeConverter(i)

                # part = {i.device: (SizeConverter(i)  }
                # usage.append(part)
                # SizeConverter(i)
                #
                # for i in usage:
                #     usage = SizeConverter(i)

        except Exception as e:
            print(e)
            print("Drive unable to be scanned. Usually empty CDROM or Floppy drive.", "\n")
            pass
        print(usage[0])
        # usage[0] = SizeConverter(usage[0])
        # usage[1] = SizeConverter(usage[1])
        # usage[2] = SizeConverter(usage[2])

        JSONData = json.dumps((fn, host, part, usage))
    return JSONData






#OpenClientConnection(FileScan("f:\\video"))
#OpenClientConnection(FileScan("c:\\users\\admin\\downloads"))
OpenClientConnection(TimeStamp())
OpenClientConnection(PlatformInfo())
#OpenClientConnection(Partitions())
#OpenClientConnection(PartUsage())
OpenClientConnection(User())
#OpenClientConnection(PSTable())
OpenClientConnection(NICs())
#OpenClientConnection(NICAddr())
#OpenClientConnection(Sockets())



#print("Sys info capture time: %s:%s" % (timestamp.hour, timestamp.minute))
# print("Sys info capture date: %s/%s/%s" % (timestamp.day, timestamp.month, timestamp.year))
# print("Device network name: %s" % (platforminfo[1]))
# print("Operating system: %s" % (platforminfo[0]))
# print("Operating system release: %s" % (platforminfo[2]))
# print("Operating system version: %s" % (platforminfo[3]))
# print("Machine type: %s" % (platforminfo[4]))
# print("Processor type: %s" % (platforminfo[5]), "\n ", "\n ")

