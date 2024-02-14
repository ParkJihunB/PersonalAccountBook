from DataManager import DataManager
from Book import Book
from Expense import Expense

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()
		self.get_linked_data()
		#self.dataM.save_current_data(self.book)

	def add_deal(self,year:int,month:int,day:int,hour:int,minute:int,amount:int):
		temp_dict = {}
		temp_dict["year"] = year
		temp_dict["month"] = month
		temp_dict["day"] = day
		temp_dict["meridiem"] = (1 if hour>12 else 0)
		temp_dict["hour"] = hour
		temp_dict["minute"] = minute
		temp_dict["amount"] = amount
		self.book.add_deal(temp_dict)

	def get_linked_data(self): #코드 좆같이 짜놨네
		linked_data = self.dataM.get_linked_data()
		for data in linked_data:
			self.add_deal(data["year"],data["month"],data["day"],data["hour"],data["minute"],data["amount"])
