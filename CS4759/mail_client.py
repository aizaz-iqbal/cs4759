import socket
import base64
import ssl
import tkinter as tk
import tkinter.scrolledtext as tkst


username = ' '
pasword = ' '

class Application(tk.Frame):
    def __init__(self,master=None):
        self.user = ' '
        self.password = ' '
        super().__init__(height=600,width=600)
        self.pack()
        self.create_login()


    def create_login(self):
        self.login_label = tk.Label(self,text="LOGIN")
        self.login_label.grid(row=0)
        self.user_label = tk.Label(self,text="Username ")
        self.user_label.grid(row=1)
        self.pass_label = tk.Label(self,text="Password ")
        self.pass_label.grid(row=2)
        self.user_entry = tk.Entry(self)
        self.user_entry.grid(row=1,column=1)
        self.pass_entry = tk.Entry(self, show="*")
        self.pass_entry.grid(row=2,column=1)

        self.login_button = tk.Button(self,text = "Login", command=self.login)
        self.login_button.grid(row=3,column=2)
        self.pack()

    def login(self):
        self.user = self.user_entry.get()
        self.password = self.pass_entry.get()
        username = self.user
        password = self.password

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        s.connect((smtp_server,smtp_port))
        r = s.recv(2048)
        r = r.decode()
        ehlo = 'EHLO smtp.gmail.com\r\n'
        s.send(ehlo.encode())
        r = s.recv(2048)
        r = r.decode()
        print("ehlo reply: "+r)
        #swapping to TLS connection
        tls = "STARTTLS \r\n"
        s.send(tls.encode())
        r = s.recv(2048)
        r = r.decode()
        print(r)
        s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
        b64_auth = ("\x00"+self.user+"\x00"+self.password).encode()
        b64_auth = base64.b64encode(b64_auth)
        auth = "AUTH PLAIN ".encode()+b64_auth+"\r\n".encode()
        s.send(auth)
        recv_auth = s.recv(2048)
        recv_auth = recv_auth.decode()
        code = recv_auth[:3]
        if code == '535':
            self.bad_login = tk.Label(self,text="Username or password incorrect")
            self.bad_login.grid(row=3)
            self.pack()
            # mail_root = tk.Tk()
            # mail_app = current_mail(master=mail_root)
            # mail_app.master.title('Mail Client')
            # mail_app.mainloop()
            self.inbox_label = tk.Label(self,text="Inbox")
            self.inbox_label.grid(row=4)
            self.email_display = tk.Text(self )
            self.email_display.grid(row=5)
            self.scrollbar = tk.Scrollbar(self,command=self.email_display.yview)
            self.scrollbar.grid(row=5,column=1,sticky="nsew")
            self.pack()


        elif code == '235':
            # for widget in root.winfo_children():
            #     widget.destroy()
            quit = "QUIT\r\n"
            s.send(quit.encode())
            r = s.recv(2048)
            r = r.decode()

            print("QUIT response: "+r)

        else:
            self.unknown_error = tk.Label(self,text="An error has occurred " + code)
            self.unknown_error.grid(row=3)
            self.pack()

    def get_mail(self):
        pop_mail_server = 'pop.gmail.com'
        pop_port = 995
        s.connect((pop_mail_server,pop_port))
        result = s.recv(2048)
        result = result.decode()
        print ("connection result: "+result)

        user_msg = "USER "+username+"\r\n"
        s.send(user_msg.encode())
        r = s.recv(4096)
        print(r.decode())
        pass_msg = "PASS "+password+"\r\n"
        s.send(pass_msg.encode())
        r = s.recv()
        print(r.decode())

        i = 1
        email_arr = []


        while True:


        msg = "RETR "+i+"\r\n"
        s.send(msg.encode())

        email = ''
        if

        while True:
        	r = s.recv(4096)
        	chunk = r.decode()
        	email = email+chunk

        	if chunk[1] == '.' or chunk[0] == '.' or chunk[-1] == '\n' :
        		break

        try:
        	not_important,important_parts = email.split("Date:")
        	email_arr.append()
        except:
        	pass













root = tk.Tk()
app = Application(master=root)
app.master.title('Mail Client')
app.mainloop()
