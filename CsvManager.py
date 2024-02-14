import csv
from Deal import Deal #임시..

class CsvManager():
	def __init__(self) -> None:
		pass

	def open_file_to_dict(self,file_name):
		f = open(file_name,'r',encoding="utf-8-sig")
		dict_data = csv.DictReader(f)
		return dict_data

	#편한 가계부 데이터 링크 함수
	def link_comfort_ac(self):
		result = []
		dict_data = self.open_file_to_dict("comfort_data.csv")
		for data in dict_data:
			new_deal = Deal()
			new_deal.amount = data["금액"]
			temp_dt = self.get_date_time(data["날짜"])
			new_deal.dateTime.set_date(temp_dt[0],temp_dt[1],temp_dt[2])
			new_deal.dateTime.set_time(temp_dt[3],temp_dt[4],temp_dt[5])
			result.append(new_deal)
		return result
	
	def get_date_time(self,data):
		temp = data.split(" ")
		temp_date = temp[0].split("/")
		if len(temp) > 1: temp_time = temp[1].split(":")
		else: temp_time = [0,0,0]
		result = [int(temp_date[0]),int(temp_date[1]),int(temp_date[2]),1 if (int)(temp_time[0])>12 else 0,int(temp_time[0]),int(temp_time[1])]
		return result

