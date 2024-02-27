from GuiWidgetHelper import *
from PyQt5 import QtGui
from Expense import Expense #deal 타입
from Income import Income 
from Transfer import Transfer

class GuiDealInputDialog():
    def __init__(self):
        tab_list = ["Expense","Income","Transfer"]
        self.tabs_dict = {}
        for tab in tab_list: self.tabs_dict[tab] = QWidget()
        self.current_type = tab_list[0]
        self.__init_input_dialog()

    def open_input_window(self,year,month,day):
        self.select_year = year
        self.select_month = month
        self.select_day = day
        self.lb_date.setText(str(self.select_year)+"년 "+str(self.select_month)+"월 "+str(self.select_day)+"일 ")
        self.input_dialog.show()
        

    def __init_input_dialog(self):
        self.input_dialog = create_dialog(1,None) #1: 화면에 있는 모든 윈도우 창 입력 차단
        hbox = QHBoxLayout()
        hbox.addWidget(self.__init_input_layout())
        self.input_dialog.layout = hbox
        self.input_dialog.setLayout(self.input_dialog.layout)

    def __init_input_layout(self):
        input_tab = QTabWidget()
        input_tab.currentChanged.connect(self.tab_changed)
        for tab in self.tabs_dict.keys():
            input_tab.addTab(self.tabs_dict[tab],tab)
            self.tabs_dict[tab].layout = self.__init_input_income_layout()
            self.tabs_dict[tab].setLayout(self.tabs_dict[tab].layout)
        return input_tab
    
    def __init_input_income_layout(self):
        vbox = QVBoxLayout()
        self.lb_date = QLabel("")
        self.le_hour = createLineEdit(limit=QtGui.QIntValidator())
        self.le_minute = createLineEdit(limit=QtGui.QIntValidator())
        self.le_amount = createLineEdit(limit=QtGui.QIntValidator())
        self.le_content = createLineEdit()
        self.btn_enter = createPushBtn("Enter",self.send_deal)
        
        hour = create_hbox([QLabel("시간: "),self.le_hour])
        minute  = create_hbox([QLabel("분: "),self.le_minute])
        vbox.addWidget(self.lb_date)
        vbox.addLayout(create_hbox([hour,minute]))
        vbox.addLayout(create_hbox([QLabel("금액: "),self.le_amount]))
        vbox.addLayout(create_hbox([QLabel("내용: "),self.le_content]))
        vbox.addWidget(self.btn_enter)
        return vbox
        
    def tab_changed(self,tab):
        self.current_type = list(self.tabs_dict.keys())[tab]

    def send_deal(self):
        new_deal = None
        if self.current_type == "Expense": new_deal = Expense()
        elif self.current_type == "Income": new_deal = Income()
        elif self.current_type == "Transfer": new_deal = Transfer()
        new_deal.dt.set_date(self.select_year,self.select_month,self.select_day)
        new_deal.dt.set_time(self.get_hour(),self.get_minute())
        new_deal.content = self.get_content()
        new_deal.amount = self.get_amount()
        self.input_dialog.close()
    
#gui에서 데이터 가져오기
    def get_hour(self): return self.get_line_edit_text_to_int(self.le_hour)
    def get_minute(self): return self.get_line_edit_text_to_int(self.le_minute)
    def get_amount(self): return self.get_line_edit_text_to_int(self.le_amount)
    def get_content(self): return self.le_content.text()

    #line edit에 적힌 값을 int로 가져온다. 값이 없을 경우 모두 0으로 통일
    def get_line_edit_text_to_int(self,le):
        if le.text() == "": return 0
        return int(le.text())