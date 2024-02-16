from Day import Day
from Calender import Calender

class Month(Calender):
	def __init__(self,index:int) -> None:
		self.index = index #현재 월
		super().__init__()
		for i in range(1,32):
			self.add_sub_date(Day(i),i)

	def get_sub_index_from_deal(self, deal):
		return deal.dt.day
	