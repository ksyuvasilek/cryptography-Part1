# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика\hillWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HillWindow(object):
    def setupUi(self, HillWindow):
        HillWindow.setObjectName("HillWindow")
        HillWindow.resize(900, 900)
        HillWindow.setMinimumSize(QtCore.QSize(900, 900))
        HillWindow.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget = QtWidgets.QWidget(HillWindow)
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
        HillWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HillWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 18))
        self.menubar.setObjectName("menubar")
        HillWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HillWindow)
        self.statusbar.setObjectName("statusbar")
        HillWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HillWindow)
        QtCore.QMetaObject.connectSlotsByName(HillWindow)

    def retranslateUi(self, HillWindow):
        _translate = QtCore.QCoreApplication.translate
        HillWindow.setWindowTitle(_translate("HillWindow", "MainWindow"))
        self.label.setText(_translate("HillWindow", "Введите текст:"))
        self.label_2.setText(_translate("HillWindow", "Введите ключ:"))
        self.pushButton.setText(_translate("HillWindow", "ЗАШИФРОВАТЬ"))
        self.pushButton_2.setText(_translate("HillWindow", "РАСШИФРОВАТЬ"))
        self.pushButton_3.setText(_translate("HillWindow", "Очистить"))
