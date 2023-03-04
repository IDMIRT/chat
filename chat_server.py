import socket
from os import path
from json import loads, load
from _thread import start_new_thread

users = dict()

HOST = '127.0.0.1'
PORT = 10500

# {host:{user:"name"}}
# 


if path.isfile('users.json'):
    with open('users.json', 'r',encoding='utf-8') as lfile:
        users = load(lfile)

def new_connect(connection, host):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        else:
            client_message = loads(data.decode())
            message = client_message['message']['text']
            user = client_message['message']['user']
            print(f'От пользователя {user} Получены данные {message}')
            connection.sendall(data)
    connection.close()



serv_chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_chat.bind((HOST, PORT))
serv_chat.listen(5)

while True:
    conn , host = serv_chat.accept()
    print(f'{host} подключился')
    start_new_thread(new_connect, (conn,host,))
   
    
