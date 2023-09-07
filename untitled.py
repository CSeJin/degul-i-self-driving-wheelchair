# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 300)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        Ui_MainPage.btn_manDriving = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainPage.btn_manDriving.sizePolicy().hasHeightForWidth())
        Ui_MainPage.btn_manDriving.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainPage.btn_manDriving.setFont(font)
        Ui_MainPage.btn_manDriving.setStyleSheet("background-color: #cfe3ac;\n"
"margin: 5px;\n"
"padding: 5px;")
        Ui_MainPage.btn_manDriving.setObjectName("btn_manDriving")
        self.gridLayout.addWidget(Ui_MainPage.btn_manDriving, 2, 1, 1, 1)
        Ui_MainPage.btn_selDes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainPage.btn_selDes.sizePolicy().hasHeightForWidth())
        Ui_MainPage.btn_selDes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainPage.btn_selDes.setFont(font)
        Ui_MainPage.btn_selDes.setStyleSheet("background-color: #cfe3ac;\n"
"margin: 5px;\n"
"padding: 5px;")
        Ui_MainPage.btn_selDes.setObjectName("btn_selDes")
        self.gridLayout.addWidget(Ui_MainPage.btn_selDes, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        Ui_MainPage.btn_emrCall = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainPage.btn_emrCall.sizePolicy().hasHeightForWidth())
        Ui_MainPage.btn_emrCall.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainPage.btn_emrCall.setFont(font)
        Ui_MainPage.btn_emrCall.setStyleSheet("background-color: #cfe3ac;\n"
"margin: 5px;\n"
"padding: 5px;")
        Ui_MainPage.btn_emrCall.setObjectName("btn_emrCall")
        self.gridLayout.addWidget(Ui_MainPage.btn_emrCall, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "홈"))
        Ui_MainPage.btn_manDriving.setText(_translate("MainWindow", "수동주행"))
        Ui_MainPage.btn_selDes.setText(_translate("MainWindow", "목적지 설정"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        Ui_MainPage.btn_emrCall.setText(_translate("MainWindow", "긴급호출"))
