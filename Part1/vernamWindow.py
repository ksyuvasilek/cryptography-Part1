# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика\vernamWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VernamWindow(object):
    def setupUi(self, VernamWindow):
        VernamWindow.setObjectName("VernamWindow")
        VernamWindow.resize(900, 900)
        VernamWindow.setMinimumSize(QtCore.QSize(900, 900))
        VernamWindow.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget = QtWidgets.QWidget(VernamWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout.addWidget(self.plainTextEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        VernamWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VernamWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        VernamWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VernamWindow)
        self.statusbar.setObjectName("statusbar")
        VernamWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VernamWindow)
        QtCore.QMetaObject.connectSlotsByName(VernamWindow)

    def retranslateUi(self, VernamWindow):
        _translate = QtCore.QCoreApplication.translate
        VernamWindow.setWindowTitle(_translate("VernamWindow", "MainWindow"))
        self.label.setText(_translate("VernamWindow", "Введите текст:"))
        self.label_2.setText(_translate("VernamWindow", "Введите ключ:"))
        self.pushButton.setText(_translate("VernamWindow", "ЗАШИФРОВАТЬ"))
        self.pushButton_4.setText(_translate("VernamWindow", "Выгрузить в файл"))
        self.pushButton_2.setText(_translate("VernamWindow", "РАСШИФРОВАТЬ"))
        self.pushButton_3.setText(_translate("VernamWindow", "Очистить"))
