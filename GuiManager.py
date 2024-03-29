from GuiWidgetHelper import *
from GuiDealInputDialog import GuiDealInputDialog
from GuiStatistic import GuiStatistic
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon

from AccountBook import AccountBook

class GuiManager(QWidget):
    #선택된 날짜
    select_year = 0
    select_month = 0
    select_day = 0

    def __init__(self):
        super().__init__()
        self.ac = AccountBook()
        self.gui_deal = GuiDealInputDialog(self.ac.categoryM)
        self.gui_stat = GuiStatistic(self.ac)
        self.__init_window()
        self.__init_layout()

    def __init_window(self):
        pass

    def __init_layout(self):
        hbox = QHBoxLayout()
        hbox.addLayout(self.__init_date_viewer_layout())
        hbox.addLayout(self.__initCalenderLayout())
        hbox.addLayout(self.gui_stat.main_layout)
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
        self.cal.currentPageChanged.connect(self.update_page)
        self.showDate(self.cal.selectedDate()) #한번 호출 해줘야 프로그램 켰을 때 날짜 표시됨
        self.update_page()

        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        return vbox
    
#위젯과 연결된 함수
    def showDate(self, date):
        self.select_year = date.year()
        self.select_month = date.month()
        self.select_day = date.day()
        self.__set_date_label() #날짜 표시 라벨 수정
        self.__call_data_by_date() #해당 날짜의 데이터 불러오기

    def update_page(self):
        self.gui_stat.update_monthly_statistic(self.cal.yearShown(),self.cal.monthShown())

    def open_input_window(self):
        self.gui_deal.open_input_window(self.select_year,self.select_month,self.select_day)

#helper functions

#기타 gui 함수(길어서 빼뒀음)
    def __call_data_by_date(self): #날짜에 맞춰 데이터 받아서 표시
        str_data = self.ac.call_data_by_date(self.select_year,self.select_month,self.select_day)
        if str_data == None: self.date_data_lb.setText("") #데이터 없음
        else: self.date_data_lb.setText(str_data)

    def __set_date_label(self):
        self.year_lb.setText(str(self.select_year)+"년")
        self.month_lb.setText(str(self.select_month)+"월")
        self.date_lb.setText(str(self.select_day)+"일")
    #날짜 변경하면 라벨과 현재 날짜 저장하는 변수 생성
    def __create_date_label_layout(self):
        self.year_lb = QLabel("")
        self.month_lb = QLabel("")
        self.date_lb = QLabel("")
        self.date_data_lb = QLabel("ddddd")
        date_box = create_hbox([self.year_lb,self.month_lb,self.date_lb])
        return create_vbox([date_box,self.date_data_lb])

#캘린더 참고: https://wikidocs.net/38036