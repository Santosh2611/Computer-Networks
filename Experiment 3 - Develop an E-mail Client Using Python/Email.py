import smtplib # Defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

"""
The email package provides some convenient encoders in its encoders module. 
These encoders are actually used by the MIMEAudio and MIMEImage class constructors to provide default encodings.
"""
from email import encoders 

from email.mime.text import MIMEText # A subclass of MIMENonMultipart, the MIMEText class is used to create MIME objects of major type text.
from email.mime.base import MIMEBase # This is the base class for all the MIME-specific subclasses of Message. 
from email.mime.multipart import MIMEMultipart # A subclass of MIMEBase, this is an intermediate base class for MIME messages that are multipart.

server = smtplib.SMTP('smtp.gmail.com', 587) # Forms an email client with SMTP listener module
# server.connect("smtp.gmail.com", 587)
# server.ehlo()
# with open('password.txt' , 'r') as f:

server.starttls()
server.login('group9cn@gmail.com', 'fbyj klbk yfsf zapk') # Log in with mail credentials
msg = MIMEMultipart() # Secure Multipurpose Internet Mail Extensions (S/MIME) is used to send attachments

msg['From'] = 'Santosh' # Sender Name
msg['To'] = 'group9cn@gmail.com' # Receiver Email Address
msg['Subject'] = 'Test File - Experiment 3' # Subject of the Mail

# with open('attachment.txt', 'r') as f:
# message = f.read()
message  = 'Hi! This is Santosh (53) here. I have sent an email sent from Python.'   
msg.attach(MIMEText(message , 'plain')) # Text Message Attachment

filename = 'Email.py' # File Name of Attachment
attachment = open(filename, 'rb') # Opens a file, and returns it as a file object
p = MIMEBase('application', 'octet-stream') # File Attachment
p.set_payload(attachment.read())

encoders.encode_base64(p) # Encodes the payload into base64 form and sets the Content-Transfer-Encoding header to base64. 
p.add_header('content-Disposition', f'attachment; filename = {filename}') # Header name is the same as file name
msg.attach(p)

text = msg.as_string() # Allows str(msg) to produce a string containing the serialized message in a readable format.
server.sendmail('group9cn@gmail.com' , 'group9cn@gmail.com', text) # Send mail, from sender to receiver with text message
print("\nThe mail along with the attachment(s) has been sent to your inbox.\n")
