from tkinter import *
import socket,threading

def acceptMessage(s,text,theSystem):
    sock,addr = s.accept()
    theSystem.sock = sock
    while True:
        text.insert(END,'[Ohter"s Message]:' + (sock.recv(1024)).decode()+'\n')

class Chat:

    def processSendButton(self):
        self.sock.send(self.Message.get().encode())
        self.text.insert(END,'[Your Message] :' + self.Message.get() + '\n')

    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12342
        self.s.bind((host,port))
        self.s.listen(1)
        window = Tk()
        window.text = Text(window)

        self.text = Text(window)
        self.text.pack()

        frame1 = Frame(window)
        frame1.pack()

        label = Label(frame1,text='Enter your Message:')
        self.Message = StringVar()
        entryMessage = Entry(frame1,textvariable=self.Message)

        btSend = Button(frame1,text='Send',command=self.processSendButton)

        label.grid(row=2,column=10)
        entryMessage.grid(row=1,column=15)
        btSend.grid(row=1,column=20)
        self.text.insert(END, "\t\t\t\t----------------\n\t\t\t\tWecolme to Chat \n\t\t\t\tEnjoy youself \n\t\t\t\t----------------\n\n\n")      
        self.text.insert(END,'[NO PERSON] Wait for another one \n')

        t = threading.Thread(target=acceptMessage,args=(self.s,self.text,self))
        t.start()

        window.mainloop()
Chat()