import socket
import ssl
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
mail_server = 'pop.gmail.com'
port = 995
# mail_server = 'imap.gmail.com'
# port = 993

s.connect((mail_server,port))
result = s.recv(2048)
result = result.decode()
print ("connection result: "+result)


username = "aizaztesting@gmail.com"
password = "StrongPassword12"

# login = "a login "+username+' '+password+'\r\n'
# s.send(login.encode())
# r = s.recv(4096)
# r = r.decode()
# print(r)
#
# fetch = "a fetch 1 all\r\n"
# s.send(fetch.encode())
# r = s.recv(4096)
# r = r.decode()
# print(r)
#
# logout = "a logout\r\n"
# s.send(logout.encode())
# r = s.recv(4096)
# r = r.decode()
# print(r)
user_msg = "USER "+username+"\r\n"
s.send(user_msg.encode())
r = s.recv(4096)
print(r.decode())
pass_msg = "PASS "+password+"\r\n"
s.send(pass_msg.encode())
r = s.recv()
print(r.decode())
#
list = "LIST\r\n"
s.send(list.encode())
r = s.recv(4096)
print(r.decode())

#msg_number = input("Input message Number: ")
#msg = "RETR "+msg_number+"\r\n"
msg = "RETR "+'1'+"\r\n"
s.send(msg.encode())

still_reciving = True
email = ''


while True:
	r = s.recv(4096)
	chunk = r.decode()
	if r == ' ' or chunk[0] == '.' :
		break
	email = email+chunk

print(email)


quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
