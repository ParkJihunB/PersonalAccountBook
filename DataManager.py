from JsonManager import JsonManager
from CsvManager import CsvManager

class DataManager():
	def __init__(self) -> None:
		self.jsonM = JsonManager()
		self.csvM = CsvManager()
		self.data = self.jsonM.load_data()
		self.link_comfort_ac()


	def link_comfort_ac(self):
		backup = self.csvM.open_file_to_dict("comfort_data.csv")