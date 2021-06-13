import socket
import sys

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("failed to create a socket")
    print("Reason : %s" %str(err))
    sys.exit()
print("Socket Created")
target_host=input("Enter the target host to connect: ")
target_port=input("Enter the port: ")
try:
    sock.connect((target_host, int(target_port)))
    print("socket connect to host: %s and port is: %s" %(target_host,target_port))
    sock.shutdown(2)
except socket.error as err:
    print("failed to connect to %s on port %s" %(target_host,target_port))
    print("Reason: %s" %str(err))
    sys.exit()