"""
import socket # Low-level networking interface

if __name__ == "__main__":

    localIP = "127.0.0.1" # IP address of the local host
    localPort = 20001 # Port Number
    bufferSize  = 1024 # Byte Size

    TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) # Create a UDP datagram socket at the client side, belonging to IPv4 family and following TCP protocol
    TCPServerSocket.bind((localIP,localPort)) # Bind the socket to address
    TCPServerSocket.listen(5) # Enable a server to accept connections. 5 specifies the number of unaccepted connections that the system will allow before refusing new connections

    while(True):

        client, address = TCPServerSocket.accept() # Accept a connection
        print(f"Connection Established: {address[0]}:{address[1]}")
        data = client.recv(bufferSize) # Receive data from the socket

        data = data.decode("UTF-8")
        data = data.upper()
        client.send(bytes(data, "UTF-8"))
        
        client.close() # Mark the socket closed
"""

import socketserver # Simplifies the task of writing network servers
bufferSize = 1024 # Byte Size

# The TCP Server class for demonstration:-
class Handler_TCPServer(socketserver.BaseRequestHandler):

    # We need to implement the Handle method to exchange data with TCP client:-
    def handle(self):

        self.data = self.request.recv(bufferSize).strip() # TCP socket connected to the client for receiving data from the socket
        print("\n{} sent: ".format(self.client_address[0]) + str(self.data))
        self.request.sendall("Acknowledgment from TCP Server!\n".encode()) # Send back ACK for data arrival confirmation

if __name__ == "__main__":

    HOST, PORT = "127.0.0.1", 9999 # IP Address of the local host and port number
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer) # Initialize the TCP server object and bind it to the localhost on 9999 port
    tcp_server.serve_forever() # Activate the TCP server

    # To abort the TCP server, press Ctrl + C.
