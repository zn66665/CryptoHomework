# -*- coding: utf-8 -*-

from lib import caesar,keyword,vigenere,autokey
from . import SuperScurity
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator

class PortalMainWindow(SuperScurity.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.setupButton()
        
    def setupButton(self):
        self.Encrypto_Button.clicked.connect(self.encrypto_click)
    #获取文件路径，加密，生成加密的文件

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
            QMessageBox.information('用户输入不是数字:', key)
        cipher_text= caesar.caesar(0,plain_text,key)
        self.CipherText_Output.setPlainText(cipher_text)

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
            pass
            #error

        

     

        