import csv

class CsvManager():
	def __init__(self) -> None:
		pass

	def open_file_to_dict(self,file_name):
		f = open(file_name,'r',encoding="utf-8-sig")
		dict_data = csv.DictReader(f)
		return dict_data

	#편한 가계부 데이터 링크 함수
	# def link_comfort_ac(self):
	# 	result = []
	# 	dict_data = self.open_file_to_dict("comfort_data.csv")
	# 	for data in dict_data:
	# 		result_dict = self.get_date_time(data["날짜"])
	# 		result_dict["amount"] = data["금액"]
	# 		result.append(result_dict)
	# 	return result
	
	# def get_date_time(self,data):
	# 	temp = data.split(" ")
	# 	temp_date = temp[0].split("/")
	# 	if len(temp) > 1: temp_time = temp[1].split(":")
	# 	else: temp_time = [0,0,0]
	# 	result = {}
	# 	result["year"] = int(temp_date[0])
	# 	result["month"] = int(temp_date[1])
	# 	result["day"] = int(temp_date[2])
	# 	result["hour"] = int(temp_time[0])
	# 	result["minute"] = int(temp_time[1])
	# 	return result

