from . import Common,NetCommunication
import threading

class ServerLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
        self.local_socket = None
        
    def listen_client_click(self):
         #输入的端口和地址可以为0,则默认监听0.0.0.0地址以及8080端口
        listen_address=self.view.ListenAddress_Input.text()
        listen_port=self.view.ListenPort_Input.text()
        if not listen_address:
            listen_address='0.0.0.0'
        if not listen_port:
            listen_port=8080
        #建立bind到指定网络接口的socket
        self.local_socket=NetCommunication.NetCommunicationLogic.bind_listen_sokcet(listen_address,listen_port)
        ##test
        print(f"绑定完成后的 socket 信息: {self.local_socket}")
        if self.local_socket is not None:
            #启动服务端线程，执行监听以及对消息的处理操作
            server_handler = threading.Thread(target=self.run_server, args=())
            server_handler.start()
        else:
            self.show_error_message("error,self local_socket is not correctly initialized!!")
            self.local_socket.close()
    #服务器，启动！！
    def run_server(self):
        #暂时只设置为只接受一个客户端连接，所以不需要循环等待
        self.local_socket.listen(1)
        try:
            # 接受客户端连接，完成对客户端socket的初始化,新建一个线程，用户对接受的消息进行处理，发送消息则直接通过
            #全局变量client_socket发送
            self.client_socket, self.client_addr = self.local_socket.accept()
            print(f"Accepted connection from {self.client_addr}")
            self.handle_client(self.client_socket,self.client_addr)
        except Exception as e:
            print(f"Error accepting connection: {e}")
            pass
        finally:
            #在stop_listening中关闭socket
            pass
        
    #处理与客户端的连接
    def handle_client(self,client_socket,client_address):
        try:
            print(f"正在与 {client_address} 连接")

            while True:
                # 接收客户端消息
                data = client_socket.recv(1024)
                if not data:
                    break  # 客户端关闭连接

                # 处理接收到的数据，这里简单地将其回送给客户端
                print(f"收到来自 {client_address} 的消息: {data.decode()}")
                
                # 发送回复消息给客户端
                reply_message = f"服务端已收到消息: {data.decode()}"
                client_socket.send(reply_message.encode())

        except Exception as e:
            print(f"与 {client_address} 通信时发生错误: {e}")

        finally:
            # 关闭客户端 socket
            client_socket.close()