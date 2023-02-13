import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 5500
SERVER= None
clients= {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        print(client,addr)

def setup():
  global SERVER
  global IP_ADDRESS
  global PORT

  SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  SERVER.bind((IP_ADDRESS,PORT))

  SERVER.listen(100)

  print("\t\t\t SERVER IS WAITING FOR INCOMING REQUESTS.......")
  print('\n')

  acceptConnections()

server_thread = Thread(target=setup)
server_thread.start()