from DateTime import DateTime

class Deal():
	def __init__(self,) -> None:
		self.amount = 0 #금액
		self.dt = DateTime() #시간
		self.content = "" #내용
		self.types = [] #대분류
		self.sub_types = {}

		self.__set_types()

	def __set_types(self):
		for item in self.types:
			self.sub_types[item] = [item+"-소분류1",item+"-소분류2"]

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
		if self.type != data.type: return False
		if self.dt.check_same(data.dt) == False: return False
		if self.amount != data.amount: return False
		return True