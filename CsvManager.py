import csv
class CsvManager():
	def __init__(self) -> None:
		pass

	def open_file_to_dict(self,file_name):
		f = open(file_name,'r',encoding="utf-8-sig")
		dict_data = csv.DictReader(f)
		return dict_data

	def link_comfort_ac(self):
		dict_data = self.open_file_to_dict("comfort_data.csv")