import socket
import ssl
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
mail_server = 'pop.gmail.com'
port = 995

s.connect((mail_server,port))
result = s.recv(2048)
result = result.decode()
print ("connection result: "+result)


username = "aizaztesting@gmail.com"
password = "StrongPassword12"

user_msg = "USER "+username+"\r\n"
s.send(user_msg.encode())
r = s.recv(4096)
print(r.decode())
pass_msg = "PASS "+password+"\r\n"
s.send(pass_msg.encode())
r = s.recv()
print(r.decode())

list = "LIST\r\n"
s.send(list.encode())
r = s.recv(4096)
print(r.decode())

msg_number = input("Input message Number: ")
msg = "RETR "+msg_number+"\r\n"
s.send(msg.encode())
r = s.recv(4096)
print(r.decode())

reset = "RSET\r\n"
s.send(reset.encode())
r = s.recv(4096)
print(r.decode())

quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
