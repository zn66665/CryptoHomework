# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperSecurity.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(110, 370, 31, 31))
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(80, 60, 941, 212))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(110, 300, 31, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(180, 300, 671, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 370, 671, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(80, 420, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(80, 460, 81, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(80, 490, 941, 212))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 939, 210))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(350, 730, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(200, 420, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(340, 420, 85, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(470, 420, 111, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(680, 460, 151, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(720, 420, 85, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(820, 420, 85, 21))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_7.setGeometry(QtCore.QRect(250, 460, 85, 21))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_8.setGeometry(QtCore.QRect(550, 460, 85, 21))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_9.setGeometry(QtCore.QRect(380, 460, 85, 21))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_11.setGeometry(QtCore.QRect(620, 420, 85, 21))
        self.checkBox_11.setObjectName("checkBox_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 730, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(80, 20, 121, 31))
        self.label_6.setObjectName("label_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(80, 60, 941, 212))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 939, 210))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_3.setCenterOnScroll(False)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_3)
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_3)
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.horizontalLayout_3.addWidget(self.verticalScrollBar_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(140, 310, 31, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 310, 671, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(140, 370, 31, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 370, 671, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(100, 420, 71, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_12.setGeometry(QtCore.QRect(210, 420, 101, 21))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_13.setGeometry(QtCore.QRect(330, 420, 85, 21))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_14.setGeometry(QtCore.QRect(470, 420, 85, 21))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_15.setGeometry(QtCore.QRect(590, 420, 85, 21))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_16.setGeometry(QtCore.QRect(720, 420, 85, 21))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_17.setGeometry(QtCore.QRect(850, 420, 85, 21))
        self.checkBox_17.setObjectName("checkBox_17")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(90, 480, 71, 16))
        self.label_10.setObjectName("label_10")
        self.checkBox_18 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_18.setGeometry(QtCore.QRect(270, 460, 85, 21))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_19.setGeometry(QtCore.QRect(410, 460, 85, 21))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_39 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_39.setGeometry(QtCore.QRect(540, 460, 85, 21))
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_40 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_40.setGeometry(QtCore.QRect(670, 460, 85, 21))
        self.checkBox_40.setObjectName("checkBox_40")
        self.checkBox_41 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_41.setGeometry(QtCore.QRect(800, 460, 85, 21))
        self.checkBox_41.setObjectName("checkBox_41")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_7.setGeometry(QtCore.QRect(80, 510, 941, 212))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 939, 210))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.plainTextEdit_7.setReadOnly(True)
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.horizontalLayout_7.addWidget(self.plainTextEdit_7)
        self.verticalScrollBar_7 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_7)
        self.verticalScrollBar_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_7.setObjectName("verticalScrollBar_7")
        self.horizontalLayout_7.addWidget(self.verticalScrollBar_7)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 740, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 300, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 300, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(90, 110, 59, 15))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(90, 160, 61, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(90, 220, 59, 15))
        self.label_23.setObjectName("label_23")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 110, 113, 23))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 160, 113, 23))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 220, 113, 23))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(150, 430, 231, 31))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 560, 121, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setGeometry(QtCore.QRect(50, 430, 91, 20))
        self.label_25.setObjectName("label_25")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 210, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(720, 100, 181, 23))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(720, 150, 181, 23))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setGeometry(QtCore.QRect(610, 100, 101, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setGeometry(QtCore.QRect(630, 150, 81, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(610, 390, 121, 31))
        self.label_28.setObjectName("label_28")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 210, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_8.setGeometry(QtCore.QRect(610, 440, 391, 341))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 389, 339))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.horizontalLayout_8.addWidget(self.plainTextEdit_9)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(630, 50, 59, 15))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_5)
        self.label_30.setGeometry(QtCore.QRect(610, 260, 101, 16))
        self.label_30.setObjectName("label_30")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(720, 260, 181, 23))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(640, 310, 81, 20))
        self.label_31.setObjectName("label_31")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(722, 310, 181, 23))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_10.setGeometry(QtCore.QRect(660, 350, 101, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 350, 101, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(30, 500, 101, 20))
        self.label_32.setObjectName("label_32")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(150, 500, 231, 31))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(50, 650, 91, 20))
        self.label_33.setObjectName("label_33")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(160, 650, 231, 31))
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 710, 121, 61))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(350, 300, 111, 61))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PlainText:"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "File:"))
        self.label_4.setText(_translate("MainWindow", "Algorithm:"))
        self.label_5.setText(_translate("MainWindow", "CipherText:"))
        self.pushButton.setText(_translate("MainWindow", "Encrypto"))
        self.checkBox.setText(_translate("MainWindow", "Caesar"))
        self.checkBox_2.setText(_translate("MainWindow", "Keyword"))
        self.checkBox_3.setText(_translate("MainWindow", "Permutation "))
        self.checkBox_4.setText(_translate("MainWindow", "Double-Transposition"))
        self.checkBox_5.setText(_translate("MainWindow", "Vigenere"))
        self.checkBox_6.setText(_translate("MainWindow", "Autokey "))
        self.checkBox_7.setText(_translate("MainWindow", "Playfair "))
        self.checkBox_8.setText(_translate("MainWindow", "RSA"))
        self.checkBox_9.setText(_translate("MainWindow", "CA "))
        self.checkBox_11.setText(_translate("MainWindow", "AES"))
        self.pushButton_6.setText(_translate("MainWindow", "SendToRemote"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Encrypttion"))
        self.label_6.setText(_translate("MainWindow", "CipherText"))
        self.label_7.setText(_translate("MainWindow", "File:"))
        self.label_8.setText(_translate("MainWindow", "Key:"))
        self.label_9.setText(_translate("MainWindow", "Algorithm:"))
        self.checkBox_12.setText(_translate("MainWindow", "Caesar"))
        self.checkBox_13.setText(_translate("MainWindow", "Keyword"))
        self.checkBox_14.setText(_translate("MainWindow", "Affine"))
        self.checkBox_15.setText(_translate("MainWindow", "Multiliteral"))
        self.checkBox_16.setText(_translate("MainWindow", "Vigenere"))
        self.checkBox_17.setText(_translate("MainWindow", "Autokey "))
        self.label_10.setText(_translate("MainWindow", "PlainText:"))
        self.checkBox_18.setText(_translate("MainWindow", "Playfair "))
        self.checkBox_19.setText(_translate("MainWindow", "RC4"))
        self.checkBox_39.setText(_translate("MainWindow", "CA "))
        self.checkBox_40.setText(_translate("MainWindow", "DES"))
        self.checkBox_41.setText(_translate("MainWindow", "AES"))
        self.pushButton_3.setText(_translate("MainWindow", "Decrypto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Decryption"))
        self.pushButton_4.setText(_translate("MainWindow", "RandomGenertate"))
        self.pushButton_5.setText(_translate("MainWindow", "generatePubKey"))
        self.label_21.setText(_translate("MainWindow", "p:"))
        self.label_22.setText(_translate("MainWindow", "g:"))
        self.label_23.setText(_translate("MainWindow", "a:"))
        self.pushButton_7.setText(_translate("MainWindow", "SendPubKey"))
        self.label_25.setText(_translate("MainWindow", "LocalPubKey:"))
        self.pushButton_8.setText(_translate("MainWindow", "ConnectServer"))
        self.label_26.setText(_translate("MainWindow", "ServerAddress:"))
        self.label_27.setText(_translate("MainWindow", "ServerPort:"))
        self.label_28.setText(_translate("MainWindow", "CommunicationLog:"))
        self.pushButton_9.setText(_translate("MainWindow", "Disconnect"))
        self.label_29.setText(_translate("MainWindow", "State:"))
        self.label_30.setText(_translate("MainWindow", "ListenAddress:"))
        self.label_31.setText(_translate("MainWindow", "ListenPort:"))
        self.pushButton_10.setText(_translate("MainWindow", "StartListening"))
        self.pushButton_11.setText(_translate("MainWindow", "StopListening"))
        self.label_32.setText(_translate("MainWindow", "RemotePubKey:"))
        self.label_33.setText(_translate("MainWindow", "GeneratedKey:"))
        self.pushButton_12.setText(_translate("MainWindow", "GenerateKey"))
        self.pushButton_13.setText(_translate("MainWindow", "SendPG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "DHKeyExchange"))
