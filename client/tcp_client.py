import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))

while True:
    message = input("message: ")
    if -1 != message.find('/exit'):
        client_sock.close()
        break
    client_sock.sendall(bytes(message, 'utf-8'))

    data = client_sock.recv(1024)  # получаем ответ от сервера
    data = str(data)
    print("after data: ", data)
    if -1 != data.find('/exit'):
        print("serer disconnect")
        break
    # print(data)
# client_sock.close()
# print('Received', repr(data))
