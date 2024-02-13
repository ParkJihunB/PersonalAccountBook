from DataManager import DataManager
from Book import Book

class AccountBook():
	def __init__(self) -> None:
		self.dataM = DataManager()
		self.book = Book()

	def add_deal(self,date_time,deal):
		self.book.add_deal(date_time,deal)
	
	def sample(self): print("sample")