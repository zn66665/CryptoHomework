# -*- coding: utf-8 -*-
import asyncio
from lib import caesar,keyword,vigenere,autokey,socketcon
from . import SuperSecurity
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QRegularExpression, QRegularExpressionValidator

class PortalMainWindow(SuperSecurity.Ui_MainWindow):
    def __init__(self):
        # 将 remote_socket 变量初始化为 None
        self.remote_socket = None
        self.local_socket=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.setupButton()
        
    #设置按钮监听事件
    def setupButton(self):
        self.Encrypto_Button.clicked.connect(self.encrypto_click)
        self.Decrypto_Button.clicked.connect(self.decrypto_click)
        self.SendToRemote_Button.clicked.connect(self.send_ciphertext_click)
        self.ConnectRemote_Button.clocked.connect(self.connect_remote_click)
        self.DisconnectRemote_Button.clicked.connct(self.stop_connect_click)
        self.StartListen_Button.clicked.connect(self.listen_local_click)
        self.StopListen_Button.clicked.connect(self.stop_listen_click)
        self.RandomGenerate_Button.clicked.connect(self.random_generate_pga_click)
        self.GeneratePubKey_Button.clicked.connect(self.generate_pubkey_click)
        self.SendPG_Button.clicked.connect(self.send_pg_click)
        self.SendPubKey_Button.clicked.connect(self.send_pubkey_click)
        self.GenerateKey_Button.clicked.connect(self.generate_common_key)

    #set encrypto button onclick
    def encrypto_click(self):
        if self.Caesar_Box.isChecked():
            self.caesar_encrypto()
        elif self.Keyword_Box.isChecked():
            self.keyword_encrypto()
        elif self.Permutation_Box.isChecked():
            self.permutation_encrypto()
        elif self.CA_Box.isChecked():
            self.ca_encrypto()
        elif self.Autokey_Box.isChecked():
            self.autokey_encrypto()
        elif self.AES_Box.isChecked():
            self.AES_encrypto()
        elif self.RSA_Box.isChecked():
            self.RSA_encrypto()
        elif self.Vigenere_Box.isChecked():
            self.vigenere_encrypto()
        elif self.Playfair_Box.isChecked():
            self.playfair_encrypto()
        elif self.DoubleTransposition_Box.isChecked():
            self.double_transposition_encrypto()
        else:
            self.show_error_message("Unchecked Eecryption Method !!")
            #error
    #set decrypto button onclick
    def decrypto_click(self):
        if self.Caesar_Box_2.isChecked():
            self.caesar_decrypto()
        elif self.Keyword_Box_2.isChecked():
            self.keyword_decrypto()
        elif self.Permutation_Box_2.isChecked():
            self.permutation_decrypto()
        elif self.CA_Box_2.isChecked():
            self.ca_decrypto()
        elif self.Autokey_Box_2.isChecked():
            self.autokey_decrypto()
        elif self.AES_Box_2.isChecked():
            self.AES_decrypto()
        elif self.RSA_Box_2.isChecked():
            self.RSA_decrypto()
        elif self.Vigenere_Box_2.isChecked():
            self.vigenere_decrypto()
        elif self.Playfair_Box_2.isChecked():
            self.playfair_decrypto()
        elif self.DoubleTransposition_Box_2.isChecked():
            self.double_transposition_decrypto()
        else:
            self.show_error_message("Unchecked Decryption Method !!")
            #error

    #连接远程,
    def connect_remote_click(self):
        #获取用户输入的ip地址和端口号，使用正则表达式做输入验证
        self.set_ip_validator(self.RemoteAddress_Input)
        self.set_port_validator(self.RemotePort_Input)
        remote_address=self.RemoteAddress_Input.text()
        remote_port=self.RemotePort_Input.text()
        if not remote_address or not remote_port:
            self.show_error_message("Invalid remote address or port!!")
        #调用socket_connect()函数连接remote,返回remote_socket对象
        self.remote_socket=socketcon.remote_socket_connect(remote_address,remote_port)
        if self.remote_socket:
            pass
        else:
        # 处理连接失败的情况
            self.show_error_message("连接失败，无法进行通信操作")
        self.RemoteAddress_Input.setValidator(None)
        self.RemotePort_Input.setValidator(None)

    #启动监听来自客户端的请求
    def listen_local_click(self):
        #设置地址和端口输入验证
        self.set_ip_validator(self.ListenAddress_Input)
        self.set_port_validator(self.ListenPort_Input)
        #输入的端口和地址可以为0,则默认监听0.0.0.0地址以及8080端口
        listen_address=self.ListenAddress_Input.text()
        listen_port=self.ListenPort_Input.text()
        if not listen_address:
            listen_address='0.0.0.0'
        if not listen_port:
            listen_port=8080
        #建立bind到指定网络接口的socket
        socketcon.bind_listen_sokcet(self.local_socket,listen_address,listen_port)
        #开始执行异步监听，接受来自客户端的请求，异步执行，不阻塞主线程
        pass
    #断开连接
    def stop_connect_click(self):
        pass
    #停止监听
    def stop_listen_click(self):
        pass
    #发送密文
    def send_ciphertext_click(self):
        pass
    #随机生成p,g,a(私钥)
    def random_generate_pga_click(self):
        pass
    #生成公钥，根据p,g,a
    def generate_pubkey_click(self):
        pass
    #将p,g参数发送到remote
    def send_pg_click(self):
        pass
    #发送生成的pubkey到remote
    def send_pubkey_click(self):
        pass
    #通过以上参数，以及计算的local pubkey和remote pubkey来生成共享密钥
    def generate_common_key(self):
        pass

    async def start_listening(self):
        #更新状态
        try:
            self.local_socket.bind((host, port))
            print(f"服务端已绑定到 {host}:{port}")
        except Exception as e:
            print(f"服务端出现错误: {e}")

        finally:
        # 关闭服务端 socket
            self.local_socket.close()
        pass

