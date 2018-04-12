import socket
import base64
import ssl
import tkinter as tk



username = ' '
password = ' '
i = 1
#This class is used for the compose mail window
class compose_mail_frame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(height=600,width=600)
        self.pack()
        self.create_compose()

    def create_compose(self):

        tk.Label(mail_root,text="To: ").place(x=25,y=50)
        mail_root.to_input = tk.Entry(mail_root,width=50)
        mail_root.to_input.place(x=75,y=50)
        tk.Label(self,text="Subject: ").place(x=25,y=100)
        mail_root.subject_input = tk.Entry(mail_root,width=50)
        mail_root.subject_input.place(x=75,y=100)
        tk.Label(self,text="Body: ").place(x=25,y=150)
        mail_root.body_input = tk.Text(self,width=60, height=23)
        mail_root.body_input.place(x=75,y=150)
        tk.Button(mail_root,text="Send",command=self.send).place(x=400,y=525)
        tk.Button(mail_root,text="Cancel",command=root.destroy).place(x=450,y=525)

#This class is used for creating the main window of the app
class Application(tk.Frame):
    def __init__(self,master=None):
        self.user = ' '
        self.password = ' '
        self.i = 1
        super().__init__(height=600,width=600)
        self.pack()
        self.create_login()
#This creates all the widgets for the main loging window
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
#This is for creating all teh widgets in the compose window
    def compose_new_mail(self):
        new = tk.Toplevel(self)
        new.minsize(width=600,height=600)
        tk.Label(new,text="To: ").place(x=25,y=50)
        self.to_input = tk.Entry(new,width=50)
        self.to_input.place(x=75,y=50)
        tk.Label(new,text="Subject: ").place(x=25,y=100)
        self.subject_input = tk.Entry(new,width=50)
        self.subject_input.place(x=75,y=100)

        tk.Label(new,text="Body: ").place(x=25,y=150)
        self.body_input = tk.Text(new,width=60, height=23)
        self.body_input.place(x=75,y=150)

        tk.Button(new,text="Send",command=self.send).place(x=400,y=525)


