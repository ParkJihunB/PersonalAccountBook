from Expense import Expense
from Income import Income
from Transfer import Transfer
#데이터 예시
# 날짜,자산,분류,소분류,내용,KRW,수입/지출,메모,금액,화폐,자산
# 2024/02/11 13:04:35,대구은행,문화생활,게임,스팀,66000,지출,발더게,66000,KRW,66000
# 2024/02/10 20:06:11,대구은행,문화생활,음악/도서,리디,3880,지출,던전밥,3880,KRW,3880
# 2024/02/09 16:05:09,대구은행,식비,카페,이디야,2900,지출,스콘,2900,KRW,2900
# 2024/02/09 13:27:33,대구은행,식비,카페,이디야,3900,지출,망고 요거트,3900,KRW,3900

#편한 가계부 연동하는 클래스
class ComfortAccoutBook():
    def __init__(self, data): #링크 데이터를 받아온다
        pass

    def get_data(self,data):
        #data는 딕셔너리의 리스트
        for item in data:
            deal = self.get_data_by_deal(data["수입/지출"]) #어떤 타입의 deal인지 판별

    
    def get_data_by_deal(self,type):
        if type == "지출":
            return Expense()
        if type == "수입":
            return Income()
        if type == "이체출금":
            return Transfer()
        
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
    
