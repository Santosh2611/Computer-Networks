"""
import socket # Low-level networking interface

if __name__ == "__main__":

    localIP = "127.0.0.1" # IP address of the local host
    localPort = 20001 # Port Number
    bufferSize  = 1024 # Byte Size

    TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) # Create a UDP datagram socket at the client side, belonging to IPv4 family and following TCP protocol
    TCPServerSocket.connect((localIP,localPort)) # Connect to a remote socket address

    data = input("\nEnter data: ")
    TCPServerSocket.send(bytes(data, "UTF-8")) # Send data to the socket
    buffer = TCPServerSocket.recv(bufferSize) # Receive data from the socket

    buffer = buffer.decode("UTF-8")
    print(f"Server: {buffer}")
"""

import socket # Low-level networking interface

host_ip, server_port = "127.0.0.1", 9999 # IP Address of the local host and port number
bufferSize = 1024 # Byte Size
data = input("\nEnter data: ")
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a UDP datagram socket at the client side, belonging to IPv4 family and following TCP protocol

try: # Some Code...

    # Establish connection to TCP server and exchange data:-
    tcp_client.connect((host_ip, server_port)) # Connect to a remote socket address
    tcp_client.sendall(data.encode()) # Send data to the socket
    received = tcp_client.recv(bufferSize) # Receive data from the socket

finally: # Some Code... (ALWAYS EXECUTED)
    tcp_client.close() # Mark the socket closed

print ("Bytes Sent: {}".format(data))
print ("Bytes Received: {}\n".format(received.decode()))
