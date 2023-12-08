import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_module import Portal

# 程序的其余部分...

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


