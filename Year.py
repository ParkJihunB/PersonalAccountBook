from Month import Month
from Calender import Calender

class Year(Calender):
	def __init__(self,year:int) -> None:
		self.index = year
		super().__init__()
		for i in range(1,13):
			self.add_sub_date(Month(i),i)

	def get_sub_index_from_deal(self, deal):
		return deal.dt.month
		