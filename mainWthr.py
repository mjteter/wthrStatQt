# always seem to need this
import sys
import os

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import mainwindow_auto
import getWeatherData

from threading import Thread
import time
from PyQt5.QtGui import *
# from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import QRect


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.setAttribute(PyQt5.QtCore.Qt.WA_DeleteOnClose)

        self.startTimeCur = 0
        self.startTimeFor = 0

        self.oldX = 10000
        self.oldXtime = 0

        self.lblWthrIcon.setPixmap(QPixmap(os.getcwd() + '/resources/icons/partlycloudy1.png'))

        self.cbxCurDataStat.addItem('West Chester: KPAWESTC28')
        Thread(target=self.getWuData).start()


    def getWuData(self):
        while True:
            if time.time() - self.startTimeCur > 30:
                parsed_json = getWeatherData.getCurrentData()

                newStr = getWeatherData.data2string(parsed_json, 'temp_f')
                self.resetFontSize(self.lblCurDataBig, newStr)

                getWeatherData.getRadar()
                self.lblRdrImg.setPixmap(QPixmap(os.getcwd() + '/resources/temp/radar.gif'))

                self.startTimeCur = time.time()



    def mouseMoveEvent(self, event):  # moves pages on swipe!
        margin = 140
        if event.x() < margin or event.x() > (320 - margin):
            # print('current:', event.x(), 'old:', self.oldX)
            if time.time() - self.oldXtime < 0.2:
                if abs(event.x() - self.oldX) > (100):
                    # print("swipe time:", time.time() - self.oldXtime)
                    # print('current:', event.x(), 'old:', self.oldX)

                    curInd = self.stkMain.currentIndex()
                    if event.x() - self.oldX > 0:
                        self.stkMain.setCurrentIndex((curInd - 1) % self.stkMain.count())  # left to right
                    else:
                        self.stkMain.setCurrentIndex((curInd + 1) % self.stkMain.count())  # right to left

                    self.oldX = 10000
                    self.oldXtime = 0
                else:
                    pass
            else:
                self.oldX = event.x()
                self.oldXtime = time.time()


    def resetFontSize(self, qLabel, data_str):
        if type(qLabel) != QLabel:
            return False

        lblFont = QFont(qLabel.font())
        # print("lblFont set")
        # lblFont.setPointSize(lblFont.pointSize() + 18)
        fit = False
        fm = QFontMetrics(lblFont)
        bound = QRect(fm.boundingRect(data_str))

        if (bound.width() > qLabel.width() or bound.height() > qLabel.height()):
            # must shrink
            while not fit:
                fm = QFontMetrics(lblFont)
                bound = QRect(fm.boundingRect(data_str))

                if bound.width() < qLabel.width() and bound.height() < qLabel.height():
                    fit = True
                else:
                    lblFont.setPointSize(lblFont.pointSize() - 1)
        else:
            # must expand
            while not fit:
                fm = QFontMetrics(lblFont)
                bound = QRect(fm.boundingRect(data_str))

                if bound.width() > qLabel.width() or bound.height() > qLabel.height():
                    fit = True
                else:
                    lblFont.setPointSize(lblFont.pointSize() + 1)

            lblFont.setPointSize(lblFont.pointSize() - 1)
        qLabel.setFont(lblFont)
        qLabel.setText(data_str)
        return True


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setWindowFlags(PyQt5.QtCore.Qt.CustomizeWindowHint)  # turns off frame
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
