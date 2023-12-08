from . import Common
from net_module import NetCommunication,ClientObiect
from net_module.EnumValue import ConnectionState,MessageType
from net_module.MessageObject import MessageObject
from Crypto.Util.number import long_to_bytes
from PyQt5.QtWidgets import QFileDialog
import json
import threading

class ServerLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
        self.local_socket = None #在本地监听的soket对象
        self.current_client = None #当前的客户端连接对象
        self.client_objects={} #保存一个从名字到客户端对象的映射
        self.stop_server=None
    #监听来自客户端的连接
    def listen_client_click(self):
         #输入的端口和地址可以为0,则默认监听0.0.0.0地址以及8080端口
        listen_address=self.view.ListenAddress_Input.text()
        listen_port=self.view.ListenPort_Input.text()
        if not listen_address:
            listen_address='0.0.0.0'
        if not listen_port:
            listen_port=8080
        #建立bind到指定网络接口的socket

        self.local_socket=NetCommunication.NetCommunication.bind_listen_sokcet(listen_address,listen_port)
        ##test
        self.output_communication_message(f"正在监听，绑定完成后的 socket 信息: {self.local_socket}")
        if self.local_socket is not None:
            #启动服务端线程，执行监听以及对消息的处理操作
            server_handler = threading.Thread(target=self.run_server, args=())
            server_handler.start()
        else:
            self.show_error_message("error,self local_socket is not correctly initialized!!")
    #服务器，启动！！
    def run_server(self):
        #最多接受五个客户端连接
        self.local_socket.listen(5)
        try:
            while True:
                # 接受客户端连接，完成对客户端对象的初始化,新建一个线程，用户对接受的消息进行处理，发送消息则直接通过
                #全局变量client_socket处理发送
                #在comBox中添加这个项
                if(self.stop_server == True):
                    print("stop listen!!")
                    break
                client_socket,client_addr = self.local_socket.accept()
                print(f"Accepted connection from {client_addr}")
                peer_name = self.generate_connection_name(client_socket)
                client_object = ClientObiect.ClientObject(client_socket,peer_name,client_addr,ConnectionState.CONNECTING)
                self.client_objects[peer_name] = client_object
                self.new_item(peer_name)
                self.current_client = client_object
                self.current_client.start_receive(self.handle_received_message)
        except Exception as e:
            print(f"Error accepting connection: {e}")
            pass
        finally:
            #在stop_listening中关闭socket
            self.local_socket.close()
            self.stop_server = False
            print("已经关闭所有连接！!")  
    #停止监听
    def stop_listen_click(self):
        #设置一个标志，用于通知 run_server 线程停止监听
        self.stop_server = True
        # 关闭所有客户端连接
        for client in self.client_objects.values():
            client.stop_receive()
        # 关闭服务器的主 socket
        # 清空 ComboBox 的所有项
        self.view.ClientObject_ComBox.clear()

        # 设置 current_client 为 None
        self.current_client = None
    #处理接受消息
    def handle_received_message(client_object, data):
        try:
            # 使用 MessageObject 类解析接收到的 JSON 数据
            message = MessageObject.from_json(data.decode('utf-8'))

            # 根据消息类型执行不同的操作
            if message.message_type == MessageType.CIPHER.value:
                # 将密文保存到文件
                with open("cipher.txt", "a") as file:
                    file.write(message.data + "\n")
                print(f"收到密文并保存: {message.data}")
            elif message.message_type == MessageType.PG.value:
                # 处理 P 和 G 参数
                print(f"收到 P 和 G 参数: P={message.p}, G={message.g}")
            elif message.message_type == MessageType.PUBKEY.value:
                # 处理公钥
                print(f"收到公钥: {message.pubKey}")

        except json.JSONDecodeError as e:
            print(f"JSON 解析错误: {e}")
        except Exception as e:
            print(f"处理消息时发生错误: {e}")
    #发送密文给当前客户端通信对象客户端
    def send_to_client_click(self):
        cipher = self.view.CipherText_Output.toPlainText()
        if not cipher:
            self.show_error_message("无效的密文输入！！")
            return
        if not self.current_client:
            self.show_error_message("未连接任何客户端！！")
        message_to_send = f"密文: {cipher}"
        self.current_client.sendMessage(message_to_send.encode('utf-8'))
        self.output_communication_message(f"向客户端{self.current_client.peer_name}发送cipherText!!")
    def save_client_object_setting_Button(self):
        if not self.current_client:
            self.show_error_message("未选择客户端对象")
            return
        self.current_client.p = self.view.ServerP_Input.text()
        self.current_client.g = self.view.ServerG_Input.text()
        self.current_client.a = self.view.ServerA_Input.text()
        self.current_client.cPubKey= self.view.sClientPubKey_Input.toPlainText()
        self.current_client.sPubKey= self.view.sServerPubKey_Input.toPlainText()
        self.current_client.key= self.view.ServerGeneratedKey_Output.toPlainText()
        self.output_communication_message(f"成功将参数保存到客户端对象{self.current_client.peer_name}")
    #server选择要将消息保存的文件路径
    def server_select_saved_file_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)
        self.view.FilePath_Input_4.setText(file_name)
    #服务端随机生成p,g,a参数
    def server_random_generate(self):
        p=self.generate_large_prime()
        g=self.choose_generator(p)
        a=self.generate_private_key(p)
        self.view.ServerP_Input.setText(str(p))
        self.view.ServerG_Input.setText(str(g))
        self.view.ServerA_Input.setText(str(a))
    #服务端通过p,g,a参数计算出公钥
    def server_generate_pubKey(self):
        # 确保 p, g, 和 a 已经被定义
        p = int(self.view.ServerP_Input.text())
        g = int(self.view.ServerG_Input.text())
        a = int(self.view.ServerA_Input.text())

        # 计算公钥 A = g^a mod p
        A = pow(g, a, p)

        # 设置公钥显示
        self.view.sServerPubKey_Input.setPlainText(str(A))
    #发送p,g参数到客户端
    def sendPG2Client(self):
        p = self.view.ServerP_Input.text()
        g = self.view.ServerG_Input.text()
        if not p or not g:
            self.show_error_message("Invalid P or G!!")
            return
        if not self.current_client:
            self.show_error_message("未连接任何服务器！！")
        message_to_send = f"向客户端{self.current_client.peer_name}发送P、G"
        self.current_client.sendMessage(message_to_send.encode('utf-8'))
        self.output_communication_message(f"向客户端{self.current_client.peer_name}发送P、G")
    #服务端发送自己的公钥
    def server_send_pubKey(self):
        pubKey = self.view.sServerPubKey_Input.toPlainText()
        if not pubKey:
            self.show_error_message("无效的公钥输入！！")
            return
        if not self.current_client:
            self.show_error_message("未连接任何服务器！！")
        message=f"向客户端{self.current_client.peer_name}发送pubKey:{pubKey}!!"
        self.current_client.sendMessage(message.encode('utf-8'))
        self.output_communication_message(f"向客户端{self.current_client.peer_name}发送pubKey:{pubKey}!!")
    #服务端通过服务端的公钥以及其他参数计算出key
    def server_generate_key(self):
        p = int(self.view.ServerP_Input.text())
        a = int(self.view.ServerA_Input.text())
        clientPubKey = int(self.view.sClientPubKey_Input.toPlainText())
        #作为客户端，据已有的p,g,a，客户端pubkey,服务端pubkey来计算最后的key
        print(f"p:{p},a:{a},clientpubkey{clientPubKey}")
        shared_key = pow(clientPubKey, a, p)
        self.view.ServerGeneratedKey_Output.setPlainText(str(shared_key))
    #为combox添加项和设置监听事件,即设置current_object为被选中的item所对应的Client_Object
    def new_item(self,itemName):
        self.view.ClientObject_ComBox.addItem(itemName)
    #改变combobox
    def on_combobox_changed(self, index):
        #combox选项数归零时不设置
        if self.view.ClientObject_ComBox.count()==0:
             self.current_client = None
             return
        # 当选项改变时调用的函数,更改当前的通信对象
        selected_text = self.view.ClientObject_ComBox.itemText(index)
        print(f"selected text is {selected_text}")
        self.current_client =  self.client_objects[selected_text]
     # 更新 UI 元素
    #将一个新的消息输出
    def output_communication_message(self, message):
        # 将新消息添加到 ClientMessageBox，并自动换行
        self.view.ServerMessageBox.appendPlainText(message)