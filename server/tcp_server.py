import socket

# параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_serv_sock = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

print(tcp_serv_sock.fileno())

tcp_serv_sock.bind(('localhost', 53210))
tcp_serv_sock.listen(3)

while True:
    print("waiting connection")
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = tcp_serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)  # recv - получает сообщение TCP
        print("data: ", data, "\t", type(data))
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(bytes("answer", 'utf-8'))

    client_sock.close()
