from Month import Month
from Calender import Calender

class Year(Calender):
    def __init__(self,year:int) -> None:
        self.index = year
        super().__init__()

    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Month(sub_index)

    def call_data_by_date(self,year_,month_,day_):
        if month_ in self.sub_date: return self.sub_date[month_].call_data_by_date(year_,month_,day_)
        return None

    def call_data_by_month(self, year_,month_):
        if month_ in self.sub_date: return self.sub_date[month_].call_data_by_month(year_,month_)
        return None
    
    def get_sub_index_from_deal(self, deal):
        return deal.dt.month
        