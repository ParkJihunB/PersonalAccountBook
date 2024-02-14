from Expense import Expense
from Income import Income

class Day():
	#모든 deal의 종류를 넣어둘 것!
	def __init__(self,index:int) -> None:
		self.index = index #현재 날짜
		self.expenses = []
		self.incomes = []

	def add_deal(self,data:dict):
		print(data)
