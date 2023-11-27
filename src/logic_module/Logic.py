from . import ClientLogic,DecryptionLogic,EncryptionLogic,NetCommunication,ServerLogic


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

    def connect_server_click(self):
        self.client.connect_server_click()
    
    def listen_client_click(self):
        self.server.listen_client_click()