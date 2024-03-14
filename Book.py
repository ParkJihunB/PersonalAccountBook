from Year import Year
from Calender import Calender


class Book(Calender):
    def __init__(self) -> None:
        super().__init__()

    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Year(sub_index)

    def call_data_by_date(self,year_,month_,day_):
        if year_ in self.sub_date: return self.sub_date[year_].call_data_by_date(year_,month_,day_)
        return None
    def call_data_by_month(self, year_,month_):
        if year_ in self.sub_date: return self.sub_date[year_].call_data_by_month(year_,month_)
        return None
    
    def get_sub_index_from_deal(self, deal):
        return deal.dt.year