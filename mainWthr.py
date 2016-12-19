# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import mainwindow_auto
import getWeatherData

from threading import Thread
import time
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontMetrics
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

        ### Hooks to for buttons
        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())

        Thread(target=self.getWuData).start()

    ### functions for the buttons to call
    def pressedOnButton(self):
        print("Pressed On!")

    def pressedOffButton(self):
        print("Pressed Off!")

    def getWuData(self):
        while True:
            if time.time() - self.startTimeCur > 10:
                parsed_json = getWeatherData.getCurrentData()
                newStr = getWeatherData.data2string(parsed_json, 'temp_f')

                lblFont = QFont(self.lblCurBig.font())
                # print("lblFont set")
                # lblFont.setPointSize(lblFont.pointSize() + 18)
                fit = False
                while not fit:
                    fm = QFontMetrics(lblFont)
                    # print("fm set")
                    bound = QRect(fm.boundingRect(newStr))
                    # print("bound set")
                    if (bound.width() > self.lblCurBig.width() or bound.height() > self.lblCurBig.height()):
                        fit = True
                    else:
                        lblFont.setPointSize(lblFont.pointSize() + 1)

                lblFont.setPointSize(lblFont.pointSize() - 1)
                self.lblCurBig.setFont(lblFont)
                self.lblCurBig.setText(newStr)

                # self.lblCurBig.setText(getWeatherData.data2string(parsed_json, 'temp_f'))

                self.startTimeCur = time.time()


def resetFontSize():
    pass

 
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