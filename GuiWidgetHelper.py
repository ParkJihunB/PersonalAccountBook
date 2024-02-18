
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit,QHBoxLayout,QTabWidget,QVBoxLayout,QLabel,QCalendarWidget,QApplication

#push 버튼 위젯 만들어준다
def createPushBtn(name, func):
	btn = QPushButton(name)
	btn.clicked.connect(func)
	return btn

#라인 에딧 위젯 만들어준다
def createLineEdit(limit = None):
	line_edit = QLineEdit()
	if limit != None: line_edit.setValidator(limit)
	return line_edit

def create_tab(tab_list:list):
	tabs = QTabWidget()
	for tab in tab_list:
		tabs.addTab(QWidget(),tab)
	vbox = QVBoxLayout()
	vbox.addWidget(tabs)
	return vbox

#hbox에 위젯이나 레이아웃을 차곡차곡 넣어서 리턴해줌
def create_hbox(items = []):
	hbox = QHBoxLayout()
	for item in items:
		if item.isWidgetType():
			hbox.addWidget(item)
		else: hbox.addLayout(item)
	return hbox
