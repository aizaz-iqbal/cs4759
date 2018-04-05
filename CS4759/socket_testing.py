import socket
import time
import sys
import base64
import ssl

#GUI class for taking email inputs
class Application(tk.Frame):
    def __init__(self, master=None):
        self.to = ' '
        self.subject = ' '
        self.body = ' '
        super().__init__(height=600,width=600)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        tk.Label(self,text="To: ").place(x=25,y=50)
        self.to_input = tk.Entry(self,width=50)
        self.to_input.place(x=75,y=50)

        tk.Label(self,text="Subject: ").place(x=25,y=100)
        self.subject_input = tk.Entry(self,width=50)
        self.subject_input.place(x=75,y=100)

        tk.Label(self,text="Body: ").place(x=25,y=150)
        self.body_input = tk.Text(self,width=60, height=23)
        self.body_input.place(x=75,y=150)

        tk.Button(self,text="Send",command=self.send).place(x=400,y=525)

        tk.Button(self,text="Cancel",command=root.destroy).place(x=450,y=525)

       # self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
       # self.quit.pack(side="bottom")


    def send(self):
        self.to = self.to_input.get()
        self.subject = self.subject_input.get()
        self.body = self.body_input.get("1.0",'end')

        From = "MAIL FROM: <testingISFUN@yubelikethis.ca>\r\n"
        s.send(From.encode())
        r = s.recv(2048)
        r = r.decode()
        print("from response:"+r)

        to = "RCPT TO: <"+self.to+">\r\n"
        s.send(to.encode())
        r = s.recv(2048)
        r = r.decode()
        print("To response: "+r)

        data = "DATA\r\n"
        s.send(data.encode())
        r = s.recv(2048)
        r = r.decode()
        print("Data response: "+r)

        subject = "Subject:"+self.subject+"\r\n"
        s.send(subject.encode())

        data = self.body+"\r\n"
        s.send(data.encode())

        end_body = "\r\n"+'.'+"\r\n"
        s.send(end_body.encode())
        r = s.recv(2048)
        r = r.decode()
        print("Data response: "+r)

        quit = "QUIT\r\n"
        s.send(quit.encode())
        r = s.recv(2048)
        r = r.decode()
        print("QUIT response: "+r)



#Making the TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mail_server = 'smtp.gmail.com'
port = 587
#Connecting to google servers
s.connect((mail_server,port))
r = s.recv(2048)
r = r.decode()
print ("connection result: "+r)
ehlo = 'EHLO smtp.gmail.com\r\n'
s.send(ehlo.encode())
r = s.recv(2048)
r = r.decode()
print("ehlo reply: "+r)
#swapping to TLS connection
tls = "STARTTLS \r\n"
s.send(tls.encode())
tlsr = s.recv(2048)
tlsr = tlsr.decode()
print(tlsr)

s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
#Authenticating google account
username = "aizaztesting@gmail.com"
password = "StrongPassword12"
b64_auth = ("\x00"+username+"\x00"+password).encode()
b64_auth = base64.b64encode(b64_auth)
auth = "AUTH PLAIN ".encode()+b64_auth+"\r\n".encode()
s.send(auth)
recv_auth = s.recv(2048)
print("AUTH response: "+recv_auth.decode())
#Creating GUI to send email
root = tk.Tk()
app = Application(master=root)
app.master.title('compose')
app.mainloop()
root.destroy()
