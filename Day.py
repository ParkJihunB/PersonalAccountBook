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

        self.__stat_income = 0
        self.__stat_expense = 0

    #하위 오브젝트 없어서 send 끝나고 걍 저장함
    def send_data(self,deal): 
        deal_type = deal.current_type #현재 deal의 종류를 가져온다(income,expense...)
        if deal_type in self.deals:
            if self.__check_same_data_in(deal_type,deal): return
            self.deals[deal_type].append(deal)
        self.is_new_change = True

    def get_data_as_list(self): 
        result = []
        for key in self.deals.keys(): #각각의 딜 타입에 따라
            for deal in self.deals[key]: #각각의 리스트에 deal 저장
                result.append(deal.get_data_as_dict())
        return result

    #새로운 수정사항이 있는지 확인하고 통계 정보 주는 함수
    def get_expense_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__expenses
    def get_income_state(self):
        if self.is_new_change: self.__sum_up()
        return self.__incomes
    def get_statistics_income(self):
        if self.is_new_change: self.__sum_up()
        return self.__stat_income
    def get_statistics_expense(self):
        if self.is_new_change: self.__sum_up()
        return self.__stat_expense
    
    #요청한 날짜에 맞는 데이터 제공(str로 만들어서 줌)
    def call_data_by_date(self,year_,month_,day_):
        str_result = ""
        for key in self.deals.keys(): #각각의 딜 타입에 따라
            for deal in self.deals[key]:
                str_result += str(deal)+"\n"
        return str_result

    #수정할 값이 생겼을 때만 호출
    def __sum_up(self): #통계 낸다는 뜻임
        #결국 그냥 deal 타입을 가져오는구나...
        for expense in self.deals["Expense"]:
            self.__expenses -= expense.amount
        for income in self.deals["Income"]:
            self.__incomes += income.amount
        #TODO: Transfer는 안 해도 돼?
        self.is_new_change = False #통계 다 냈으니까 더이상 또 호출할 필요 없음
    
    def __check_same_data_in(self,key_type,deal): #리스트 안에 같은 데이터가 있는지 살펴본다
        for item in self.deals[key_type]:
            if item == deal: return True
        return False