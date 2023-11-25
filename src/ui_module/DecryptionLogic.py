#实现十一种调用解密的逻辑

from lib import caesar,keyword,vigenere,autokey
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIntValidator


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

#输出错误提示
def show_error_message(self, error_message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Warning)
    error_box.setWindowTitle("Error")
    error_box.setText(error_message)
    error_box.setStyleSheet("QMessageBox QLabel{min-width: 300px; font-size: 18px;}")

    # 显示消息框
    error_box.show()

    # 将消息框移动到屏幕中间
    desktop = QDesktopWidget()
    screen_rect = desktop.availableGeometry(desktop.primaryScreen())
    error_box.move(screen_rect.center() - error_box.rect().center()) 