from Day import Day

class Month():
	def __init__(self,index:int) -> None:
		self.index = index
		self.days = []
		for i in range(1,32):
			self.days.append(Day(i))

	def add_deal(self,data:dict):
		self.get_day(data["day"]).add_deal(data)
		
	def get_day(self,index):
		for day in self.days:
			if day.index == index: return day
		return None