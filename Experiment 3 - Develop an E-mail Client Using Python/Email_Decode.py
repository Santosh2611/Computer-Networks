import imaplib # This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which encapsulate a connection to an IMAP4 server and implement a large subset of the IMAP4rev1 client protocol as defined in RFC 2060. 

import email # Library for managing email messages 
imap_server = 'imap.gmail.com' # IMAP server with the IMAP listener module
email_address = 'group9cn@gmail.com'
password = 'fbyj klbk yfsf zapk'

imap = imaplib.IMAP4_SSL(imap_server) # This is a subclass derived from IMAP4 that connects over an SSL encrypted socket 
imap.login(email_address, password) # Log in with mail credentials
imap.select("Inbox") # Item selection for decoding
_, msgnum = imap.search(None, "ALL") # Return the count of mails in 'Inbox'
print("\nCount of Mails in Inbox: " + str(msgnum) + "\n")

# Print Decoded Details:-
for msgnum in msgnum[0].split(): # Splits a string into a list
    _, data = imap.fetch(msgnum, ("RFC822")) # Fetch (parts of) messages
    
    message = email.message_from_bytes(data[0][1]) # Return a message object structure from a bytes-like object.
    print(f"Message Index Number: {msgnum}")
    print(f"From : {message.get('From')}")
    print(f"To : {message.get('To')}")

    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")     
    print("Content: ")

    # The walk() method is an all-purpose generator which can be used to iterate over all the parts and subparts of a message object tree, in depth-first traversal order.
    for part in message.walk():
        if part.get_content_type() == "text/plain": # Return the message’s content type, coerced to lower case of the form maintype/subtype. 
            print(part.as_string()) # Allows str(msg) to produce a string containing the serialized message in a readable format.
    
    print("\n")
