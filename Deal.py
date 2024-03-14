from DateTime import DateTime

#돈이 오고가는 종류는 모두 다
class Deal():
    def __init__(self,) -> None:
        self.current_type = "" #현재 딜 타입(멍청하지만 필요해서 넣었음..)
        self.amount = 0 #금액
        self.dt = DateTime() #시간
        self.content = "" #내용
        self.category = ""#대분류
        self.sub_category = ""#소분류

    def set_category(self,cat,sub_cat): 
        self.category = cat
        self.sub_category = sub_cat

    def get_data_as_dict(self):
        result = {}
        result["type"] = self.current_type
        result["amount"] = self.amount
        result["dt"] = self.dt.get_data_as_dict()
        result["content"] = self.content
        result["category"] = self.category
        result["sub_category"] = self.sub_category
        return result
    
    def set_deal_by_dict_data(self,dict_deal):
        self.current_type = dict_deal["type"]
        self.amount = int(dict_deal["amount"])
        self.dt.get_dict_to_date(dict_deal["dt"])
        self.content = dict_deal["content"]
        self.category = dict_deal["category"]
        self.sub_category = dict_deal["sub_category"]
        

    def __eq__(self, other): #비교 연산자 오버로딩
        return self.__check_same(other)
    
    def __str__(self):
        str_result = ""
        str_result += str(self.content)+": "
        str_result += str(self.amount)
        # str_result += str(self.dt)
        # str_result += "content: " + str(self.content) + "\n"
        # str_result += "amount: " + str(self.amount) + "\n"
        # str_result += str(type(self))
        return str_result
    
    def __check_same(self, data): 
        if self.dt.check_same(data.dt) == False: return False
        if self.amount != data.amount: return False
        return True