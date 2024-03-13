from DataManager import DataManager
from CategoryManager import CategoryManager
from Book import Book
from Deal import Deal
from ComfortAccoutBook import ComfortAccoutBook

class AccountBook():
    def __init__(self) -> None:
        self.dataM = DataManager()
        self.book = Book()
        self.categoryM = CategoryManager(self.dataM.jsonM.load_data_file("Category.json"))
        self.__link_comfort_accountBook()
        self.__load_data()

    def call_data_by_date(self,year_,month_,day_):
        return self.book.call_data_by_date(year_,month_,day_)
        
    def __link_comfort_accountBook(self):
        cab = ComfortAccoutBook(self.dataM.csvM.open_file_to_dict("comfort_data.csv"))
        for deal in cab.deal_list:
            self.add_deal(deal)
        self.__save_data()

    def __load_data(self):
        deal_list = self.dataM.load_data_to_deal_list()
        for deal in deal_list:
            self.add_deal(deal)

    def __save_data(self): #데이터 저장은 자동으로
        #TODO: 데이터 저장은 데이터 변경될 때 마다 자동 업데이트 가능?
        current_data = self.dataM.save_data_as_json(self.book.get_data_as_list(),"")
    
    def add_deal(self,new_deal):
        self.book.send_data(new_deal)

    def get_linked_data(self): #코드 좆같이 짜놨네
        linked_data = self.dataM.get_linked_data()
        for data in linked_data:
            self.add_deal(data["year"],data["month"],data["day"],data["hour"],data["minute"],data["amount"])
