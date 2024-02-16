from Calender import Calender
from DealManager import DealManager

class Day(Calender):
	#모든 deal의 종류를 넣어둘 것!
	def __init__(self,index:int) -> None:
		super().__init__()
		self.index = index #현재 날짜
		self.dealM = DealManager()
		self.expenses = []
		self.incomes = []

	#하위 오브젝트 없어서 send 끝나고 걍 저장함
	def send_data(self,deal): 
		print(deal)

	def get_sub_index_from_deal(self, deal):
		return None

	#일단은 expense만 가져온걸로 함
	def check_same(self,date_time,deal):
		for expense in self.dealM.get_expense_list():
			if expense == deal: return True
		return False
