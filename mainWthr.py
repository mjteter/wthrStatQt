# always seem to need this
import sys
import os

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import mainwindow_auto
import getWeatherData
import getSettingsData

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
        self.setupUi(self)  # gets defined in the UI file
        self.setAttribute(PyQt5.QtCore.Qt.WA_DeleteOnClose)

        self.startTimeCur = 0  # current observations
        self.startTimeFor = 0  # short forecast
        self.startTimeRdr = 0  # radar

        self.timeoutCur = 30  # 600 for 10 mins
        self.timeoutFor = 10000  # 3600 for 1 hr
        self.timeoutRdr = 10000  # 900 for 15 mins

        self.oldX = 10000
        self.oldXtime = 0

        self.cur_label_list = [[self.lblCurDataBig, 'big', 'temp', self.lblCurNmBig, None],
                               [self.lblCurData1, '1', 'temp', self.lblCurNm1, self.lblCurUnit1],
                               [self.lblCurData2, '2', 'temp', self.lblCurNm2, self.lblCurUnit2],
                               [self.lblCurData3, '3', 'temp', self.lblCurNm3, self.lblCurUnit3],
                               [self.lblCurData4, '4', 'temp', self.lblCurNm4, self.lblCurUnit4]]
        self.cur_for_label_list = [[self.lblForData1, '1', 'high', self.lblForNm1, self.lblForUnit1],
                                   [self.lblForData2, '2', 'high', self.lblForNm2, self.lblForUnit2],
                                   [self.lblForData3, '3', 'high', self.lblForNm3, self.lblForUnit3],
                                   [self.lblForData4, '4', 'high', self.lblForNm4, self.lblForUnit4]]

        # try:
        #     wu_key = open(os.getcwd() + '/resources/keys/local.key.txt', 'r').read().strip('\n')
        # except FileNotFoundError:
        #     print("NO WU KEY FOUND!  PROGRAM WON'T RUN!")
        #     while True:
        #         pass

        self.data_handler = getWeatherData.AllWeatherData(os.getcwd() + '/resources/keys/local.key.txt')

        self.lblWthrIcon.setPixmap(QPixmap(os.getcwd() + '/resources/icons/partlycloudy1.png'))

        self.cbxCurDataStat.addItem('West Chester: KPAWESTC28')

        self.set_current_labels()
        self.set_cur_forecast_labels()

        Thread(target=self.get_wu_data).start()

    def get_wu_data(self):
        while True:
            if time.time() - self.startTimeCur > self.timeoutCur:
                self.data_handler.update_current_data()

                reset_font_size(self.cur_label_list[0][0], self.data_handler.current_data[self.cur_label_list[0][2]] +
                                ' ' + self.data_handler.get_units(self.cur_label_list[0][2]))

                for lbl_list in self.cur_label_list[1:]:
                    lbl_list[0].setText(self.data_handler.current_data[lbl_list[2]])

                self.startTimeCur = time.time()

            if time.time() - self.startTimeFor > self.timeoutFor:
                self.data_handler.update_forecast_data()

                for lbl_list in self.cur_for_label_list:
                    lbl_list[0].setText(self.data_handler.forecast_data['period1'][lbl_list[2]])

                # set labels in forecast tab

                self.startTimeFor = time.time()

            if time.time() - self.startTimeRdr > self.timeoutRdr:
                # NEED SOME SORT OF ERROR HANDLING IF IT GOES BAD
                store_loc = self.data_handler.update_radar()
                self.lblRdrImg.setPixmap(QPixmap(store_loc))
                self.startTimeRdr = time.time()

    def mouseMoveEvent(self, event):  # moves pages on swipe!
        margin = 140
        if event.x() < margin or event.x() > (320 - margin):  # MUST CHANGE THESE VALUES FOR DIFFERENT RESOLUTIONS
            # print('current:', event.x(), 'old:', self.oldX)
            if time.time() - self.oldXtime < 0.2:
                if abs(event.x() - self.oldX) > 100:  # MUST CHANGE THESE VALUES FOR DIFFERENT RESOLUTIONS
                    # print("swipe time:", time.time() - self.oldXtime)
                    # print('current:', event.x(), 'old:', self.oldX)

                    cur_ind = self.stkMain.currentIndex()
                    if event.x() - self.oldX > 0:
                        self.stkMain.setCurrentIndex((cur_ind - 1) % self.stkMain.count())  # left to right
                    else:
                        self.stkMain.setCurrentIndex((cur_ind + 1) % self.stkMain.count())  # right to left

                    self.oldX = 10000
                    self.oldXtime = 0
                else:
                    pass
            else:
                self.oldX = event.x()
                self.oldXtime = time.time()

    def set_current_labels(self):
        cur_label_dict = getSettingsData.get_label_dict()
        for lbl_list in self.cur_label_list:
            lbl_list[2] = cur_label_dict['current'][lbl_list[1]]
            lbl_list[3].setText(self.data_handler.get_data_type_str(lbl_list[2]))
            if lbl_list[4] is not None:
                lbl_list[4].setText(self.data_handler.get_units(lbl_list[2]))

    def set_cur_forecast_labels(self):
        for_label_dict = getSettingsData.get_label_dict()
        for lbl_list in self.cur_for_label_list:
            lbl_list[2] = for_label_dict['forecast'][lbl_list[1]]
            lbl_list[3].setText(self.data_handler.get_data_type_str(lbl_list[2]))
            lbl_list[4].setText(self.data_handler.get_units(lbl_list[2]))


def reset_font_size(q_label, data_str):
    if type(q_label) != QLabel:
        return False

    lbl_font = QFont(q_label.font())
    # print("lblFont set")
    # lblFont.setPointSize(lblFont.pointSize() + 18)
    fit = False
    fm = QFontMetrics(lbl_font)
    bound = QRect(fm.boundingRect(data_str))

    if bound.width() > q_label.width() or bound.height() > q_label.height():
        # must shrink
        while not fit:
            fm = QFontMetrics(lbl_font)
            bound = QRect(fm.boundingRect(data_str))

            if bound.width() < q_label.width() and bound.height() < q_label.height():
                fit = True
            else:
                lbl_font.setPointSize(lbl_font.pointSize() - 1)
    else:
        # must expand
        while not fit:
            fm = QFontMetrics(lbl_font)
            bound = QRect(fm.boundingRect(data_str))

            if bound.width() > q_label.width() or bound.height() > q_label.height():
                fit = True
            else:
                lbl_font.setPointSize(lbl_font.pointSize() + 1)

        lbl_font.setPointSize(lbl_font.pointSize() - 1)

    q_label.setFont(lbl_font)
    q_label.setText(data_str)
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
