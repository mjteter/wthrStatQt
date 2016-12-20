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
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStyleSheet("* {\n"
"    /*background-color: black;\n"
"    color: lightblue;*/\n"
"}\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.stkMain = QtWidgets.QStackedWidget(self.centralWidget)
        self.stkMain.setGeometry(QtCore.QRect(0, 0, 481, 321))
        self.stkMain.setMinimumSize(QtCore.QSize(481, 0))
        self.stkMain.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.stkMain.setObjectName("stkMain")
        self.stkPgCur = QtWidgets.QWidget()
        self.stkPgCur.setObjectName("stkPgCur")
        self.lblCurDataBig = QtWidgets.QLabel(self.stkPgCur)
        self.lblCurDataBig.setGeometry(QtCore.QRect(10, 39, 300, 121))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(45)
        self.lblCurDataBig.setFont(font)
        self.lblCurDataBig.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurDataBig.setMouseTracking(False)
        self.lblCurDataBig.setAutoFillBackground(False)
        self.lblCurDataBig.setStyleSheet("")
        self.lblCurDataBig.setScaledContents(True)
        self.lblCurDataBig.setObjectName("lblCurDataBig")
        self.frame = QtWidgets.QFrame(self.stkPgCur)
        self.frame.setGeometry(QtCore.QRect(245, 170, 225, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cbxForDataStat = QtWidgets.QComboBox(self.frame)
        self.cbxForDataStat.setGeometry(QtCore.QRect(10, 30, 205, 22))
        self.cbxForDataStat.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.cbxForDataStat.setCurrentText("")
        self.cbxForDataStat.setObjectName("cbxForDataStat")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_8.setObjectName("label_8")
        self.lblCurNm1_2 = QtWidgets.QLabel(self.frame)
        self.lblCurNm1_2.setGeometry(QtCore.QRect(10, 60, 125, 16))
        self.lblCurNm1_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_2.setFont(font)
        self.lblCurNm1_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_2.setObjectName("lblCurNm1_2")
        self.lblCurNm1_3 = QtWidgets.QLabel(self.frame)
        self.lblCurNm1_3.setGeometry(QtCore.QRect(10, 80, 125, 16))
        self.lblCurNm1_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_3.setFont(font)
        self.lblCurNm1_3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_3.setObjectName("lblCurNm1_3")
        self.lblCurNm1_4 = QtWidgets.QLabel(self.frame)
        self.lblCurNm1_4.setGeometry(QtCore.QRect(10, 100, 125, 16))
        self.lblCurNm1_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_4.setFont(font)
        self.lblCurNm1_4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_4.setObjectName("lblCurNm1_4")
        self.lblCurNm1_5 = QtWidgets.QLabel(self.frame)
        self.lblCurNm1_5.setGeometry(QtCore.QRect(10, 120, 125, 16))
        self.lblCurNm1_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_5.setFont(font)
        self.lblCurNm1_5.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_5.setObjectName("lblCurNm1_5")
        self.lblCurUnit1_5 = QtWidgets.QLabel(self.frame)
        self.lblCurUnit1_5.setGeometry(QtCore.QRect(175, 60, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_5.setFont(font)
        self.lblCurUnit1_5.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_5.setObjectName("lblCurUnit1_5")
        self.lblCurUnit1_6 = QtWidgets.QLabel(self.frame)
        self.lblCurUnit1_6.setGeometry(QtCore.QRect(175, 100, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_6.setFont(font)
        self.lblCurUnit1_6.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_6.setObjectName("lblCurUnit1_6")
        self.lblCurData1_5 = QtWidgets.QLabel(self.frame)
        self.lblCurData1_5.setGeometry(QtCore.QRect(135, 100, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_5.setFont(font)
        self.lblCurData1_5.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_5.setObjectName("lblCurData1_5")
        self.lblCurUnit1_7 = QtWidgets.QLabel(self.frame)
        self.lblCurUnit1_7.setGeometry(QtCore.QRect(175, 120, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_7.setFont(font)
        self.lblCurUnit1_7.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_7.setObjectName("lblCurUnit1_7")
        self.lblCurUnit1_8 = QtWidgets.QLabel(self.frame)
        self.lblCurUnit1_8.setGeometry(QtCore.QRect(175, 80, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_8.setFont(font)
        self.lblCurUnit1_8.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_8.setObjectName("lblCurUnit1_8")
        self.lblCurData1_6 = QtWidgets.QLabel(self.frame)
        self.lblCurData1_6.setGeometry(QtCore.QRect(135, 60, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_6.setFont(font)
        self.lblCurData1_6.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_6.setObjectName("lblCurData1_6")
        self.lblCurData1_7 = QtWidgets.QLabel(self.frame)
        self.lblCurData1_7.setGeometry(QtCore.QRect(135, 120, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_7.setFont(font)
        self.lblCurData1_7.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_7.setObjectName("lblCurData1_7")
        self.lblCurData1_8 = QtWidgets.QLabel(self.frame)
        self.lblCurData1_8.setGeometry(QtCore.QRect(135, 80, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_8.setFont(font)
        self.lblCurData1_8.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_8.setObjectName("lblCurData1_8")
        self.frame_2 = QtWidgets.QFrame(self.stkPgCur)
        self.frame_2.setGeometry(QtCore.QRect(10, 170, 225, 140))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.cbxCurDataStat = QtWidgets.QComboBox(self.frame_2)
        self.cbxCurDataStat.setGeometry(QtCore.QRect(10, 30, 205, 22))
        self.cbxCurDataStat.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.cbxCurDataStat.setCurrentText("")
        self.cbxCurDataStat.setObjectName("cbxCurDataStat")
        self.lblCurUnit1 = QtWidgets.QLabel(self.frame_2)
        self.lblCurUnit1.setGeometry(QtCore.QRect(175, 60, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1.setFont(font)
        self.lblCurUnit1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1.setObjectName("lblCurUnit1")
        self.lblCurNm1 = QtWidgets.QLabel(self.frame_2)
        self.lblCurNm1.setGeometry(QtCore.QRect(10, 60, 125, 16))
        self.lblCurNm1.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1.setFont(font)
        self.lblCurNm1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1.setObjectName("lblCurNm1")
        self.lblCurData1 = QtWidgets.QLabel(self.frame_2)
        self.lblCurData1.setGeometry(QtCore.QRect(135, 60, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1.setFont(font)
        self.lblCurData1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1.setObjectName("lblCurData1")
        self.lblCurNm1_6 = QtWidgets.QLabel(self.frame_2)
        self.lblCurNm1_6.setGeometry(QtCore.QRect(10, 80, 125, 16))
        self.lblCurNm1_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_6.setFont(font)
        self.lblCurNm1_6.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_6.setObjectName("lblCurNm1_6")
        self.lblCurNm1_7 = QtWidgets.QLabel(self.frame_2)
        self.lblCurNm1_7.setGeometry(QtCore.QRect(10, 100, 125, 16))
        self.lblCurNm1_7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_7.setFont(font)
        self.lblCurNm1_7.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_7.setObjectName("lblCurNm1_7")
        self.lblCurNm1_8 = QtWidgets.QLabel(self.frame_2)
        self.lblCurNm1_8.setGeometry(QtCore.QRect(10, 120, 125, 16))
        self.lblCurNm1_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNm1_8.setFont(font)
        self.lblCurNm1_8.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNm1_8.setObjectName("lblCurNm1_8")
        self.lblCurUnit1_2 = QtWidgets.QLabel(self.frame_2)
        self.lblCurUnit1_2.setGeometry(QtCore.QRect(175, 80, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_2.setFont(font)
        self.lblCurUnit1_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_2.setObjectName("lblCurUnit1_2")
        self.lblCurData1_2 = QtWidgets.QLabel(self.frame_2)
        self.lblCurData1_2.setGeometry(QtCore.QRect(135, 80, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_2.setFont(font)
        self.lblCurData1_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_2.setObjectName("lblCurData1_2")
        self.lblCurUnit1_3 = QtWidgets.QLabel(self.frame_2)
        self.lblCurUnit1_3.setGeometry(QtCore.QRect(175, 100, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_3.setFont(font)
        self.lblCurUnit1_3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_3.setObjectName("lblCurUnit1_3")
        self.lblCurData1_3 = QtWidgets.QLabel(self.frame_2)
        self.lblCurData1_3.setGeometry(QtCore.QRect(135, 100, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_3.setFont(font)
        self.lblCurData1_3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_3.setObjectName("lblCurData1_3")
        self.lblCurUnit1_4 = QtWidgets.QLabel(self.frame_2)
        self.lblCurUnit1_4.setGeometry(QtCore.QRect(175, 120, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurUnit1_4.setFont(font)
        self.lblCurUnit1_4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurUnit1_4.setObjectName("lblCurUnit1_4")
        self.lblCurData1_4 = QtWidgets.QLabel(self.frame_2)
        self.lblCurData1_4.setGeometry(QtCore.QRect(135, 120, 40, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurData1_4.setFont(font)
        self.lblCurData1_4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurData1_4.setObjectName("lblCurData1_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lblWthrIcon = QtWidgets.QLabel(self.stkPgCur)
        self.lblWthrIcon.setGeometry(QtCore.QRect(320, 10, 150, 150))
        self.lblWthrIcon.setText("")
        self.lblWthrIcon.setObjectName("lblWthrIcon")
        self.lblCurNmBig = QtWidgets.QLabel(self.stkPgCur)
        self.lblCurNmBig.setGeometry(QtCore.QRect(10, 10, 125, 16))
        self.lblCurNmBig.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lblCurNmBig.setFont(font)
        self.lblCurNmBig.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblCurNmBig.setTextFormat(QtCore.Qt.AutoText)
        self.lblCurNmBig.setObjectName("lblCurNmBig")
        self.frame_2.raise_()
        self.frame.raise_()
        self.lblCurDataBig.raise_()
        self.lblWthrIcon.raise_()
        self.lblCurNmBig.raise_()
        self.stkMain.addWidget(self.stkPgCur)
        self.stkPgFor = QtWidgets.QWidget()
        self.stkPgFor.setObjectName("stkPgFor")
        self.label = QtWidgets.QLabel(self.stkPgFor)
        self.label.setGeometry(QtCore.QRect(130, 80, 59, 14))
        self.label.setObjectName("label")
        self.stkMain.addWidget(self.stkPgFor)
        self.stkPgRdr = QtWidgets.QWidget()
        self.stkPgRdr.setObjectName("stkPgRdr")
        self.label_2 = QtWidgets.QLabel(self.stkPgRdr)
        self.label_2.setGeometry(QtCore.QRect(380, 220, 59, 14))
        self.label_2.setObjectName("label_2")
        self.lblRdrImg = QtWidgets.QLabel(self.stkPgRdr)
        self.lblRdrImg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.lblRdrImg.setText("")
        self.lblRdrImg.setObjectName("lblRdrImg")
        self.lblRdrImg.raise_()
        self.label_2.raise_()
        self.stkMain.addWidget(self.stkPgRdr)
        self.stkPgStg = QtWidgets.QWidget()
        self.stkPgStg.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.stkPgStg.setObjectName("stkPgStg")
        self.label_3 = QtWidgets.QLabel(self.stkPgStg)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 59, 14))
        self.label_3.setObjectName("label_3")
        self.stkMain.addWidget(self.stkPgStg)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.stkMain.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCurDataBig.setText(_translate("MainWindow", "20.4 mph"))
        self.label_8.setText(_translate("MainWindow", "Today\'s Forecast"))
        self.lblCurNm1_2.setText(_translate("MainWindow", "Temperature"))
        self.lblCurNm1_3.setText(_translate("MainWindow", "Relative Humidity"))
        self.lblCurNm1_4.setText(_translate("MainWindow", "Wind"))
        self.lblCurNm1_5.setText(_translate("MainWindow", "Feels Like"))
        self.lblCurUnit1_5.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurUnit1_6.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurData1_5.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurUnit1_7.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurUnit1_8.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurData1_6.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurData1_7.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurData1_8.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurUnit1.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurNm1.setText(_translate("MainWindow", "Pressure"))
        self.lblCurData1.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurNm1_6.setText(_translate("MainWindow", "Relative Humidity"))
        self.lblCurNm1_7.setText(_translate("MainWindow", "Wind"))
        self.lblCurNm1_8.setText(_translate("MainWindow", "Feels Like"))
        self.lblCurUnit1_2.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurData1_2.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurUnit1_3.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurData1_3.setText(_translate("MainWindow", "XX.XX"))
        self.lblCurUnit1_4.setText(_translate("MainWindow", "Btu/lb"))
        self.lblCurData1_4.setText(_translate("MainWindow", "XX.XX"))
        self.label_9.setText(_translate("MainWindow", "Current Weather"))
        self.lblCurNmBig.setText(_translate("MainWindow", "Temperature"))
        self.label.setText(_translate("MainWindow", "Forecast"))
        self.label_2.setText(_translate("MainWindow", "Radar"))
        self.label_3.setText(_translate("MainWindow", "Settings"))

