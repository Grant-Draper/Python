#working code from mike, client side, cert created by me, see CertCreation.txt


#!/usr/bin/env python3.5
import socket, ssl

if __name__ == "__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
  ssl_sock.connect(("localhost", 7075))
  ssl_sock.write("fuck".encode("UTF-8"))
  stuff = ssl_sock.read()
  print(stuff.decode("UTF-8"))
  ssl_sock.close()






















#client side, with exception handling
#
# import socket
# import sys
# import time
#
# #Connection 1
# #these are the creds of the target machine and port
# HOST = "127.0.0.1"
# PORT = 30001
#
# #this creates variable called s
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.connect((HOST, PORT))
# except:
#     print("Fail")
#     sys.exit()
#
# print("about to send")
#
#
# #not working while loop to increment a value and send the value to
# #the server whist waiting for 1 second
# while True:
#     time.sleep(1)
#     counter = 1
#     if counter < (counter + 1) :
#        s.sendall(bytes(counter, "utf8"))

#
# time.sleep(1)
# s.sendall(bytes("Grant says hi", "utf8"))
# print("sent")
# data = s.recv(1024)
# print ('Received', repr(data))
#
# s.shutdown(socket.SHUT_RDWR)
# s.close()
#



#Connection 2
#
# import socket, sys
#
# #these are the creds of the target machine and port
# HOST = "127.0.0.1"
# PORT = 30001
#
# #this creates variable called s
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.connect((HOST, PORT))
# except:
#     print("Fail")
#     sys.exit()
#
#
# s.sendall(bytes("Dave says hi", "utf8"))
#
# data = s.recv(1024)
# print ('Received', repr(data))
#
# s.shutdown(socket.SHUT_RDWR)
# s.close()

























##client, working
#
# import socket
#
# HOST = "127.0.0.1"
# PORT = 30001
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
# s.connect((HOST, PORT))
# s.sendall(bytes("Grant says hi again again", "utf8"))
#
# while True:
#     data = s.recv(1024)
#     print ('Received', repr(data))
#
# s.shutdown(socket.SHUT_RDWR)
# s.close()





