from Year import Year
from Calender import Calender


class Book(Calender):
	def __init__(self) -> None:
		super().__init__()
		self.add_sub_date(Year(2024),2024)

	def get_sub_index_from_deal(self, deal):
		return deal.dt.year