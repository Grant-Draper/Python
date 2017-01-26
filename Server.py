"""**********************************************************
            Grant Draper SFC5 - Net Mon Tool (Server)
                Script Pre-Requisites

                Python 3.6 Interpreter
                Modules: psutil 5.01
**********************************************************"""

import socket, ssl, json

"""starting to try and implement sockets"""



def OpenServerConnection():
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_socket.bind(('', 30000))
    master_socket.listen(1)
    return master_socket


s = OpenServerConnection()
newsock, newaddr = s.accept()
ssl_socket = ssl.wrap_socket(newsock, server_side=True, certfile="server.crt", keyfile="server.key")

# reads data from the socket and assigns it to a local variable
incoming_data = ssl_socket.read()

# decodes the variable from UTF-8 and prints
decoded_data = incoming_data.decode("UTF-8")

# additions
python_data = json.loads(decoded_data)

# assigns a variable an ACK message
outgoing_data = "Server Received Data"

# encodes the outgoing data in UTF-8 and writes it to the socket
ssl_socket.write(outgoing_data.encode("UTF-8"))

# pauses the socket
ssl_socket.detach()




# closes the connection
#ssl_socket.close()









if python_data[0] == "FileScan":
    while True:
        while True:
            # Identifier Options
            print(python_data[0])
            print(python_data[1])

            print("Filepath:", python_data[7])
            for s in (python_data[5]):
                print("Directory has", python_data[4], "files, which consume", s)
            #print("Total number of files:", python_data[4])
            print("Contents:")
            for i in (python_data[3]):
                print(i)
            print(" ")
            print(" ")
            break
        print("Directory Scanned:", python_data[2])
        print("Total Size of Directory:", python_data[6])
        break




elif python_data[0] == "TimeStamp":
    print(python_data)

elif python_data[0] == "PlatformInfo":
    print(python_data)

    print("Device network name: %s" % (python_data[1]))
    print("Operating system: %s" % (python_data[0]))
    print("Operating system release: %s" % (python_data[2]))
    print("Operating system version: %s" % (python_data[3]))
    print("Machine type: %s" % (python_data[4]))
    print("Processor type: %s" % (python_data[5]), "\n ", "\n ")

elif python_data[0] == "Partitions":
    print(python_data)







else:
    print("invalid")
