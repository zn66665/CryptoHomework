import sys
from ui_module import LocalCryptoTool
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LocalCryptoTool.LocalCryptoWindow()
    window.show()
    sys.exit(app.exec_())
