from lib import caesar,keyword,vigenere,autokey,playfair,column_permutation,AES,RC4
from . import Common
import os
import time
from PyQt5.QtWidgets import QFileDialog

class EncryptionLogic(Common.Common):
    def __init__(self,_view):
        self.view = _view
    
    def encrypto_click(self):
        if self.view.Caesar_Box.isChecked():
            self.caesar_encrypto(self.view)
        elif self.view.Keyword_Box.isChecked():
            self.keyword_encrypto(self.view)
        elif self.view.Permutation_Box.isChecked():
            self.column_permutation_encrypto(self.view)
        elif self.view.CA_Box.isChecked():   
            self.RC4_encrypto(self.view)
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
            self.permutation_encrypto(self.view)
        else:
            self.show_error_message("Unchecked Eecryption Method !!")
            #error
################加密调用逻辑#################    
    #凯撒加密
    def caesar_encrypto(self,view):
        #获取明文域和file文件中的内容
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
          # 判断输入key是否为数字
        if not key or not key.isdigit():
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=caesar.caesar(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= caesar.caesar(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)
    #关键字加密
    def keyword_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=keyword.key(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= keyword.key(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #置换加密
    def column_permutation_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=column_permutation.column_permutation(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= column_permutation.column_permutation(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)
    
    #RC4加密
    def RC4_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=RC4.rc4(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= RC4.rc4(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    
    #autokey加密
    def autokey_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=autokey.autokey(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= autokey.autokey(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #AES加密
    def AES_encrypto(self,view):
         # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=AES.AES(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= AES.AES(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #RSA加密
    def RSA_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=RC4.rc4(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= RC4.rc4(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)

    #vigenere加密
    def vigenere_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=vigenere.vigenere(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= vigenere.vigenere(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)


    #栅栏加密
    def playfair_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        plain_text = view.PlainText_Input.toPlainText()
        key=view.Key_Input.text()
        if not key:
            self.show_error_message("Invalid Input Key!!!")
        #加密文件内容，并输出到新文件中
        if file_content is not None:
            out_content=playfair.playfair(0,file_content,key)
            self.file_write(out_content)
        if plain_text is None:
            return
        cipher_text= playfair.playfair(0,plain_text,key)
        view.CipherText_Output.setPlainText(cipher_text)
    #双置换加密
    def permutation_encrypto(self,view):
        # 获取文件内容
        file_content=self.file_content()
        pass
    #选择明文文件
    def select_plain_text_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print("Selected file:", file_name)
        self.view.FilePath_Input.setText(file_name)
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
        output_file_name = "encrypted_" + str(int(time.time())) + ".txt"
        output_path = os.path.join(file_path, output_file_name)
        with open(output_path, 'w') as output_file:
            output_file.write(content)