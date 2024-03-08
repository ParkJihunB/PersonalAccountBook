from JsonManager import JsonManager
from CsvManager import CsvManager
from Expense import Expense #deal 타입
from Income import Income 
from Transfer import Transfer

class DataManager():
    def __init__(self) -> None:
        self.jsonM = JsonManager()
        self.csvM = CsvManager()
        self.data = self.jsonM.load_data()
        
    def save_data_as_json(self,data, file_name):
        self.jsonM.save_data(data, file_name)

    def load_data_to_deal_list(self):
        result = []
        for dict_data in self.jsonM.data:
            result.append(self.dict_to_deal(dict_data))
        return result
    
    def dict_to_deal(self, dict_data):
        new_deal = None
        if dict_data["type"] == "Expense":
            new_deal = Expense()
        elif dict_data["type"] == "Income":
            new_deal = Income()
        elif dict_data["type"] == "Transfer":
            new_deal = Transfer()
        else: print("strangetype")
        new_deal.set_deal_by_dict_data(dict_data)
        return new_deal

    # def save_current_data(self,book):
    # 	new_data = []
    # 	for year in book.years:
    # 		for month in year.months:
    # 			for day in month.days:
    # 				for expense in day.expenses:
    # 					new_data.append(self.deal_to_dict(expense))
    # 	result = {}
    # 	result["result"] = new_data
    # 	self.jsonM.save_data(data = new_data)
    
    # def deal_to_dict(self,deal):
    # 	result = {}
    # 	result["year"] = deal.dt.year
    # 	result["month"] = deal.dt.month
    # 	result["day"] = deal.dt.day
    # 	result["meridiem"] = deal.dt.meridiem
    # 	result["hour"] = deal.dt.hour
    # 	result["minute"] = deal.dt.minute
    # 	result["amount"] = deal.amount
    # 	return result
