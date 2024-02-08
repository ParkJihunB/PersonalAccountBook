# from AccountBook import AccountBook
# from DateTime import DateTime
# from Expense import Expense
import sys 
from PyQt5.QtWidgets import *
from GuiManager import GuiManager
# ab = AccountBook()

# dt = DateTime()
# dt.set_date(2024,1,1)
# ex = Expense()
# ab.add_deal(dt,ex)


app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()

#pyreverse -o png ./