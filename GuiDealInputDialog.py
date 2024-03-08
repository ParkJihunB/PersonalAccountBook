from GuiWidgetHelper import *
from GuiDealInput import GuiDealInputExpense, GuiDealInputIncome, GuiDealInputTransfer
from PyQt5 import QtGui

class GuiDealInputDialog():
    def __init__(self,categoryM):
        self.select_year = 0
        self.select_month = 0
        self.select_day = 0
        #탭에 넣을 것들 딕셔너리에 넣기
        expense_tab = GuiDealInputExpense(categoryM)
        income_tab = GuiDealInputIncome(categoryM)
        transfer_tab = GuiDealInputTransfer(categoryM)
        self.tabs_dict = {
            expense_tab.tab_name: expense_tab, 
            income_tab.tab_name:income_tab, 
            transfer_tab.tab_name: transfer_tab}
        self.current_tab = expense_tab.tab_name

        self.__init_deal_tabs()
        self.__init_dialog()

    def open_input_window(self,year,month,day):
        self.select_year = year
        self.select_month = month
        self.select_day = day
        self.tab_changed(self.input_tab.currentIndex()) #새 창 열때 탭 업데이트
        self.input_dialog.show()

    def __init_deal_tabs(self):
        self.input_tab = QTabWidget()
        self.input_tab.currentChanged.connect(self.tab_changed)
        for tab_name in self.tabs_dict.keys():
            self.input_tab.addTab(self.tabs_dict[tab_name].tab_widget,tab_name)

    def __init_dialog(self):
        self.input_dialog = create_dialog(1,None) #1: 화면에 있는 모든 윈도우 창 입력 차단
        hbox = QHBoxLayout()
        hbox.addWidget(self.input_tab)
        self.input_dialog.layout = hbox
        self.input_dialog.setLayout(self.input_dialog.layout)

    def tab_changed(self,tab):
        self.current_tab = list(self.tabs_dict.keys())[tab]
        self.tabs_dict[self.current_tab].set_current_date(self.select_year,self.select_month,self.select_day)

    def send_deal_as_dict(self):
        new_deal = {}
        new_deal["type"] = self.current_tab
        new_deal["dt"] = {}
        new_deal["dt"]["year"] = self.select_year
        new_deal["dt"]["month"] = self.select_month
        new_deal["dt"]["day"] = self.select_day
        new_deal["dt"]["hour"] = self.get_hour()
        new_deal["dt"]["minute"] = self.get_minute()
        new_deal["content"] = self.get_content()
        new_deal["amount"] = self.get_amount()
        self.input_dialog.close()