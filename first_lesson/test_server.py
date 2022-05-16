import socket
from urls import routes


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8002)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    print('Сервер готов к работе...')
    client_connection, client_address = server_socket.accept()
    routes.get()
    print(f'Запрос от:{client_address}')
    data = client_connection.recv(1024).decode()
    print(data)
    client_connection.close()
