from PyQt5.QtWidgets import QMessageBox

class Common(object):
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