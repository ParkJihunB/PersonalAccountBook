
class DateTime():
	year:int
	month:int
	day:int
	meridiem:int
	hour:int
	minute:int
	
	def __init__(self) -> None:
		pass

	def set_date(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def set_time(self,meridiem, hour, minute):
		self.meridiem = meridiem
		self.hour = hour
		self.minute = minute