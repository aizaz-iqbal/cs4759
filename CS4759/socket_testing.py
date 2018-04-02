import socket
import time
import sys
import base64
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mail_server = 'smtp.gmail.com'
port = 587

s.connect((mail_server,port))
result = s.recv(2048)
result = result.decode()
if result[:3] != '220':
    print("220 reply not recived")
else:
    print ("connection result: "+result)
ehlo = 'EHLO smtp.gmail.com\r\n'
s.send(ehlo.encode())
r2 = s.recv(2048)
r2 = r2.decode()
if r2[:3] != '250':
    print('250 reply not recived')
else:
    print("ehlo reply: "+r2)

tls = "STARTTLS \r\n"
s.send(tls.encode())
tlsr = s.recv(2048)
tlsr = tlsr.decode()
print(tlsr)

s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)

username = "aizaztesting@gmail.com"
password = "StrongPassword12"
b64_auth = ("\x00"+username+"\x00"+password).encode()
b64_auth = base64.b64encode(b64_auth)
auth = "AUTH PLAIN ".encode()+b64_auth+"\r\n".encode()
s.send(auth)
recv_auth = s.recv(2048)
print("AUTH response: "+recv_auth.decode())


From = "MAIL FROM: <testingISFUN@yubelikethis.ca>\r\n"
s.send(From.encode())
r3 = s.recv(2048)
r3 = r3.decode()
print("from response:"+r3)

to_input = input("To: ")
to = "RCPT TO: <"+to_input+">\r\n"
s.send(to.encode())
r4 = s.recv(2048)
r4 = r4.decode()
print("To response: "+r4)

data = "DATA\r\n"
s.send(data.encode())
r5 = s.recv(2048)
r5 = r5.decode()
print("Data response: "+r5)

subject_input = input("Subject: ")
subject = "Subject:"+subject_input+"\r\n"
s.send(subject.encode())

body = input("Body: ")
data = body+"\r\n"
s.send(data.encode())
x = "\r\n"+'.'+"\r\n"
s.send(x.encode())
r5 = s.recv(2048)
r5 = r5.decode()
print("Data response: "+r5)

quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
