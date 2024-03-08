
#Book, year,month 에 상속되어서 멤버 리스트의 하위 오브젝트를 찾아주는 가상 클래스
#모든 서브 데이터에는 특정 index가 있는 걸로 친다
class Calender():
    def __init__(self) -> None:
        self.sub_date = {}
    
    #각각의 클래스마다 하위 날짜가 다르므로 각각 만들어준다
    def add_sub_date(self,sub_index): pass
    def get_sub_index_from_deal(self, deal): pass
    
    def get_sub(self,sub_index):
        return self.sub_date[sub_index]
    
    def call_data_by_date(self,year_,month_,day_):
        pass

	#받은 데이터의 인덱스에 맞게 하위로 데이터 보내주기
    def send_data(self,deal): 
        current_index = self.get_sub_index_from_deal(deal)
        if current_index in self.sub_date: pass
        else: self.add_sub_date(current_index) #해당 인덱스가 없으면 만들어준다
        self.sub_date[current_index].send_data(deal)

    #하위 아이템들을 index에 맞춰 딕셔너리 저장
    def get_data_as_list(self):
        result = []
        for key in self.sub_date.keys():
            temp_list = self.sub_date[key].get_data_as_list()
            result = result + temp_list #date 별로 받은 리스트 다 풀어서 리스트 하나로 만든다
        return result
        # result = {}
        # for key in self.sub_date.keys(): 
        #     result[key] = self.sub_date[key].get_data_as_dict()
        # return result
