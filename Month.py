from Day import Day
from Calender import Calender
from MoneyHelper import *

class Month(Calender):
    
    __expenses = 0 #지출 총합
    __incomes = 0 #수입 총합
    
    def __init__(self,index:int) -> None:
        self.index = index #현재 월
        super().__init__()

    #새로운 수정사항이 있는지 확인하고 통계 정보 주는 함수
    def get_expense_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__expenses
    def get_income_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__incomes
    
    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Day(sub_index)

    def call_data_by_date(self,year_,month_,day_):
        if day_ in self.sub_date: return self.sub_date[day_].call_data_by_date(year_,month_,day_)
        return None
    
    def call_data_by_month(self, year_,month_):
        str_result = ""
        str_result += "총 지출: "+change_int_to_KRW_str(self.get_expense_state())+"\n"
        str_result += "총 수입: "+change_int_to_KRW_str(self.get_income_state())
        return str_result
    
    def get_sub_index_from_deal(self, deal):
        return deal.dt.day
    
    def __sum_up(self): #통계 낸다는 뜻임
        for key in self.sub_date:
            self.__expenses += self.sub_date[key].get_expense_state()
            self.__incomes += self.sub_date[key].get_income_state()
        self.is_new_change = False #통계 다 냈으니까 더이상 또 호출할 필요 없음
    