from Day import Day
from Calender import Calender

class Month(Calender):
    def __init__(self,index:int) -> None:
        self.index = index #현재 월
        super().__init__()
            
    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Day(sub_index)

    def call_data_by_date(self,year_,month_,day_):
        if day_ in self.sub_date: return self.sub_date[day_].call_data_by_date(year_,month_,day_)
        return None
    
    def get_sub_index_from_deal(self, deal):
        return deal.dt.day
    