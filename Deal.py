from DateTime import DateTime

class Deal():
	amount: int #금액
	def __init__(self) -> None:
		self.dateTime = DateTime() #시간
	
	def check_same(self, data): 
		if self.dateTime.check_same(data.dateTime) == False: return False
		if self.amount != data.amount: return False
		return True
	
	def __eq__(self, other): #비교 연산자 오버로딩
		return self.check_same(other)