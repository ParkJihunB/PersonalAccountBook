from DataManager import DataManager
from Book import Book
from Deal import Deal

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()
		self.get_linked_data()
		#self.dataM.save_current_data(self.book)

	def add_deal(self,year:int,month:int,day:int,hour:int,minute:int,amount:int):
		new_deal = Deal()
		new_deal.dateTime.year = year
		new_deal.dateTime.month = month
		new_deal.dateTime.day = day
		new_deal.dateTime.hour = hour
		new_deal.dateTime.minute = minute
		new_deal.amount = amount
		self.book.send_data(new_deal,self.book)

	def get_linked_data(self): #코드 좆같이 짜놨네
		linked_data = self.dataM.get_linked_data()
		for data in linked_data:
			self.add_deal(data["year"],data["month"],data["day"],data["hour"],data["minute"],data["amount"])
