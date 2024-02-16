from DateTime import DateTime

class Deal():
	def __init__(self) -> None:
		self.amount = 0#금액
		self.dt = DateTime() #시간
		self.content = "" #내용
	
	def check_same(self, data): 
		if self.dt.check_same(data.dt) == False: return False
		if self.amount != data.amount: return False
		return True
	
	def __eq__(self, other): #비교 연산자 오버로딩
		return self.check_same(other)