
#server side, multiple connections

import socket
import select

HOST = ""
PORT = 30001

master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
master_socket.setblocking(0)
master_socket.bind((HOST, PORT))
master_socket.listen(1)

#creates a storage area for our connections
sockets = []
sockets.append(master_socket)
print("about to loop")
while True:
    (readable, writable, exceptional) = select.select(sockets, [], sockets)
    #print(readable)
    for s in readable:
        if s is master_socket:
            (client, _) = master_socket.accept()
            client.setblocking(0)
            sockets.append(client)
        else:
            data = s.recv(1024)

            if not data:
                s.shutdown(socket.SHUT_RDWR)
                s.close()
                sockets.remove(s)
            else:
                s.sendall(data)
            #print ("Recieved", repr(data))








# import socket
# import select
#
# HOST = "192.168.1.117"
# PORT = 30001
#
# master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# master_socket.setblocking(0)
# master_socket.bind((HOST, PORT))
# master_socket.listen(1)
#
# # creates a storage area for our connections
# sockets = []
# sockets.append(master_socket)
#
# while True:
#     (readable, writable, exceptional) = select.select(sockets, sockets, sockets)
#
#     for s in readable:
#         is s is master_socket:
#         (client, _) = master_socket.accept()
#         client.setblocking(0)
#         sockets.append(client)
#
#     else:
#         data = s.recv(1024)
#         if not data:
#             s.shutdown(socket.SHUT_RDWR)
#             s.close()
#             sockets.remove(s)
#         print("Recieved", repr(data))
#         elif s in writable:
#         s.sendall(data)
#
#








# #server side, working blank, one connection
#
# import socket
#
# HOST = "192.168.1.117"
# PORT = 30001
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(1)
#
# conn, addr = server_socket.accept()
# print ("connection from:", addr)
#
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     print ('Received', bytes(data))
#     conn.sendall(data)
# conn.shutdown(socket.SHUT_RDWR)
# conn.close
# server_socket.close()
