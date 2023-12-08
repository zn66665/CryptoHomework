from . import Common
from net_module import NetCommunication,ServerObject
from net_module.EnumValue import ConnectionState,MessageType
from net_module.MessageObject import MessageObject
import json
from Crypto.Util.number import long_to_bytes
from PyQt5.QtWidgets import QFileDialog

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
            server_object = ServerObject.ServerObject(server_socket,peer_name,server_address,ConnectionState.CONNECTING)
            self.server_objects[peer_name] = server_object
            self.show_tip_message("成功连接到服务器！！")
            self.output_communication_message(f"成功连接到服务器,soket信息: {server_socket}")
            self.new_item(peer_name)
            server_object.start_receive(self.handle_received_message)
        else:
        # 处理连接失败的情况
            self.show_error_message("connect remote fail,please try again!!")
    '''
    #处理与remote端的连接
    def handle_server_connection(self,server_object):
        try:
            while True:
                # 接收服务器消息
                print("test")
                data = server_object.socket.recv(1024)
                if not data:
                    self.output_communication_message("服务器关闭了连接！！")
                    break  # 服务端关闭连接
                if server_object.connectState == EnumValue.ConnectionState.DISCONNECTION:
                    
                    self.output_communication_message(f"已关闭{server_object.addr}的连接！！")
                    break 
                # 处理接收到的数据，这里简单地将其回送给客户端
                self.output_communication_message(f"收到来自 server 的消息: {data.decode()}")
                
                # 发送回复消息给客户端
                reply_message = f"客户端已收到消息: {data.decode()}"
                server_object.socket.send(reply_message.encode())

        except Exception as e:
            self.output_communication_message(f"与server 通信时发生错误: {e}")

        finally:
            # 关闭服务器的 socket
            server_object.socket.close()
            server_object.server_object.connectState = EnumValue.ConnectionState.DISCONNECTION
            self.delete_comBox_item(self.view.ServerObject_ComBox,server_object.name)
            #从combox中删除该项
    
    '''   
    #断开与服务器的连接,关闭socket,从combox中删除该项
    def stop_connect_click(self):
        select_item = self.view.ServerObject_ComBox.currentText()
        server_object = self.server_objects[select_item]
        server_object.connectState =ConnectionState.DISCONNECTION
        index_to_remove = self.view.ServerObject_ComBox.currentIndex()
        self.view.ServerObject_ComBox.removeItem(index_to_remove)
        server_object.stop_receive()
        self.output_communication_message(f"已经关闭到服务器{self.current_server.peer_name}的连接！")
    #客户端选择要将消息保存的文件路径
    def cient_select_saved_file_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)
        self.view.FilePath_Input_3.setText(file_name)
    #发送密文给服务器
    def send_to_server_click(self):
        cipher = self.view.CipherText_Output.toPlainText()
        if not cipher:
            self.show_error_message("无效的密文输入！！")
            return
        if not self.current_server:
            self.show_error_message("未连接任何服务器！！")
        message_to_send = f"密文：{cipher}"
        self.current_server.sendMessage(message_to_send.encode('utf-8'))
        self.output_communication_message(f"向服务器{self.current_server.peer_name}发送cipherText!!")
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
        p = self.view.ClientP_Inputline.text()
        g = self.view.ClientG_Inputline.text()
        if not p or not g:
            self.show_error_message("Invalid P or G!!")
            return
        if not self.current_server:
            self.show_error_message("未连接任何服务器！！")
        message_to_send = f"向服务器{self.current_server.peer_name}发送P:{p}、G:{g}"
        self.current_server.sendMessage(message_to_send.encode('utf-8'))
        self.output_communication_message(f"向服务器{self.current_server.peer_name}发送P、G")
    #客户端发送自己的公钥
    def client_send_PubKey(self):
        pubKey = self.view.cClientPubKey_Input.toPlainText()
        if not pubKey:
            self.show_error_message("无效的公钥输入！！")
            return
        if not self.current_server:
            self.show_error_message("未连接任何服务器！！")
        message_to_send = f"向服务器{self.current_server.peer_name}发送pubKey:{pubKey}!!"
        self.current_server.sendMessage(message_to_send.encode('utf-8'))
        self.output_communication_message(f"向服务器{self.current_server.peer_name}发送pubKey!!")
    #客户端通过服务端的公钥以及其他参数计算出key
    def client_generate_key(self):
        p = int(self.view.ClientP_Inputline.text())
        a = int(self.view.ClientA_Inputline.text())
        serverPubKey = int(self.view.cServerPubKey_Input.toPlainText())
        #作为客户端，据已有的p,g,a，客户端pubkey,服务端pubkey来计算最后的key
        shared_key = pow(serverPubKey, a, p)
        self.view.ClientGeneratedKey_Output.setPlainText(str(shared_key))
     #保存服务器信息
    def save_server_object_setting_Button(self):
        if not self.current_server:
            self.show_error_message("未选择服务器对象")
            return
        self.current_server.p = self.view.ClientP_Inputline.text()
        self.current_server.g = self.view.ClientG_Inputline.text()
        self.current_server.a = self.view.ClientA_Inputline.text()
        self.current_server.cPubKey= self.view.cClientPubKey_Input.toPlainText()
        self.current_server.sPubKey= self.view.cServerPubKey_Input.toPlainText()
        self.current_server.key= self.view.ClientGeneratedKey_Output.toPlainText()
        self.output_communication_message(f"成功将参数保存到客户端对象{self.current_server.peer_name}")
    #处理接受到的消息
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
    def new_item(self,itemName):
        self.view.ServerObject_ComBox.addItem(itemName)
    #改变combobox
    def on_combobox_changed(self, index):
        #combox选项数归零时不设置
        if self.view.ServerObject_ComBox.count()==0:
             self.current_server = None
             return
        # 当选项改变时调用的函数,更改当前的通信对象
        selected_text = self.view.ServerObject_ComBox.itemText(index)
        print(f"selected text is {selected_text}")
        self.current_server =  self.server_objects[selected_text]
    #将一个新的消息输出到
    def output_communication_message(self, message):
        # 将新消息添加到 ClientMessageBox，并自动换行
        self.view.ClientMessageBox.appendPlainText(message)
        pass