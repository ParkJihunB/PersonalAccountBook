from JsonManager import JsonManager
from CsvManager import CsvManager

class DataManager():
	def __init__(self) -> None:
		self.jsonM = JsonManager()
		self.data = self.jsonM.load_data()
		self.link_data = self.csvM.link_comfort_ac()

	def get_linked_data(self): return self.link_data

	def save_current_data(self,book):
		new_data = []
		for year in book.years:
			for month in year.months:
				for day in month.days:
					for expense in day.expenses:
						new_data.append(self.deal_to_dict(expense))
		result = {}
		result["result"] = new_data
		self.jsonM.save_data(data = new_data)
	
	def deal_to_dict(self,deal):
		result = {}
		result["year"] = deal.dt.year
		result["month"] = deal.dt.month
		result["day"] = deal.dt.day
		result["meridiem"] = deal.dt.meridiem
		result["hour"] = deal.dt.hour
		result["minute"] = deal.dt.minute
		result["amount"] = deal.amount
		return result
