from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
s.bind(('', 8080))  # '' равно localhost, указывает на самого себя
s.listen(6)  # цифра означает, сколько подключений удерживает одновременно сетевая карта
client, addr = s.accept()  # забрать следующего из очереди
req = client.recv(0x10000)
print(req.decode())
resp = (''
        'HTTP/1.0 200 OK\r\n'
        'Content-Type: image/gif\r\n'  # смотри MIME TYPE
        '\r\n'
        )
client.send(resp.encode())
with open('tenor.gif', 'rb') as file:
    client.send(file.read())
client.shutdown(SHUT_WR)
client.close()
