from Year import Year

class Book():
	def __init__(self) -> None:
		self.years = []
		self.years.append(Year(2024))

	def add_deal(self,data:dict):
		self.__get_year(data["year"]).add_deal(data)

	def __get_year(self, index:int): #맞는 년도의 year 오브젝트를 찾아줌
		for year in self.years:
			if year.index == index: return year
		return None