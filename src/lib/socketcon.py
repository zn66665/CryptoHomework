import asyncio
import socket
##通过remote的地址和port，建立socket连接，并返回该对象
def remote_socket_connect(address, port):
    # 创建一个 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 尝试连接到指定的地址和端口
        client_socket.connect((address, port))
        print(f"成功连接到 {address}:{port}")

        # 返回连接成功的 socket 对象
        return client_socket

    except Exception as e:
        # 连接失败时处理异常
        print(f"连接失败: {e}")

        # 关闭 socket 连接
        client_socket.close()

        # 返回 None 表示连接失败
        return None

##建立绑定到本机地址和特定端口号的socket，并开始监听，异步函数，不阻塞主线程运行
def bind_listen_sokcet(local_socket,host,port):
    local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        local_socket.bind((host, port))
        print(f"服务端已绑定到 {host}:{port}")
    except Exception as e:
        print(f"服务端出现错误: {e}")

    finally:
        # 关闭服务端 socket
        local_socket.close()
    pass