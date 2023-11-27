from . import SuperSecurity
from logic_module import Logic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class PortalMainWindow(SuperSecurity.Ui_MainWindow):
    
    def __init__(self):
        self.logic = Logic.Logic(self)

    # 将 remote_socket 变量初始化为 None
    remote_socket = None
    local_socket = None
    client_socket = None
    client_addr = None


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.presetting_vaildator()
        self.setupButton()
        
    #设置按钮监听事件
    def setupButton(self):
        self.Encrypto_Button.clicked.connect(self.encrypto_click)
        self.Decrypto_Button.clicked.connect(self.decrypto_click)
        self.SendToClient_Button.clicked.connect(self.send_to_client_click)
        self.SendToServer_Button.clicked.connect(self.send_to_server_click)
        self.SelectPlainTextFile.clicked.connect(self.select_plain_text_file)
        self.SelectCipherTextFile.clicked.connect(self.select_cipher_text_file)
        self.cSelectSavedFilePath.clicked.connect(self.cient_select_saved_file_path)
        self.sSelectSavedFilePath.clicked.connect(self.server_select_saved_file_path)
        self.ConnectServer_Button.clicked.connect(self.connect_server_click)
        self.DisconnectServer_Button.clicked.connect(self.stop_connect_click)
        self.StartListen_Button.clicked.connect(self.listen_client_click)
        self.StopListen_Button.clicked.connect(self.stop_listen_click)
        self.ClientRandomGenerate_Button.clicked.connect(self.client_random_generate)
        self.ClientGeneratePubKey_Button.clicked.connect(self.client_generate_pubKey)
        self.SendPG2Server_Button.clicked.connect(self.sendPG2Server)
        self.ClientSendPubKey_Button.clicked.connect(self.client_send_PubKey)
        self.ClientGenerateKey_Button.clicked.connect(self.client_generate_key)
        self.ServerRandomGenerate_Button.clicked.connect(self.server_random_generate)
        self.ServerGeneratePubKey_Button.clicked.connect(self.server_generate_pubKey)
        self.SendPG2Client_Button.clicked.connect(self.sendPG2Client)
        self.ServerSendPubKey_Button.clicked.connect(self.server_send_pubKey)
        self.ServerGenerateKey_Button.clicked.connect(self.server_generate_key)
    #pre-setting vaildator，预先设置某些输入的输入验证要求
    def presetting_vaildator(self):
        #设置地址和端口输入验证
        self.set_ip_validator(self.ListenAddress_Input)
        self.set_port_validator(self.ListenPort_Input)
        #获取用户输入的ip地址和端口号，使用正则表达式做输入验证
        self.set_ip_validator(self.ServerAddress_Input)
        self.set_port_validator(self.ServerPort_Input)
    #set encrypto button onclick
    def encrypto_click(self):
        self.logic.encrypto_click()      
    #set decrypto button onclick
    def decrypto_click(self):
        self.logic.decrypto_click()
    #连接远程服务器,
    def connect_server_click(self):
        self.logic.connect_server_click()
    #启动监听来自客户端的请求,判断当前是否已经在监听
    def listen_client_click(self):
        self.logic.listen_client_click()
    #断开连接
    def stop_connect_click(self):
        self.logic.stop_connect_click()
    #停止监听
    def stop_listen_click(self):
        self.logic.stop_listen_click()
    #发送密文给客户端
    def send_to_client_click(self):
        self.logic.send_to_client_click()
    #发送密文给服务器
    def send_to_server_click(self):
        self.logic.send_to_server_click()
    #选择明文文件
    def select_plain_text_file(self):
        self.logic.select_plain_text_file()
    #选择密文文件
    def select_cipher_text_file(self):
        self.logic.select_cipher_text_file()
    #客户端选择要将消息保存的文件路径
    def cient_select_saved_file_path(self):
        self.logic.client_select_saved_file_path()
    #server选择要将消息保存的文件路径
    def server_select_saved_file_path(self):
        self.logic.server_select_saved_file_path()
    #客户端随机生成p,g,a参数
    def client_random_generate(self):
        self.logic.client_random_generate()
    #客户端通过p,g,a参数计算出公钥
    def client_generate_pubKey(self):
        self.logic.client_generate_pubKey()
    #发送p,g参数到服务器
    def sendPG2Server(self):
        self.logic.sendPG2Server()
    #客户端发送自己的公钥
    def client_send_PubKey(self):
        self.logic.client_send_PubKey()
    #客户端通过服务端的公钥以及其他参数计算出key
    def client_generate_key(self):
        self.logic.client_generate_key()
    #服务端随机生成p,g,a参数
    def server_random_generate(self):
        self.logic.server_random_generate()
    #服务端通过p,g,a参数计算出公钥
    def server_generate_pubKey(self):
        self.logic.server_generate_pubKey()
    #发送p,g参数到客户端
    def sendPG2Client(self):
        self.logic.sendPG2Client()
    #服务端发送自己的公钥
    def server_send_pubKey(self):
        self.logic.server_send_pubKey()
    #服务端通过服务端的公钥以及其他参数计算出key
    def server_generate_key(self):
        self.logic.server_generate_key()
###########输入验证################
    #ip,端口输入验证
    def set_ip_validator(self,ip_input):
        
        ip_validator = QRegExpValidator(QRegExp(
            "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
        ))
        ip_input.setValidator(ip_validator)
    def set_port_validator(self,port_input):
        port_validator = QRegExpValidator(QRegExp("^[1-9]\\d{0,4}$"))
        port_input.setValidator(port_validator)
    def set_int_validator(self,key_input):
        int_validator = QIntValidator()
        # 将验证器应用于输入框
        key_input.setValidator(int_validator)
    #为输入框设置字符验证，只允许字母作为输入
    def set_char_validator(self,input):
        pass

        
    

    