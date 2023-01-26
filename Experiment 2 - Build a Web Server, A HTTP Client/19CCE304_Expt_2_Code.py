from http.server import HTTPServer, BaseHTTPRequestHandler
"""
http.server - Defines classes for implementing HTTP servers.
HTTPServer - This class builds on the TCPServer class by storing the server address as instance variables named server_name and server_port. 
BaseHTTPRequestHandler - This class is used to handle the HTTP requests that arrive at the server.
"""

import time # Provides various time-related functions

HOST = "192.168.109.13" # IP address of server
PORT = 5000 # Port Number

class requestHandler(BaseHTTPRequestHandler):
   
    # GET method is used to appends form data to the URL in name or value pair:-
    def do_GET(self):
        self.send_response(200) # Sends the response header only
        self.send_header("Content-type", "text/html") # Adds the HTTP header to an internal buffer which will be written to the output stream when either end_headers() or flush_headers() is invoked.
        self.end_headers() # Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer and calls flush_headers().
       
        self.wfile.write(bytes("<html><body><h1>HTTP_client_server</h1></body></html>", "utf-8")) # Contains the output strean for writing a response back to the client.
       
    # POST is a method that is supported by HTTP and depicts that a web server accepts the data included in the body of the message:-
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
       
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) # Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. 
        self.wfile.write(bytes('{"time": "'+ date +'"}', "utf-8"))
       
server = HTTPServer((HOST, PORT), requestHandler)
print("The Server is Running...")

server.serve_forever() # Handle requests until an explicit shutdown() request.
server.server_close() # Clean up the server. May be overridden.

# Client URL (cURL) is a computer software project providing a library and command-line tool for transferring data using various network protocols. 
