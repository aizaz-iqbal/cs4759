import socket
import ssl

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
#
list = "LIST\r\n"
s.send(list.encode())
r = s.recv(4096)
print(r.decode())


msg = "RETR "+'1'+"\r\n"
s.send(msg.encode())


email = ''


while True:
	r = s.recv(4096)
	chunk = r.decode()
	email = email+chunk

	if chunk[1] == '.' or chunk[0] == '.' or chunk[-1] == '\n' :
		break


date = email.split("Date:")[0]
FROM = email.split("From:")[0]
subject = email.split("Subject:")[0]
print(email)

# print(date)
# print('\n')
# print(FROM )
# print('\n')
# print(subject )

quit = "QUIT\r\n"
s.send(quit.encode())
r7 = s.recv(2048)
r7 = r7.decode()
print("QUIT response: "+r7)
s.close()
