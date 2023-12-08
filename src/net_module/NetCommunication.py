from logic_module import Common
import socket

class NetCommunication(Common.Common):
##通过server的地址和port，建立socket连接，并返回该socket对象
    @classmethod
    def server_socket_connect(cls,address, port):
        # 创建一个 socket 对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # 尝试连接到指定的地址和端口
            server_socket.connect((address, int(port)))
            print(f"成功连接到 {address}:{port}")

            # 返回连接成功的 socket 对象
            return server_socket

        except Exception as e:
            # 连接失败时处理异常
            print(f"连接失败: {e}")

            # 关闭 socket 连接
            server_socket.close()

            # 返回 None 表示连接失败
            return None

    ##建立bind到主机地址和特定端口号的socket
    @classmethod
    def bind_listen_sokcet(cls,host,port):
        local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            local_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            local_socket.bind((host, int(port)))
            print(f"服务端已绑定到 {host}:{port}")
            return local_socket
        except Exception as e:
            print(f"服务端出现错误: {e}")
            return None