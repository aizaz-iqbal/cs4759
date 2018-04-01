import socket
import ssl
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
mail_server = 'imap.gmail.com'
port = 993

s.connect((mail_server,port))
result = s.recv(2048)
result = result.decode()
print ("connection result: "+result)


username = "aizaztesting@gmail.com"
password = "StrongPassword12"
#b64_auth = ("\x00"+username+"\x00"+password).encode()
#b64_auth = base64.b64encode(b64_auth)
#auth = "LOGIN ".encode()+b64_auth+"\r\n".encode()
login = "a login aizaztesting@gmail.com StrongPassword12 \r\n"
s.send(login.encode())
recv_auth = s.recv(2048)
print("AUTH response: "+recv_auth.decode())

list = "a list"
s.send(list.encode())
r3 = s.recv()
r3 = r3.decode()
print("list response: "+r3)

quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
