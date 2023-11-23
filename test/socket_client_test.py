import socket

# 创建一个TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 服务器地址和端口
server_address = ('172.22.15.8', 12345)  # 替换为服务器的局域网IP

# 客户端连接服务器
client_socket.connect(server_address)

try:
    while True:
        # 发送消息给服务器
        message = input('发给服务器: ')
        client_socket.sendall(message.encode('utf-8'))

        # 接收服务器的响应
        data = client_socket.recv(1024)
        print('服务器说:', data.decode('utf-8'))

finally:
    # 清理连接
    client_socket.close()
