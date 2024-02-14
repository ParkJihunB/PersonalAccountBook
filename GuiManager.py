from GuiWidgetHelper import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
import sys
from AccountBook import AccountBook

class GuiManager(QWidget):
	current_year: int
	current_month: int
	current_day: int

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
		vbox.addLayout(self.__createDateLabelLayout())
		self.le_hour = createLineEdit(limit=QtGui.QIntValidator(self))
		self.le_minute = createLineEdit(limit=QtGui.QIntValidator(self))
		self.le_amount = createLineEdit(limit=QtGui.QIntValidator(self))
		self.btn_enter = createPushBtn("Enter",self.sendDeal)
		hour = createHbox([QLabel("시간: "),self.le_hour])
		minute  = createHbox([QLabel("분: "),self.le_minute])
		vbox.addLayout(createHbox([hour,minute]))
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
		self.current_year = date.year()
		self.current_month = date.month()
		self.current_day = date.day()
		self.year_lb.setText(str(self.current_year)+"년")
		self.month_lb.setText(str(self.current_month)+"월")
		self.date_lb.setText(str(self.current_day)+"일")

	def sendDeal(self):
		self.ac.add_deal(self.current_year,self.current_month,self.current_day,int(self.le_hour.text()),int(self.le_minute.text()),int(self.le_amount.text()))


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