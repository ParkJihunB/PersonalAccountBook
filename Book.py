from Year import Year

class Book():
	def __init__(self) -> None:
		self.years = []
		self.years.append(Year(2024))

	def add_deal(self, date_time, deal):
		self.get_year(date_time.year).add_deal(date_time,deal)

	def get_year(self, index:int): #맞는 년도의 year 오브젝트를 찾아줌
		for year in self.years:
			if year.index == index: return year
		return None