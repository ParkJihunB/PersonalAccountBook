
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

def createPushBtn(name, func):
	btn = QPushButton(name)
	btn.clicked.connect(func)
	return btn

def createLineEdit(limit=""):
	line_edit = QLineEdit()
	if limit=="": pass
	elif limit=="int": line_edit.setValidator(QtGui.QIntValidator())
	return line_edit


def createLabelAndLineEditLayout(label_content:str,limit = ""):
	label = QLabel(label_content)
	line_edit = createLineEdit(limit)

	hbox = QHBoxLayout()
	hbox.addWidget(label)
	hbox.addWidget(line_edit)
	return hbox
