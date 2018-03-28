import socket
import time
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mail_server = 'smtp.gmail.com'
port = 587

#print(host)
#request = "GET / HTTP/1.1\nHost: "+host_ip+"\n\n"

s.connect((mail_server,port))
#s.send(request.encode())
result = s.recv(2048)
result = result.decode()
if result[:3] != '220':
    print("220 reply not recived")
else:
    print ("connection result: "+result)
ehlo = 'EHLO Alice\r\n'
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


From = "MAIL FROM: <testingISFUN@yubelikethis.ca>\r\n"
s.send(From.encode())
r3 = s.recv(2048)
r3 = r3.decode()
print("from response:"+r3)

to = "RCPT TO: <aizaz_iqbal@hotmail.com>\r\n"
s.send(to.encode())
r4 = s.recv(2048)
r4 = r4.decode()
print("To response: "+r4)

data = "DATA\r\n"
s.send(data.encode())
r5 = s.recv(2048)
r5 = r5.decode()
print("Data response: "+r5)

subject = "Subject: TEST\r\n\r\n"
s.send(subject.encode())
r6 = s.recv(2048)
r6 = r6.decode()
print("subject response: "+r6)

quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
