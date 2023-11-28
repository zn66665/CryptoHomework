from . import ClientLogic,DecryptionLogic,EncryptionLogic,ServerLogic


class Logic(object):
    def __init__(self,_view):
        self.view = _view
        self.client=ClientLogic.ClientLogic(_view)
        self.server=ServerLogic.ServerLogic(_view)
        self.encryption=EncryptionLogic.EncryptionLogic(_view)
        self.decryption=DecryptionLogic.DecryptionLogic(_view)
    
    #加密
    def encrypto_click(self):
        self.encryption.encrypto_click()
    #解密
    def decrypto_click(self):
        self.decryption.decrypto_click()
    #连接服务器
    def connect_server_click(self):
        self.client.connect_server_click()
    #监听客户端连接
    def listen_client_click(self):
        self.server.listen_client_click()
    #断开连接
    def stop_connect_click(self):
        self.client.stop_connect_click()
    #停止监听，断开所有连接
    def stop_listen_click(self):
        self.server.stop_listen_click()
    #发送密文给客户端
    def send_to_client_click(self):
        self.server.send_to_client_click()
    #发送密文给服务器
    def send_to_server_click(self):
        self.client.send_to_server_click()
    #选择明文文件
    def select_plain_text_file(self):
        self.encryption.select_plain_text_file()
    #选择密文文件
    def select_cipher_text_file(self):
        self.decryption.select_cipher_text_file()
    #客户端选择要将消息保存的文件路径
    def client_select_saved_file_path(self):
        self.client.cient_select_saved_file_path()
    #server选择要将消息保存的文件路径
    def server_select_saved_file_path(self):
        self.server.server_select_saved_file_path()
    #客户端随机生成p,g,a参数
    def client_random_generate(self):
        self.client.client_random_generate()
    #客户端通过p,g,a参数计算出公钥
    def client_generate_pubKey(self):
        self.client.client_generate_pubKey()
    #发送p,g参数到服务器
    def sendPG2Server(self):
        self.client.sendPG2Server()
    #客户端发送自己的公钥
    def client_send_PubKey(self):
        self.client.client_send_PubKey()
    #客户端通过服务端的公钥以及其他参数计算出key
    def client_generate_key(self):
        self.client.client_generate_key()
    #服务端随机生成p,g,a参数
    def server_random_generate(self):
        self.server.server_random_generate()
    #服务端通过p,g,a参数计算出公钥
    def server_generate_pubKey(self):
        self.server.server_generate_pubKey()
    #发送p,g参数到客户端
    def sendPG2Client(self):
        self.server.sendPG2Client()
    #服务端发送自己的公钥
    def server_send_pubKey(self):
        self.server.server_send_pubKey()
    #服务端通过客户端的公钥以及其他参数计算出key
    def server_generate_key(self):
        self.server.server_generate_key()
    #客户端
    def client_combobox_changed(self,index):
        self.client.on_combobox_changed(index)
    #服务端
    def server_combobox_changed(self,index):
        self.server.on_combobox_changed(index)