from JsonManager import JsonManager
from Book import Book

class AccountBook():
	def __init__(self) -> None:
		self.jsonM = JsonManager()
		self.book = Book()

	# def add_deal(self,date_time,deal):
	# 	self.book.add_deal(date_time,deal)
	def add_deal(self,year:int,month:int,day:int,hour:int,minute:int,amount:int):
		temp_dict = {}
		temp_dict["year"] = year
		temp_dict["month"] = month
		temp_dict["day"] = day
		temp_dict["hour"] = hour
		temp_dict["minute"] = minute
		temp_dict["amount"] = amount
		self.book.add_deal(temp_dict)
	
	def sample(self): print("sample")