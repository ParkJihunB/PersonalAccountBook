
#Book, year,month 에 상속되어서 멤버 리스트의 하위 오브젝트를 찾아주는 가상 클래스
#모든 서브 데이터에는 특정 index가 있는 걸로 친다
class Calender():
    def __init__(self) -> None:
        self.sub_date = {}

    def add_sub_date(self, sub_data,sub_index):
        self.sub_date[sub_index] = sub_data
    
    def get_sub(self,sub_index):
        return self.sub_date[sub_index]
    
    def get_sub_index_from_deal(self, deal): pass
	
    def send_data(self,deal):
        self.sub_date[self.get_sub_index_from_deal(deal)].send_data(deal)
