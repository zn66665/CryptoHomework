from . import Common
from net_module import NetCommunication,ServerObject
from PyQt5.QtWidgets import QFileDialog
import threading
class ClientLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
        self.current_server = None #当前的客户端连接对象
        self.server_objects={} #保存一个从名字到客户端对象的映射

    #连接远程服务器
    def connect_server_click(self):
        server_address=self.view.ServerAddress_Input.text()
        server_port=self.view.ServerPort_Input.text()
        if not server_address or not server_port:
            self.show_error_message("Invalid remote address or port!!")
            return
        #调用socket_connect()函数连接remote,返回remote_socket对象
        server_socket=NetCommunication.NetCommunication.server_socket_connect(server_address,server_port)
        if server_socket is not None:
            peer_name = self.generate_connection_name(server_socket)
            server_object = ServerObject.ServerObject(server_socket,peer_name,server_address)
            self.new_item(peer_name)
            self.server_objects[peer_name] = server_object
            self.current_server_ = server_object
            server_handler = threading.Thread(target=self.handle_server_connection, args=(server_object,))
            server_handler.start()
        else:
        # 处理连接失败的情况
            self.show_error_message("connect remote fail,please try again!!")
    #处理与remote端的连接
    def handle_server_connection(self,server_object):
        try:
            while True:
                # 接收服务器消息
                data = server_object.socket.recv(1024)
                if not data:
                    break  # 服务端关闭连接

                # 处理接收到的数据，这里简单地将其回送给客户端
                self.output_communication_message(f"收到来自 server 的消息: {data.decode()}")
                
                # 发送回复消息给客户端
                reply_message = f"客户端已收到消息: {data.decode()}"
                server_object.socket.send(reply_message.encode())

        except Exception as e:
            self.output_communication_message(f"与server 通信时发生错误: {e}")

        finally:
            # 关闭客户端 socket
            server_object.socket.close()
    #断开连接
    def stop_connect_click(self):
        pass
    #发送密文给服务器
    def send_to_server_click(self):
        pass
    #客户端选择要将消息保存的文件路径
    def cient_select_saved_file_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)
        self.view.FilePath_Input_3.setText(file_name)
     #客户端随机生成p,g,a参数
    def client_random_generate(self):
        p=self.generate_large_prime()
        g=self.choose_generator(p)
        a=self.generate_private_key(p)
        self.view.ClientP_Inputline.setText(str(p))
        self.view.ClientG_Inputline.setText(str(g))
        self.view.ClientA_Inputline.setText(str(a))
    #客户端通过p,g,a参数计算出公钥
    def client_generate_pubKey(self):
           # 确保 p, g, 和 a 已经被定义
        p = int(self.view.ClientP_Inputline.text())
        g = int(self.view.ClientG_Inputline.text())
        a = int(self.view.ClientA_Inputline.text())

        # 计算公钥 A = g^a mod p
        A = pow(g, a, p)

        # 设置公钥显示
        self.view.cClientPubKey_Input.setPlainText(str(A))
    #发送p,g参数到服务器
    def sendPG2Server(self):
        pass
    #客户端发送自己的公钥
    def client_send_PubKey(self):
        pass
    #客户端通过服务端的公钥以及其他参数计算出key
    def client_generate_key(self):
        pass
    def new_item(self,itemName):
        self.view.ServerObject_ComBox.addItem(itemName)
    #改变combobox
    def on_combobox_changed(self, index):
        # 当选项改变时调用的函数,更改当前的通信对象
        selected_text = self.view.ServerObject_ComBox.itemText(index)
        self.currrnt_server =  self.server_objects[selected_text]

    #将一个新的消息输出到
    def output_communication_message(self, message):
        # 将新消息添加到 ClientMessageBox，并自动换行
        self.view.ClientMessageBox.appendPlainText(message)
        pass