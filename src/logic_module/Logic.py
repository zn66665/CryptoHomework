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
        pass
    #停止监听，断开所有连接
    def stop_listen_click(self):
        pass
    #发送密文给客户端
    def send_to_client_click(self):
        pass
    #发送密文给服务器
    def send_to_server_click(self):
        pass
    #选择明文文件
    def select_plain_text_file(self):
        pass
    #选择密文文件
    def select_cipher_text_file(self):
        pass
    #客户端选择要将消息保存的文件路径
    def cient_select_saved_file_path():
        pass
    #server选择要将消息保存的文件路径
    def server_select_saved_file_path():
        pass
    #客户端随机生成p,g,a参数
    def client_random_generate(self):
        pass
    #客户端通过p,g,a参数计算出公钥
    def client_generate_pubKey(self):
        pass
    #发送p,g参数到服务器
    def sendPG2Server(self):
        pass
    #客户端发送自己的公钥
    def client_send_PubKey(self):
        pass
    #客户端通过服务端的公钥以及其他参数计算出key
    def client_generate_key(self):
        pass
    #服务端随机生成p,g,a参数
    def server_random_generate(self):
        pass
    #服务端通过p,g,a参数计算出公钥
    def server_generate_pubKey(self):
        pass
    #发送p,g参数到客户端
    def sendPG2Client(self):
        pass
    #服务端发送自己的公钥
    def server_send_pubKey(self):
        pass
    #服务端通过客户端的公钥以及其他参数计算出key
    def server_generate_key(self):
        pass