# -*- coding: utf-8 -*-

import sys
from ui_module import Portal
from PyQt5.QtWidgets import QApplication, QMainWindow


    #加载主窗口

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Portal.PortalMainWindow()
    ui.setupUi(main_window)
    #fffff
    # 显示主窗口
    main_window.show()
    
    # 进入应用程序主循环
    sys.exit(app.exec_())


