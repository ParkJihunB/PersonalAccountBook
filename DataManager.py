from JsonManager import JsonManager
from CsvManager import CsvManager

class DataManager():
	def __init__(self) -> None:
		self.jsonM = JsonManager()
		self.csvM = CsvManager()
		self.data = self.jsonM.load_data()

		self.csvM.link_comfort_ac()
