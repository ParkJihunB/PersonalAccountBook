from Calender import Calender

class Day(Calender):
    #모든 deal의 종류를 넣어둘 것!
    def __init__(self,index:int) -> None:
        super().__init__()
        self.index = index #현재 날짜
        self.deals = {"Expense":[],
                      "Income": [],
                      "Transfer": []} #deal의 종류에 따라 추가될 것이다

        self.is_new_change = False #새로운 값이 들어옴(통계 새로 낸다->sum_up 함수 호출한다)
        self.__expenses = 0 #지출 총합
        self.__incomes = 0 #수입 총합

    #하위 오브젝트 없어서 send 끝나고 걍 저장함
    def send_data(self,deal): 
        deal_type = deal.current_type #현재 deal의 종류를 가져온다(income,expense...)
        if deal_type in self.deals:
            self.deals[deal_type].append(deal)
        self.is_new_change = True

    #새로운 수정사항이 있는지 확인하고 통계 정보 주는 함수
    def get_expense_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__expenses
    def get_income_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__incomes
    
    #수정할 값이 생겼을 때만 호출
    def __sum_up(self): #통계 낸다는 뜻임
        #결국 그냥 deal 타입을 가져오는구나...
        for expense in self.deals["Expense"]:
            self.__expenses -= expense.amount
        for income in self.deals["Income"]:
            self.__incomes += income.amount
        #TODO: Transfer는 안 해도 돼?
        self.is_new_change = False #통계 다 냈으니까 더이상 또 호출할 필요 없음

    def get_sub_index_from_deal(self, deal):
        return None

    #일단은 expense만 가져온걸로 함
    def check_same(self,date_time,deal):
        for expense in self.dealM.get_expense_list():
            if expense == deal: return True
        return False
