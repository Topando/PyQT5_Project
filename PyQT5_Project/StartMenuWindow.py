# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartMenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartMenu(object):
    def setupUi(self, StartMenu):
        StartMenu.setObjectName("StartMenu")
        StartMenu.resize(573, 446)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        StartMenu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(StartMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 591, 131))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 191, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 350, 191, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 280, 191, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        StartMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 25))
        self.menubar.setObjectName("menubar")
        StartMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartMenu)
        self.statusbar.setObjectName("statusbar")
        StartMenu.setStatusBar(self.statusbar)

        self.retranslateUi(StartMenu)
        QtCore.QMetaObject.connectSlotsByName(StartMenu)

    def retranslateUi(self, StartMenu):
        _translate = QtCore.QCoreApplication.translate
        StartMenu.setWindowTitle(_translate("StartMenu", "MainWindow"))
        self.label.setText(_translate("StartMenu", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">OGE MATH BOT</span></p></body></html>"))
        self.pushButton.setText(_translate("StartMenu", "Задания"))
        self.pushButton_2.setText(_translate("StartMenu", "Вариант"))
        self.pushButton_3.setText(_translate("StartMenu", "Настройки"))
        self.pushButton_4.setText(_translate("StartMenu", "Статистика"))
