import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDRESS =  '127.0.0.1'
PORT = 5500
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title('MUSIC WINDOW')
    window.geometry('500x500')
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window,text="SELECT SONG",bg="LightSkyBlue",font=('Calibri',10))
    selectLabel.place(x=5,y=10)

    listBox = Listbox(window,height=10,width=40,activestyle="dotbox", bg="LightSkyBlue", font=('Calibri',10))
    listBox.place(x=100,y=10)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command= listBox.yview)

    playButton = Button(window,text="Play",width=10,bg="yellow",bd=1,font=('Helvetica',10))
    playButton.place(x=30,y=200)

    Stop = Button(window,text="Stop",bd=1,width=10,bg='yellow',font=('Helvetica',10))
    Stop.place(x=200,y=200)

    upload = Button(window,text="Upload",bd=1,width=10,bg='cyan',font=('Helvetica',10),fg="white")
    upload.place(x=30,y=250)

    download = Button(window,text="Download",width=10,bd=1,bg="cyan",font=('Calibri',10))
    download.place(x=200,y=250)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global SERVER

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()