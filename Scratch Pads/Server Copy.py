"""**********************************************************
            Grant Draper SFC5 - Net Mon Tool (Server)
                Script Pre-Requisites

                Python 3.6 Interpreter
                Modules: psutil 5.01
**********************************************************"""

import socket, ssl, json, select

"""starting to try and implement sockets"""


def FileScan(python_data):
    while True:
        while True:
            # Identifier Options
            print(python_data[0])
            print(python_data[1])

            print("Filepath:", python_data[7])
            for s in (python_data[5]):
                print("Directory has", python_data[4], "files, which consume", s)
            # print("Total number of files:", python_data[4])
            print("Contents:")
            for i in (python_data[3]):
                print(i)
            print(" ")
            print(" ")
            break
        print("Directory Scanned:", python_data[2])
        print("Total Size of Directory:", python_data[6])
        break
    return
















Host = ""
Port = 30000


master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
master_socket.setblocking(0)
master_socket.bind((Host, Port))
master_socket.listen(1)

sockets = []
sockets.append(master_socket)


def Listening():

    while True:
        (readable, writable, exceptional) = select.select(sockets, [], sockets)

        for s in readable:
            if s is master_socket:
                (client, _) = master_socket.accept()
                ssl_socket = ssl.wrap_socket(client, server_side=True, certfile="server.crt", keyfile="server.key")
                ssl_socket.setblocking(0)
                sockets.append(ssl_socket)

            else:
                incoming_data = ssl_socket.read()

                if not incoming_data:
                    ssl_socket.shutdown(socket.SHUT_RDWR)
                    ssl_socket.close()
                    sockets.remove(ssl_socket)
                else:
                    decoded_data = incoming_data.decode("UTF-8")
                    python_data = json.loads(decoded_data)
                    outgoing_data = "Server Received Data"
                    ssl_socket.write(outgoing_data.encode("UTF-8"))

                    if python_data[0] == "TimeStamp":
                        print(python_data[0])
                        print(python_data[1])
                    elif python_data[0] == "PlatformInfo":
                        print(python_data[0])
                        print(python_data[1])

                        items = []
                        for i in python_data[2]:
                            items.append(i)

                        #print(items)
                        print("Device hostname:              ", items[1])
                        print("Operating system:             ", items[0])
                        print("Operating system release:     ", items[2])
                        print("Operating system version:     ", items[3])
                        print("Machine type:                 ", items[4])
                        print("Processor type:               ", items[5], "\n ", "\n ")

                    # elif python_data[0] == "Partitions":
                    #     print(python_data[0])
                    #     print(python_data[1])
                    #
                    #     items = []
                    #     for i in python_data[2]:
                    #         items.append(i)
                    #     print(items)

                    elif python_data[0] == "PartUsage":
                        #print(python_data)
                        print(python_data[0])
                        print(python_data[1])

                        part = []
                        usage = []
                        for i in python_data[2]:
                            part.append(i)
                        for i in python_data[3]:
                            usage.append(i)

                        for i in part:
                            print(i[0])
                            print("Total Space: ", usage[0])
                            print("Used Space:  ", usage[0])
                            print("Free Space:  ", usage[0])







                        print(part)
                        print(usage)
                        #print("Total Space: ", (SizeConverter(items[0])))
                        #print("Used Space: ", (SizeConverter(items[1])))
                        #print("Free Space: ", (SizeConverter(items[2])), "\n ")




                    elif python_data[0] == "FileScan":
                        FileScan(python_data)


                    else:
                        print("invalid")




Listening()


    # print("Device network name: %s" % (python_data[1]))
    # print("Operating system: %s" % (python_data[0]))
    # print("Operating system release: %s" % (python_data[2]))
    # print("Operating system version: %s" % (python_data[3]))
    # print("Machine type: %s" % (python_data[4]))
    # print("Processor type: %s" % (python_data[5]), "\n ", "\n ")









