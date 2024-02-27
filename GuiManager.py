from GuiWidgetHelper import *
from GuiDealInputDialog import GuiDealInput
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
import sys

from AccountBook import AccountBook

class GuiManager(QWidget):
    select_year: int
    select_month: int
    select_day: int

    def __init__(self):
        super().__init__()
        self.gui_deal = GuiDealInput()
        self.ac = AccountBook()
        self.__init_window()
        self.__init_layout()

    def __init_window(self):
        pass

    def __init_layout(self):
        hbox = QHBoxLayout()
        hbox.addLayout(self.__init_date_viewer_layout(),1)
        hbox.addLayout(self.__initCalenderLayout(),1)
        self.setLayout(hbox)

    def __init_date_viewer_layout(self):
        vbox = QVBoxLayout()
        vbox.addLayout(self.__create_date_label_layout())
        vbox.addWidget(createPushBtn("데이터입력",self.open_input_window))
        return vbox

    def __initCalenderLayout(self):
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True) #날짜 사이 그리드 표시
        self.cal.clicked[QDate].connect(self.showDate) #날짜 클릭하면 show date 함수 호출
        self.showDate(self.cal.selectedDate())

        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        return vbox
    
#위젯과 연결된 함수
    def showDate(self, date):
        self.select_year = date.year()
        self.select_month = date.month()
        self.select_day = date.day()
        self.year_lb.setText(str(self.select_year)+"년")
        self.month_lb.setText(str(self.select_month)+"월")
        self.date_lb.setText(str(self.select_day)+"일")

    def open_input_window(self):
        self.gui_deal.open_input_window(self.select_year,self.select_month,self.select_day)

#helper functions


#기타 gui 함수(길어서 빼뒀음)
    #날짜 변경하면 라벨과 현재 날짜 저장하는 변수 생성
    def __create_date_label_layout(self):
        self.year_lb = QLabel("")
        self.month_lb = QLabel("")
        self.date_lb = QLabel("")
        return create_hbox([self.year_lb,self.month_lb,self.date_lb])

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()