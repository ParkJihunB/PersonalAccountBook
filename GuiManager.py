
from GuiWidgetHelper import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
import sys
from AccountBook import AccountBook

class GuiManager(QWidget):
	def __init__(self):
		self.ac = AccountBook()
		self.__init_window()
		self.__init_layout()

	def __init_window(self):
		super().__init__()

	def __init_layout(self):

		hbox = QHBoxLayout()
		hbox.addLayout(self.__initCalenderLayout())
		hbox.addLayout(self.__initInputLayout())
		self.setLayout(hbox)

	def __initInputLayout(self):
		vbox = QVBoxLayout()
		vbox.addLayout(createLabelAndLineEditLayout("금액: ",limit="int"))
		return vbox


	def __initCalenderLayout(self):
		self.cal = QCalendarWidget(self)
		self.cal.setGridVisible(True) #날짜 사이 그리드 표시
		self.cal.clicked[QDate].connect(self.showDate) #날짜 클릭하면 show date 함수 호출

		self.lbl = QLabel(self)
		self.lbl = QLabel(self)
		date = self.cal.selectedDate() #현재 선택된 날짜 정보(디폴트는 현재 날짜) 라벨에 표시
		self.lbl.setText(date.toString())

		vbox = QVBoxLayout()
		vbox.addWidget(self.cal)
		vbox.addWidget(self.lbl)
		return vbox
	
#위젯과 연결된 함수
	def showDate(self, date):
		self.lbl.setText(date.toString())

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()