from Expense import Expense
from Income import Income
from Transfer import Transfer

#편한 가계부 연동하는 클래스
class ComfortAccoutBook():
    def __init__(self, data): #링크 데이터를 받아온다
        self.deal_list = []
        self.get_data(data)

    def get_data(self,data):
        #data는 딕셔너리의 리스트
        for item in data:
            deal = self.get_data_by_deal(item) #각각의 deal에 따라 입력
            self.set_deal(item,deal) #공통 deal 입력
            self.deal_list.append(deal)

    def set_deal(self,item,deal): #Deal의 기본 사항 입력
        deal.amount = int(item["금액"])
        temp_dt = self.get_date_time(item["날짜"])
        deal.dt.set_date(temp_dt["year"],temp_dt["month"],temp_dt["day"])
        deal.dt.set_time(temp_dt["hour"],temp_dt["minute"])
        deal.content = item["내용"]
        deal.set_category(item["분류"],item["소분류"])

    def get_data_by_deal(self,item):
        if item["수입/지출"] == "지출":
            return self.set_expense(item)
        if item["수입/지출"] == "수입":
            return self.set_income(item)
        if item["수입/지출"] == "이체출금":
            return self.set_transfer(item)
        print("comfort account book-wrong category")

    def set_expense(self,item): 
        deal = Expense()
        #각각의 deal에 맞는 입력을 하고
        return deal
    def set_income(self,item):
        deal = Income()
        return deal
    def set_transfer(self,item):
        deal = Transfer()
        return deal
    

        
    def get_date_time(self,data):
        temp = data.split(" ")
        temp_date = temp[0].split("/")
        if len(temp) > 1: temp_time = temp[1].split(":")
        else: temp_time = [0,0,0]
        result = {}
        result["year"] = int(temp_date[0])
        result["month"] = int(temp_date[1])
        result["day"] = int(temp_date[2])
        result["hour"] = int(temp_time[0])
        result["minute"] = int(temp_time[1])
        return result

    #편한 가계부 데이터 링크 함수
    # def link_comfort_ac(self):
    # 	result = []
    # 	dict_data = self.open_file_to_dict("comfort_data.csv")
    # 	for data in dict_data:
    # 		result_dict = self.get_date_time(data["날짜"])
    # 		result_dict["amount"] = data["금액"]
    # 		result.append(result_dict)
    # 	return result
    
