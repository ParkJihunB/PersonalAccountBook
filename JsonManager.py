import json

class JsonManager():
	file_name = "data.json"
	data = None
	def __init__(self) -> None:
		self.load_data()

	def load_data(self):
		with open(self.file_name, encoding='UTF8') as f:
			self.data = json.load(f)