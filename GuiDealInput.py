from GuiWidgetHelper import *
from PyQt5 import QtGui

class GuiDealInput(): #deal에 공통으로 들어가는 위젯 생성
    def __init__(self) -> None:
        self.tab_name = ""
        self.tab_widget = QWidget()
        self.hour = 0
        self.min = 0
        self.amount = 0
        self.content = ""
        
        self.__init_layout()
        self.tab_widget.layout = self.vbox
        self.tab_widget.setLayout(self.tab_widget.layout)

    def set_current_date(self,year_,month_,day_):
        self.year = year_
        self.month = month_
        self.day = day_
        self.lb_date.setText((str)(year_)+"년 "+(str)(month_)+"월 "+(str)(day_)+"일")
        
    def __init_layout(self):
        self.lb_date = QLabel("")
        self.le_hour = createLineEdit(limit=QtGui.QIntValidator())
        self.le_minute = createLineEdit(limit=QtGui.QIntValidator())
        self.le_amount = createLineEdit(limit=QtGui.QIntValidator())
        self.le_content = createLineEdit()
        #self.btn_enter = createPushBtn("Enter",self.send_deal)
        
        hour = create_hbox([QLabel("시간: "),self.le_hour])
        minute  = create_hbox([QLabel("분: "),self.le_minute])
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lb_date)
        self.vbox.addLayout(create_hbox([hour,minute]))
        self.vbox.addLayout(create_hbox([QLabel("금액: "),self.le_amount]))
        self.vbox.addLayout(create_hbox([QLabel("내용: "),self.le_content]))
        #self.vbox.addWidget(self.btn_enter)
#gui에서 데이터 가져오기
    def get_hour(self): return self.get_line_edit_text_to_int(self.le_hour)
    def get_minute(self): return self.get_line_edit_text_to_int(self.le_minute)
    def get_amount(self): return self.get_line_edit_text_to_int(self.le_amount)
    def get_content(self): return self.le_content.text()

        #line edit에 적힌 값을 int로 가져온다. 값이 없을 경우 모두 0으로 통일
    def get_line_edit_text_to_int(self,le):
        if le.text() == "": return 0
        return int(le.text())
    

#딜의 종류마다 각각의 딜에 해당되는 분류 같은 것 불러와서 콤보 박스 생성하고..
class GuiDealInputExpense(GuiDealInput):
    def __init__(self) -> None:
        super().__init__()
        self.tab_name = "Expense"

class GuiDealInputIncome(GuiDealInput):
    def __init__(self) -> None:
        super().__init__()
        self.tab_name = "Income"

class GuiDealInputTransfer(GuiDealInput):
    def __init__(self) -> None:
        super().__init__()
        self.tab_name = "Transfer"