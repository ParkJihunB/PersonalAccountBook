from GuiManager import GuiManager
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()

#pyreverse -o png ./