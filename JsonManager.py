import json

class JsonManager():
	file_name = "data.json"
	def __init__(self) -> None:pass

	def load_data(self):
		with open(self.file_name, encoding='UTF8') as f:
			data = json.load(f)
		return data