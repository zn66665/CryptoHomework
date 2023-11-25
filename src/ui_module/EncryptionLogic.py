#实现共十一种解密调用的逻辑


from lib import caesar,keyword,vigenere,autokey
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIntValidator

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