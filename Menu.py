# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(200, 100)
        Menu.setMinimumSize(QtCore.QSize(200, 100))
        self.widget = QtWidgets.QWidget(Menu)
        self.widget.setGeometry(QtCore.QRect(10, 10, 181, 81))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.comum = QtWidgets.QPushButton(self.widget)
        self.comum.setObjectName("comum")
        self.horizontalLayout.addWidget(self.comum)

        self.cientifica = QtWidgets.QPushButton(self.widget)
        self.cientifica.setObjectName("cientifica")
        self.horizontalLayout.addWidget(self.cientifica)
        
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.titulo.setText(_translate("Menu", "MENU"))
        self.comum.setText(_translate("Menu", "COMUM"))
        self.cientifica.setText(_translate("Menu", "CIENTÍFICA"))




