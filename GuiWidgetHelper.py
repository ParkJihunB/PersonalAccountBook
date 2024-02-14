
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

def createPushBtn(name, func):
	btn = QPushButton(name)
	btn.clicked.connect(func)
	return btn

def createLineEdit(limit = None):
	line_edit = QLineEdit()
	if limit != None: line_edit.setValidator(limit)
	return line_edit

def createHbox(items = []):
	hbox = QHBoxLayout()
	for item in items:
		if item.isWidgetType():
			hbox.addWidget(item)
		else: hbox.addLayout(item)
	return hbox

def createLabelAndLineEditLayout(label_content:str,limit):
	label = QLabel(label_content)
	line_edit = createLineEdit(limit)

	hbox = QHBoxLayout()
	hbox.addWidget(label)
	hbox.addWidget(line_edit)
	return hbox
