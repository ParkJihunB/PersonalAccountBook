from DataManager import DataManager
from CategoryManager import CategoryManager
from Book import Book
from Deal import Deal

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()
		self.categoryM = CategoryManager(self.dataM.jsonM.load_data_file("Category.json"))
		#self.get_linked_data()
		#self.dataM.save_current_data(self.book)

	def add_deal(self,year:int,month:int,day:int,hour:int,minute:int,amount:int):
		new_deal = Deal()
		new_deal.dt.year = year
		new_deal.dt.month = month
		new_deal.dt.day = day
		new_deal.dt.hour = hour
		new_deal.dt.minute = minute
		new_deal.amount = amount
		self.book.send_data(new_deal)
	
	def add_deal(self,new_deal):
		self.book.send_data(new_deal)

	def get_linked_data(self): #코드 좆같이 짜놨네
		linked_data = self.dataM.get_linked_data()
		for data in linked_data:
			self.add_deal(data["year"],data["month"],data["day"],data["hour"],data["minute"],data["amount"])
