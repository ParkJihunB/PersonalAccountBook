from DataManager import DataManager
from Book import Book
from Expense import Expense

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()
		self.get_linked_data()
		self.dataM.save_current_data(self.book)

<<<<<<< HEAD
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
=======
	def add_deal(self,date_time,deal):
		self.book.add_deal(date_time,deal)

	def get_linked_data(self): #코드 좆같이 짜놨네
		linked_data = self.dataM.get_linked_data()
		for data in linked_data:
			ex = Expense()
			ex.amount = data.amount
			self.add_deal(data.dateTime,ex)
>>>>>>> 3202bc970e96dfb27a37ce20704b3560eebd24b4
