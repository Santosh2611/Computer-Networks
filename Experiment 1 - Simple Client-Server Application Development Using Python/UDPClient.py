import socket # Low-level networking interface

if __name__ == "__main__":

    localIP = "127.0.0.1" # IP address of the local host
    localPort = 20001 # Port Number
    serverAddressPort = (localIP, localPort)
    bufferSize = 1024 # Byte Size

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Create a UDP datagram socket at the client side, belonging to IPv4 family and following connection-less UDP protocol

    while(True):
        data = input("\nEnter data: ")
        data = data.encode("UTF-8") # Encode the string
        UDPClientSocket.sendto(data, serverAddressPort) # Sending a reply to server

        data, address = UDPClientSocket.recvfrom(bufferSize) # Receive the address to send the data back
        data = data.decode("UTF-8") # Decode the bytes
        print(f"Server: {data}")
