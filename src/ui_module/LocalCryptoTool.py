
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class LocalCryptoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

           # 获取当前文件所在的目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 使用相对路径加载 ui 文件
        uic.loadUi(os.path.join(current_dir, 'LocalCryptoTool.ui'), self)
        self.pushButton.clicked.connect(self.on_button_clicked)
        self.pushButton_2.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # 这里是按钮点击事件的处理代码
        print("Button Clicked")