#This function takes the input from the compose window and the username and password
#entered above then forms an connection with gmail smtp server to send mail
    def send(self):
        self.to = self.to_input.get()
        self.subject = self.subject_input.get()
        self.body = self.body_input.get("1.0",'end')

        #Making the TCP socket
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mail_server = 'smtp.gmail.com'
        port = 587
        #Connecting to google servers
        s2.connect((mail_server,port))
        r = s2.recv(2048)
        r = r.decode()
        print ("connection result: "+r)
        ehlo = 'EHLO smtp.gmail.com\r\n'
        s2.send(ehlo.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("ehlo reply: "+r)
        #swapping to TLS connection
        tls = "STARTTLS \r\n"
        s2.send(tls.encode())
        tlsr = s2.recv(2048)
        tlsr = tlsr.decode()
        print(tlsr)

        s2 = ssl.wrap_socket(s2,ssl_version=ssl.PROTOCOL_TLS)
        #Authenticating google account

        b64_auth = ("\x00"+username+"\x00"+password).encode()
        b64_auth = base64.b64encode(b64_auth)
        auth = "AUTH PLAIN ".encode()+b64_auth+"\r\n".encode()
        s2.send(auth)
        recv_auth = s2.recv(2048)
        print("AUTH response: "+recv_auth.decode())
#Begining of the mail transaction
        From = "MAIL FROM: <testingISFUN@yubelikethis.ca>\r\n"
        s2.send(From.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("from response:"+r)
        #Setting who the rcpt is
        to = "RCPT TO: <"+self.to+">\r\n"
        s2.send(to.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("To response: "+r)
        #Marks begining of data section of email
        data = "DATA\r\n"
        s2.send(data.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("Data response: "+r)
        #Subject is sent as part of the data
        subject = "Subject:"+self.subject+"\r\n"
        s2.send(subject.encode())
        #The data of the email is sent
        data = self.body+"\r\n"
        s2.send(data.encode())
        #This is the required marker to end the email which is then sent
        end_body = "\r\n"+'.'+"\r\n"
        s2.send(end_body.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("Data response: "+r)
        #This ends the connection with the smtp server
        quit = "QUIT\r\n"
        s2.send(quit.encode())
        r = s2.recv(2048)
        r = r.decode()
        print("QUIT response: "+r)
        s2.close()
        new.destroy()
#This function is for retriving mail via pop3 from the gmail pop3 server for a given account
    def get_mail(self):
        pop_mail_server = 'pop.gmail.com'
        pop_port = 995
        #Here a secure socket is created which is required for further communication with pop.gmail.com
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLS)
        s.connect((pop_mail_server,pop_port))
        result = s.recv(2048)
        result = result.decode()
        print ("connection result: "+result)
        #This the the pop3 authentication messages for Username and Password
        user_msg = "USER "+username+"\r\n"
        s.send(user_msg.encode())
        r = s.recv(4096)
        print(r.decode())
        pass_msg = "PASS "+password+"\r\n"
        s.send(pass_msg.encode())
        r = s.recv()
        print(r.decode())
        #This is the command to retreve the email at index i
        msg = "RETR "+str(self.i)+"\r\n"
        s.send(msg.encode())
        email = ''
        self.i += 1
        actual_message = False
        #This loop is to recive all the email data as it does not come in 1 packet
        while True:
            r = s.recv(4096)
            chunk = r.decode()
            email = email+chunk
            #This is to see if an error has occurred but as gmail has having issues sending the data it is disabled
            # if "Error: " in chunk:
            #     self.email_display.insert('end','An Error has occurred ')
            #     self.email_display.insert('end',chunk)
            #     print(chunk)
            #     break
            #This is to find the chunk of data that contains the actual message and not the other overhead
            if "Date: " in chunk:
                actual_message = True
            if actual_message:
                self.email_display.insert("end", chunk)
            #Here the end of an smtp message is watched for to know when the email is fully recived
            if chunk[1] == '.' or chunk[0] == '.' or chunk[-1] == '\n' :
                break
        #This was an alternate method of splittiing the excess data from the message
        # try:
        #     not_important,important_parts = email.split("Date:")
        #     self.email_display.insert("end", important_parts)
        # except:
        #     pass

    #login is to check if the user can actually use the account information entered
    def login(self):
        self.user = self.user_entry.get()
        self.password = self.pass_entry.get()
        username = self.user
        password = self.password
        #A connection to the smtp server is made to check the auth info
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
        #535 is the code for invalid username or password snd generates an error message
        if code == '535':
            self.bad_login = tk.Label(self,text="Username or password incorrect")
            self.bad_login.grid(row=3)
            self.pack()
            #235 is the code if the auth is successful and the program creates the rest of the frame
        elif code == '235':

            self.inbox_label = tk.Label(self,text="Inbox")
            self.inbox_label.grid(row=4)
            self.email_display = tk.Text(self )
            self.email_display.grid(row=5)
            self.scrollbar = tk.Scrollbar(self,command=self.email_display.yview)
            self.scrollbar.grid(row=5,column=1,sticky="nsew")
            self.next_email = tk.Button(self, text="Next Email", command=self.get_mail)
            self.next_email.grid(row=6)
            self.compose_button = tk.Button(self, text="compose", command = self.compose_new_mail)
            self.compose_button.grid(row=6,column=2)
            self.pack()
            print("QUIT response: "+r)
        #This is if some other error has occurred
        else:
            self.unknown_error = tk.Label(self,text="An error has occurred " + code)
            self.unknown_error.grid(row=3)
            self.pack()



#These lines are to start the initial program
root = tk.Tk()
app = Application(master=root)
app.master.title('Mail Client')
app.mainloop()
