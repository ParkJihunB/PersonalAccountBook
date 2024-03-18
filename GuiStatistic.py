from GuiWidgetHelper import *

#통계 페이지 오른쪽에 간략하게 표시/추가 통계 창 띄우는 버튼
class GuiStatistic(QWidget):
    def __init__(self,ac):
        super().__init__()
        self.ac = ac
        self.current_year = 0
        self.current_month = 0
        self.__init_main_layout()

    def __init_main_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.__init_simple_statistic())

    def update_monthly_statistic(self,year_,month_):
        self.current_year = year_
        self.current_month = month_
        self.month_lb.setText(str(self.current_year)+"년 " +str(self.current_month)+"월")
        self.__set_current_monthly_data()

    def __set_current_monthly_data(self):
        str_data = self.ac.call_data_by_month( self.current_year, self.current_month)
        if str_data == None: 
            self.monthly_incomes_lb.setText("총 수입: 0")
            self.monthly_expenses_lb.setText("총 지출: 0")
        else: self.monthly_incomes_lb.setText(str_data)

    #오른쪽 페이지에 넣을 간단한 통계 데이터
    def __init_simple_statistic(self):
        simple_static_layout = QVBoxLayout()
        self.month_lb = QLabel(str(self.current_year)+"년 " +str(self.current_month)+"월")
        self.monthly_incomes_lb = QLabel("총 수입")
        self.monthly_expenses_lb = QLabel("총 지출")
        
        simple_static_layout.addWidget(self.month_lb)
        simple_static_layout.addWidget(self.monthly_incomes_lb)
        simple_static_layout.addWidget(self.monthly_expenses_lb)
        return simple_static_layout
    