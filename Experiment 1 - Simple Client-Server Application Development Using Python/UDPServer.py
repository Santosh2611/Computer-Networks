import socket # Low-level networking interface

if __name__ == "__main__":

    localIP = "127.0.0.1" # IP address of the local host
    localPort = 20001 # Port Number
    bufferSize  = 1024 # Byte Size

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Create a datagram socket, belonging to IPv4 family and following connection-less UDP protocol
    UDPServerSocket.bind((localIP, localPort)) # Bind the socket with IP address and port number
    print("\nUDP Server Up & Listening...")

    # Listen for incoming datagrams:-
    while(True):
        data, address = UDPServerSocket.recvfrom(bufferSize) # Receive the address to send the data back
        data = data.decode("UTF-8")
        print(f"Client: {data}")
        
        data = data.upper()
        data = data.encode("UTF-8")
        UDPServerSocket.sendto(data, address) # Sending a reply to client
