# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 207)
        MainWindow.setMinimumSize(QtCore.QSize(431, 207))
        MainWindow.setMaximumSize(QtCore.QSize(431, 207))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "КМЗИ"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Атбаш"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Сцитала"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Квадрат Полибия"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Цезарь"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Альберти"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Гронсфельд"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Вижинер"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Кардано"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ришелье"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Плейфер"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Вернам"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Хилл"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Гаммирование"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Частотный анализ"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Криптоанализ полиалфавитных шифров"))
        self.comboBox.setItemText(15, _translate("MainWindow", "DES"))
        self.comboBox.setItemText(16, _translate("MainWindow", "ГОСТ"))
        self.pushButton.setText(_translate("MainWindow", "ЗАШИФРОВАТЬ"))
        self.label.setText(_translate("MainWindow", "Выберите шифр:"))
        self.label_2.setText(_translate("MainWindow", "Василенко Ксения, КИ17-01"))
