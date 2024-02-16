from GuiWidgetHelper import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
import sys
from AccountBook import AccountBook
from Deal import Deal

class GuiManager(QWidget):
	select_year: int
	select_month: int
	select_day: int

	def __init__(self):
		super().__init__()
		self.ac = AccountBook()
		self.__init_window()
		self.__init_layout()

	def __init_window(self):
		self.resize(500,300)

	def __init_layout(self):
		hbox = QHBoxLayout()
		hbox.addLayout(self.__initInputLayout(),1)
		hbox.addLayout(self.__initCalenderLayout(),1)
		self.setLayout(hbox)

	def __initInputLayout(self):
		vbox = QVBoxLayout()
		self.le_hour = createLineEdit(limit=QtGui.QIntValidator(self))
		self.le_minute = createLineEdit(limit=QtGui.QIntValidator(self))
		self.le_amount = createLineEdit(limit=QtGui.QIntValidator(self))
		self.le_content = createLineEdit()
		self.btn_enter = createPushBtn("Enter",self.send_deal)
		vbox.addLayout(self.__createDateLabelLayout())
		hour = createHbox([QLabel("시간: "),self.le_hour])
		minute  = createHbox([QLabel("분: "),self.le_minute])
		vbox.addLayout(createHbox([hour,minute]))
		vbox.addLayout(createHbox([QLabel("내용: "),self.le_content]))
		vbox.addLayout(createHbox([QLabel("금액: "),self.le_amount,self.btn_enter]))
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

	def send_deal(self):
		new_deal = Deal()
		new_deal.dt.set_date(self.select_year,self.select_month,self.select_day)
		new_deal.dt.set_time(self.get_hour(),self.get_minute)
		new_deal.content = self.get_content()
		new_deal.amount = self.get_amount()
		self.ac.add_deal(new_deal)

#gui에서 데이터 가져오기
	def get_hour(self): return self.get_line_edit_text_to_int(self.le_hour)
	def get_minute(self): return self.get_line_edit_text_to_int(self.le_minute)
	def get_amount(self): return self.get_line_edit_text_to_int(self.le_amount)
	def get_content(self): return self.le_content.text()
#helper functions
	def get_line_edit_text_to_int(self,le):
		 #line edit에 적힌 값을 int로 가져온다. 값이 없을 경우 모두 0으로 통일
		if le.text() == "": return 0
		return int(le.text())

#기타 gui 함수(길어서 빼뒀음)
	#날짜 변경하면 라벨과 현재 날짜 저장하는 변수 생성
	def __createDateLabelLayout(self):
		hbox = QHBoxLayout()
		self.year_lb = QLabel("")
		self.month_lb = QLabel("")
		self.date_lb = QLabel("")
		hbox.addWidget(self.year_lb)
		hbox.addWidget(self.month_lb)
		hbox.addWidget(self.date_lb)
		return hbox

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()