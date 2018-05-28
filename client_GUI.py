from tkinter import *
import socket,threading
# 进入消息循环

def acceptMessage(sock,text):
    while True:
        text.insert(END,"[Other's Message] :" + (sock.recv(1024)).decode() + '\n')

class Chat:

    def processSendButton(self):
        self.s.send((self.Message.get().encode()))
        self.text.insert(END,'[You Message]:' + self.Message.get() + '\n')


    def processLinkButton(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建 socket 对象
        host = socket.gethostname() #获取本地主机名
        port= 12342
        self.s.connect((host,port))
        self.text.insert(END,'Linked\n')
        t = threading.Thread(target=acceptMessage,args=(self.s,self.text))
        t.start()

    def __init__(self):
        window = Tk()
        #设置标题
        window.title('Chat')
        #创建文本输入框
        self.text =Text(window)
        self.text.pack()
        #设置框架
        frame1 = Frame(window)
        frame1.pack()
        #创建label
        label = Label(frame1,text='Enter your Message:')
        # label.pack()

        self.Message = StringVar()
        entryMessage = Entry(frame1,textvariable=self.Message)
        btSend = Button(frame1,text='Send',command=self.processSendButton)#只有第一个属性设置frame才能 grid 否则 pack
        btLink = Button(frame1,text='Link',command=self.processLinkButton)
        # btLink.pack() #button只能pack()

        #设置元素位置
        label.grid(row=1,column=5)
        entryMessage.grid(row=1,column=7)
        btSend.grid(row=1,column=15)
        btLink.grid(row=2,column=7)
        self.text.insert(END,"\t\t\t\t----------------\n\t\t\t\tWecolme to Chat \n\t\t\t\tEnjoy youself \n\t\t\t\t----------------\n\n\n")
        self.text.tag_config('star',background='yellow')


        window.mainloop()

Chat()