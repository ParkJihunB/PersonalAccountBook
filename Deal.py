from DateTime import DateTime

#돈이 오고가는 종류는 모두 다
class Deal():
	def __init__(self,) -> None:
		self.amount = 0 #금액
		self.dt = DateTime() #시간
		self.content = "" #내용


	def __eq__(self, other): #비교 연산자 오버로딩
		return self.__check_same(other)
	
	def __str__(self):
		str_result = ""
		str_result += str(self.dt)
		str_result += "content: " + str(self.content) + "\n"
		str_result += "amount: " + str(self.amount) + "\n"
		str_result += str(type(self))
		return str_result
	
	def __check_same(self, data): 
		if self.dt.check_same(data.dt) == False: return False
		if self.amount != data.amount: return False
		return True