from lib import caesar,keyword,vigenere,autokey,playfair,column_permutation
from . import Common
import os
import time
from PyQt5.QtWidgets import QFileDialog
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
        # 获取文件内容
        file_content=self.file_content()
        #设置key的输入验证
        view.set_int_validator(view.Key_Input_2)
        cipher_text=view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        # 判断输入是否为数字
        if not key or not cipher_text:
            self.show_error_message("Invalid Input Key or cipherText !!!")
        if file_content is not None:
            out_content=caesar.caesar(1,file_content,key)
            self.file_write(out_content)
        plain_text= caesar.caesar(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
        view.Key_Input_2.setValidator(None)

    #关键字解密
    def keyword_decrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=keyword.key(1,file_content,key)
            self.file_write(out_content)
        plain_text= keyword.key(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)

    #置换解密
    def permutation_decrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=column_permutation.column_permutation(1,file_content,key)
            self.file_write(out_content)
        plain_text= column_permutation.column_permutation(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
    
    #CA解密
    def ca_decrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=column_permutation.column_permutation(1,file_content,key)
            self.file_write(out_content)
        plain_text= column_permutation.column_permutation(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
    
    #autokey解密
    def autokey_decrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=autokey.autokey(1,file_content,key)
            self.file_write(out_content)
        plain_text= autokey.autokey(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)



    #AES解密
    def AES_decrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=autokey.autokey(1,file_content,key)
            self.file_write(out_content)
        plain_text= autokey.autokey(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
        pass
    #RSA解密
    def RSA_decrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=autokey.autokey(1,file_content,key)
            self.file_write(out_content)
        plain_text= autokey.autokey(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
        pass

    #vigenere解密
    def vigenere_decrypto(self,view):
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=vigenere.vigenere(1,file_content,key)
            self.file_write(out_content)
        plain_text= vigenere.vigenere(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)


    #栅栏解密
    def playfair_decrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=playfair.playfair(1,file_content,key)
            self.file_write(out_content)
        plain_text= playfair.playfair(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)

    #双置换解密
    def double_transposition_decrypto(self,view):
          # 获取文件内容
        file_content=self.file_content()
        cipher_text = view.CiperText_Input.toPlainText()
        key=view.Key_Input_2.text()
        if file_content is not None:
            out_content=playfair.playfair(1,file_content,key)
            self.file_write(out_content)
        plain_text= playfair.playfair(1,cipher_text,key)
        view.PlainText_Output.setPlainText(plain_text)
        pass
    #选择密文文件
    def select_cipher_text_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)
        self.view.FilePath_Input_2.setText(file_name)
        #返回文件内容
    def file_content(self):
         # 获取文件选择路径
        file_path = self.view.FilePath_Input.text()
        if not file_path or not os.path.exists(file_path):
            return None
        # 读取文件内容
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    def file_write(self,content):
        # 生成不重复的输出文件名
        file_path = self.view.FilePath_Input.text()
        # 确保路径是目录，如果是文件则获取文件所在目录
        if os.path.isfile(file_path):
            file_path = os.path.dirname(file_path)
        output_file_name = "decrypted_" + str(int(time.time())) + ".txt"
        output_path = os.path.join(file_path, output_file_name)
        with open(output_path, 'w') as output_file:
            output_file.write(content)

