class DateTime(): pass

class DateTime():
	year:int
	month:int
	day:int
	hour:int
	minute:int
	
	def __init__(self) -> None:
		pass

	def set_date(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day

	def set_time(self, hour, minute):
		self.hour = hour
		self.minute = minute

	def check_same(self,dt: DateTime):
		if self.year != dt.year: return False
		if self.month != dt.month: return False
		if self.day != dt.day: return False
		if self.hour != dt.hour: return False
		if self.minute != dt.minute: return False
		return True


