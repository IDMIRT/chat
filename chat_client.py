import socket
from json import dumps, loads

# HOST = '192.168.3.125'
HOST = '127.0.0.1'
PORT = 10500


user_name = input('Введите имя пользователя: ')


conn_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn_client.connect((HOST,PORT))

while True:
    # conn_client.connect((HOST,PORT))
    data = input('Введите текст: ')
    data_to_send = dumps({'message':{'user':user_name,'text':data}})
    conn_client.sendall(data_to_send.encode())
    answer = conn_client.recv(1024)
    load_answer = loads(answer.decode())
    user = load_answer['message']['user']
    message = load_answer['message']['text']
    if user==user_name:
        print(f'Вы: {message}')
    else:
        print(f'{user}: {message}')
    
# conn_client.close()