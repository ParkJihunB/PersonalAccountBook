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

	#일단은 expense만 가져온걸로 함
	def check_duplicate(self,date_time,deal):
		for expense in self.expenses:
			if expense.dateTime.meridiem != date_time.meridiem: continue
			if expense.dateTime.hour != date_time.hour: continue
			if expense.dateTime.minute != date_time.minute: continue
			if deal.amount != deal.amount: continue
			return True
		return False
