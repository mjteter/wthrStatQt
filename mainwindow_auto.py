# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnOn = QtWidgets.QPushButton(self.centralWidget)
        self.btnOn.setGeometry(QtCore.QRect(70, 190, 80, 22))
        self.btnOn.setObjectName("btnOn")
        self.btnOff = QtWidgets.QPushButton(self.centralWidget)
        self.btnOff.setGeometry(QtCore.QRect(160, 180, 80, 22))
        self.btnOff.setObjectName("btnOff")
        self.lblCurNm1 = QtWidgets.QLabel(self.centralWidget)
        self.lblCurNm1.setGeometry(QtCore.QRect(320, 10, 70, 16))
        self.lblCurNm1.setMinimumSize(QtCore.QSize(0, 0))
        self.lblCurNm1.setObjectName("lblCurNm1")
        self.lblCurBig = QtWidgets.QLabel(self.centralWidget)
        self.lblCurBig.setGeometry(QtCore.QRect(10, 10, 300, 110))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.lblCurBig.setFont(font)
        self.lblCurBig.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurBig.setMouseTracking(False)
        self.lblCurBig.setAutoFillBackground(False)
        self.lblCurBig.setStyleSheet("")
        self.lblCurBig.setScaledContents(True)
        self.lblCurBig.setObjectName("lblCurBig")
        self.lblCurData1 = QtWidgets.QLabel(self.centralWidget)
        self.lblCurData1.setGeometry(QtCore.QRect(390, 10, 40, 16))
        self.lblCurData1.setObjectName("lblCurData1")
        self.lblCurUnit1 = QtWidgets.QLabel(self.centralWidget)
        self.lblCurUnit1.setGeometry(QtCore.QRect(430, 10, 40, 16))
        self.lblCurUnit1.setObjectName("lblCurUnit1")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOn.setText(_translate("MainWindow", "On"))
        self.btnOff.setText(_translate("MainWindow", "Off"))
        self.lblCurNm1.setText(_translate("MainWindow", "Heat Index"))
        self.lblCurBig.setText(_translate("MainWindow", "20.4 mph"))
        self.lblCurData1.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurUnit1.setText(_translate("MainWindow", "Btu/lb"))

