from DataManager import DataManager
from Book import Book
from Expense import Expense

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()
		self.get_linked_data()
		self.dataM.save_current_data(self.book)

	def add_deal(self,date_time,deal):
		self.book.add_deal(date_time,deal)

	def get_linked_data(self): #코드 좆같이 짜놨네
		linked_data = self.dataM.get_linked_data()
		for data in linked_data:
			ex = Expense()
			ex.amount = data.amount
			self.add_deal(data.dateTime,ex)