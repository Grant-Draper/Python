
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

if __name__ == "__main__":
    s = OpenServerConnection()
    newsock, newaddr = s.accept()
    ssl_socket = ssl.wrap_socket(newsock, server_side=True, certfile="server.crt", keyfile="server.key")

    #reads data from the socket and assigns it to a local variable
    incoming_data = ssl_socket.read()

    #decodes the variable from UTF-8 and prints
    decoded_data = incoming_data.decode("UTF-8")


    #additions

    python_data = json.loads(decoded_data)
    print(python_data)
    print(python_data[0])
    print(python_data[1])
    for i in (python_data[1]):
        print(i)



    #assigns a variable an ACK message
    outgoing_data = "Server Received Data"

    #encodes the outgoing data in UTF-8 and writes it to the socket
    ssl_socket.write(outgoing_data.encode("UTF-8"))

    #closes the connection
    ssl_socket.close()

