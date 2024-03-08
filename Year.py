from Month import Month
from Calender import Calender

class Year(Calender):
    def __init__(self,year:int) -> None:
        self.index = year
        super().__init__()

    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Month(sub_index)
        
    def get_sub_index_from_deal(self, deal):
        return deal.dt.month
        