################加密调用逻辑#################    
    #凯撒加密
    def caesar_encrypto(self):
           #获取明文域和file文件中的内容
        int_validator = QIntValidator()
        # 将验证器应用于输入框
        self.Key_Input.setValidator(int_validator)
        plain_text = self.PlainText_Input.toPlainText()
        key=self.Key_Input.text()
          # 判断输入是否为数字
        if self.Key_Input.hasAcceptableInput():
            pass
        else:
            self.show_error_message("Invalid Input Key!!")
        cipher_text= caesar.caesar(0,plain_text,key)
        self.CipherText_Output.setPlainText(cipher_text)
        self.Key_Input.setValidator(None)

    #关键字加密
    def keyword_encrypto(self):
        plain_text = self.PlainText_Input.toPlainText()
        key=self.Key_Input.text()
        cipher_text= keyword.key(0,plain_text,key)
        self.CipherText_Output.setPlainText(cipher_text)

    #置换加密
    def permutation_encrypto(self):
        pass
    
    #CA加密
    def ca_encrypto(self):
        pass
    
    #autokey加密
    def autokey_encrypto(self):
        plain_text = self.PlainText_Input.toPlainText()
        key=self.Key_Input.text()
        cipher_text= autokey.autokey(0,plain_text,key)
        self.CipherText_Output.setPlainText(cipher_text)

    #AES加密
    def AES_encrypto(self):
        pass

    #RSA加密
    def RSA_encrypto(self):
        pass

    #vigenere加密
    def vigenere_encrypto(self):
        plain_text = self.PlainText_Input.toPlainText()
        key=self.Key_Input.text()
        cipher_text= vigenere.vigenere(0,plain_text,key)
        self.CipherText_Output.setPlainText(cipher_text)


    #栅栏加密
    def playfair_encrypto(self):
        pass

    #双置换加密
    def double_transposition_encrypto(self):
        pass

########################解密逻辑##########################
    #凯撒解密
    def caesar_decrypto(self):
           #获取明文域和file文件中的内容
        int_validator = QIntValidator()
        # 将验证器应用于输入框
        self.Key_Input_2.setValidator(int_validator)
        cipher_text=self.CiperText_Input.toPlainText()
        key=self.Key_Input_2.text()
        # 判断输入是否为数字
        if self.Key_Input.hasAcceptableInput():
            pass
        else:
            self.show_error_message("Invalid Input Key,Expected a Number!!!")
        plain_text= caesar.caesar(1,cipher_text,key)
        self.PlainText_Output.setPlainText(plain_text)
        self.Key_Input_2.setValidator(None)

    #关键字解密
    def keyword_decrypto(self):
        cipher_text = self.CiperText_Input.toPlainText()
        key=self.Key_Input_2.text()
        plain_text= keyword.key(1,cipher_text,key)
        self.PlainText_Output.setPlainText(plain_text)

    #置换解密
    def permutation_decrypto(self):
        pass
    
    #CA解密
    def ca_decrypto(self):
        pass
    
    #autokey解密
    def autokey_decrypto(self):
        cipher_text = self.CiperText_Input.toPlainText()
        key=self.Key_Input_2.text()
        plain_text= autokey.autokey(1,cipher_text,key)
        self.PlainText_Output.setPlainText(plain_text)



    #AES解密
    def AES_decrypto(self):
        pass

    #RSA解密
    def RSA_decrypto(self):
        pass

    #vigenere解密
    def vigenere_decrypto(self):
        cipher_text = self.CiperText_Input.toPlainText()
        key=self.Key_Input_2.text()
        plain_text= vigenere.vigenere(1,cipher_text,key)
        self.PlainText_Output.setPlainText(plain_text)


    #栅栏解密
    def playfair_decrypto(self):
        pass

    #双置换解密
    def double_transposition_decrypto(self):
        pass



###########输入验证################
    def set_ip_validator(self,ip_input):
        ip_validator = QRegularExpressionValidator(QRegularExpression(
            "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
        ))
        ip_input.setValidator(ip_validator)
    def set_port_validator(self,port_input):
        port_validator = QRegularExpressionValidator(QRegularExpression("^[1-9]\\d{0,4}$"))
        port_input.setValidator(port_validator)



#############错误提示####################
    #输出错误提示
    def show_error_message(self,error_message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Error")
        error_box.setText(error_message)
        error_box.setStyleSheet("QMessageBox QLabel{min-width: 300px; font-size: 18px;}")
        #desktop = QDesktopWidget()
        #screen_rect = desktop.availableGeometry(desktop.primaryScreen())
        #error_box.move(screen_rect.center() - error_box.rect().center())
        # 显示消息框
        error_box.exec_()

        # 将消息框移动到屏幕中间
      

        
    

    