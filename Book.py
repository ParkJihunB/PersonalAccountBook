from Year import Year
from Calender import Calender


class Book(Calender):
    def __init__(self) -> None:
        super().__init__()

    def add_sub_date(self,sub_index):
        self.sub_date[sub_index] = Year(sub_index)

    def get_sub_index_from_deal(self, deal):
        return deal.dt.year