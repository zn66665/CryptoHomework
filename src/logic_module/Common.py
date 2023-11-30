
from PyQt5.QtWidgets import QMessageBox
import random
import socket
from Crypto.Util import number
class Common(object):

    ###随机生成p,g,a
    def generate_large_prime(self):
        # 生成一个足够大的素数（例如 2048 位）
        return number.getPrime(1024)

    def choose_generator(self,p):
        # 选择一个生成元 g，这里简单地选择 2
        return 2

    def generate_private_key(self, p):
        # 生成一个小于 p 的随机私钥
        return random.randint(2, p-2)
    
    def generate_connection_name(self,connection):
    # 获取连接的客户端地址和端口号
        client_address, client_port = connection.getpeername()

        # 可选：尝试获取主机名
        try:
            host_name = socket.gethostbyaddr(client_address)[0]
        except socket.herror:
        # 如果无法解析主机名，则使用 IP 地址
            host_name = client_address

        # 创建并返回命名字符串
        return f"{host_name}_port{client_port}"
    #删除combox中的某一项
    def delete_comBox_item(self,comboBox,text):
        index_to_remove = self.find_index_by_text(comboBox,text)
        comboBox.removeItem(index_to_remove)
    def find_index_by_text(comboBox, text):
        for index in range(comboBox.count()):
            if comboBox.itemText(index) == text:
                return index
        return -1  # 如果没有找到匹配的项，则返回 -1
    #############提示窗口####################
    #输出正常提示
    def show_tip_message(self,message):
        tip_box = QMessageBox()
        tip_box.setIcon(QMessageBox.Information)
        tip_box.setWindowTitle("Tip")
        tip_box.setText(message)
        tip_box.setStyleSheet("QMessageBox QLabel{min-width: 300px; font-size: 18px;}")
        tip_box.exec_()
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
    #检查连接状态
    def check_sokcet_state(socket):
    #更新连接状态
        pass
    def update_state(self,new_state):
        pass

