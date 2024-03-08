from Day import Day
from Calender import Calender

class Month(Calender):
    def __init__(self,index:int) -> None:
        self.index = index #현재 월
        super().__init__()
            
    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Day(sub_index)
        
    def get_sub_index_from_deal(self, deal):
        return deal.dt.day
    