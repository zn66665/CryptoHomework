from lib import caesar,keyword,vigenere,autokey,playfair
from . import Common

class DecryptionLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view

    def decrypto_click(self):
        if self.view.Caesar_Box_2.isChecked():
            self.caesar_decrypto(self.view)
        elif self.view.Keyword_Box_2.isChecked():
            self.keyword_decrypto(self.view)
        elif self.view.Permutation_Box_2.isChecked():
            self.permutation_decrypto(self.view)
        elif self.view.CA_Box_2.isChecked():
            self.ca_decrypto(self.view)
        elif self.view.Autokey_Box_2.isChecked():
            self.autokey_decrypto(self.view)
        elif self.view.AES_Box_2.isChecked():
            self.AES_decrypto(self.view)
        elif self.view.RSA_Box_2.isChecked():
            self.RSA_decrypto(self.view)
        elif self.view.Vigenere_Box_2.isChecked():
            self.vigenere_decrypto(self.view)
        elif self.view.Playfair_Box_2.isChecked():
            self.playfair_decrypto(self.view)
        elif self.view.DoubleTransposition_Box_2.isChecked():
            self.double_transposition_decrypto(self.view)
        else:
            self.show_error_message("Unchecked Decryption Method !!")
            #error
        ########################解密逻辑##########################
    #凯撒解密
    def caesar_decrypto(self,view):
        #获取明文域和file文件中的内容
        #设置key的输入验证
        view.set_int_validator(view.Key_Input_2)
        cipher_text=view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        # 判断输入是否为数字
        if not key or not cipher_text:
            self.show_error_message("Invalid Input Key or cipherText !!!")
        plain_text= caesar.caesar(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
        view.Key_Input_2.setValidator(None)

    #关键字解密
    def keyword_decrypto(self,view):
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        plain_text= keyword.key(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)

    #置换解密
    def permutation_decrypto(self,view):
        pass
    
    #CA解密
    def ca_decrypto(self,view):
        pass
    
    #autokey解密
    def autokey_decrypto(self,view):
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        plain_text= autokey.autokey(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)



    #AES解密
    def AES_decrypto(self):
        pass

    #RSA解密
    def RSA_decrypto(self):
        pass

    #vigenere解密
    def vigenere_decrypto(self,view):
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        plain_text= vigenere.vigenere(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)


    #栅栏解密
    def playfair_decrypto(self,view):
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        plain_text= playfair.playfair(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)

    #双置换解密
    def double_transposition_decrypto(self):
        pass


