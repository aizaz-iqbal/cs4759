import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        self.to = 'test to'
        self.sender = 'test from'
        self.body = 'test body'
        super().__init__(height=600,width=600)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self,text="To: ").place(x=25,y=50)
        self.to_input = tk.Entry(self,width=50)
        self.to_input.place(x=75,y=50)

        tk.Label(self,text="From: ").place(x=25,y=100)
        self.sender_input = tk.Entry(self,width=50)
        self.sender_input.place(x=75,y=100)

        tk.Label(self,text="Body: ").place(x=25,y=150)
        self.body_input = tk.Text(self,width=60, height=23)
        self.body_input.place(x=75,y=150)

        tk.Button(self,text="Send",command=self.send).place(x=400,y=525)

        tk.Button(self,text="Cancel",command=root.destroy).place(x=450,y=525)
 
       # self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
       # self.quit.pack(side="bottom")

    def send(self):
        self.to = self.to_input.get()
        self.sender = self.sender_input.get()
        self.body = self.body_input.get("1.0",'end')
        print(self.to)
        print(self.sender)
        print(self.body)

root = tk.Tk()
app = Application(master=root)
app.master.title('compose')
app.mainloop()




		
