from Year import Year

class Book():
	def __init__(self) -> None:
		self.years = []
		self.years.append(Year(2024))

<<<<<<< HEAD
	def add_deal(self,data:dict):
		self.get_year(data["year"]).add_deal(data)
=======
	def add_deal(self, date_time, deal):
		self.__get_year(date_time.year).add_deal(date_time,deal)
>>>>>>> 3202bc970e96dfb27a37ce20704b3560eebd24b4

	def __get_year(self, index:int): #맞는 년도의 year 오브젝트를 찾아줌
		for year in self.years:
			if year.index == index: return year
		return None