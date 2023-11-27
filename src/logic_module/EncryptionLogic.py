from lib import caesar,keyword,vigenere,autokey,playfair
from . import Common

class EncryptionLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
    
    def encrypto_click(self):
        if self.view.Caesar_Box.isChecked():
            self.caesar_encrypto(self.view)
        elif self.view.Keyword_Box.isChecked():
            self.keyword_encrypto(self.view)
        elif self.view.Permutation_Box.isChecked():
            self.permutation_encrypto(self.view)
        elif self.view.CA_Box.isChecked():   
            self.ca_encrypto(self.view)
        elif self.view.Autokey_Box.isChecked():
            self.autokey_encrypto(self.view)
        elif self.view.AES_Box.isChecked():
            self.AES_encrypto(self.view)
        elif self.view.RSA_Box.isChecked():
            self.RSA_encrypto(self.view)
        elif self.view.Vigenere_Box.isChecked():
            self.vigenere_encrypto(self.view)
        elif self.view.Playfair_Box.isChecked():
            self.playfair_encrypto(self.view)
        elif self.view.DoubleTransposition_Box.isChecked():
            self.double_transposition_encrypto(self.view)
        else:
            self.show_error_message("Unchecked Eecryption Method !!")
            #error
################加密调用逻辑#################    
    #凯撒加密
    def caesar_encrypto(self,view):
        #获取明文域和file文件中的内容
        #设置key的输入验证
        view.set_int_validator(view.Key_Input)
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
          # 判断输入是否为数字
        if not key or not plain_text:
            self.show_error_message("Invalid Input Key or plainText !!!")
        
        cipher_text= caesar.caesar(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)
        view.Key_Input.setValidator(None)

    #关键字加密
    def keyword_encrypto(self,view):
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        cipher_text= keyword.key(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #置换加密
    def permutation_encrypto(self,view):
        pass
    
    #CA加密
    def ca_encrypto(self,view):
        pass
    
    #autokey加密
    def autokey_encrypto(self,view):
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        cipher_text= autokey.autokey(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #AES加密
    def AES_encrypto(self,view):
        pass

    #RSA加密
    def RSA_encrypto(self,view):
        pass

    #vigenere加密
    def vigenere_encrypto(self,view):
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        cipher_text= vigenere.vigenere(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)


    #栅栏加密
    def playfair_encrypto(self,view):
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        cipher_text= playfair.playfair(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)


    #双置换加密
    def double_transposition_encrypto(self,view):
        pass
