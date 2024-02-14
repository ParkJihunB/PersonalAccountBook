from Month import Month

class Year():
	def __init__(self,year:int) -> None:
		self.index = year
		self.months = []
		for i in range(1,13):
			self.months.append(Month(i))

	def add_deal(self,data:dict):
		self.get_month(data["month"]).add_deal(data)
		
	def get_month(self,index):
		for month in self.months:
			if month.index == index: return month
		return None