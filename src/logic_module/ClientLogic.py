from . import Common,NetCommunication
import threading
class ClientLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
        self.server_socket = None

    #连接远程服务器
    def connect_server_click(self):
        server_address=self.view.ServerAddress_Input.text()
        server_port=self.view.ServerPort_Input.text()
        if not server_address or not server_port:
            self.show_error_message("Invalid remote address or port!!")
            return
        #调用socket_connect()函数连接remote,返回remote_socket对象
        self.server_socket=NetCommunication.NetCommunicationLogic.server_socket_connect(server_address,server_port)
        if self.server_socket:
            server_handler = threading.Thread(target=self.handle_server_connection, args=(self.server_socket,))
            server_handler.start()
        else:
        # 处理连接失败的情况
            self.show_error_message("connect remote fail,please try again!!")
    #处理与remote端的连接
    def handle_server_connection(self,server_socket):
        try:
            while True:
                # 接收服务器消息
                data = server_socket.recv(1024)
                if not data:
                    break  # 服务端关闭连接

                # 处理接收到的数据，这里简单地将其回送给客户端
                print(f"收到来自 server 的消息: {data.decode()}")
                
                # 发送回复消息给客户端
                reply_message = f"客户端已收到消息: {data.decode()}"
                server_socket.send(reply_message.encode())

        except Exception as e:
            print(f"与server 通信时发生错误: {e}")

        finally:
            # 关闭客户端 socket
            server_socket.close()