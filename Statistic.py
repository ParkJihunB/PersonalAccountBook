
class Statistic():
    is_new_change = False #새로운 값이 들어옴(통계 새로 낸다->sum_up 함수 호출한다)
    expenses = 0 #지출 총합 - 그대로 값 가져가기 금지
    incomes = 0 #수입 총합

    def sum_up(self): pass
    #새로운 수정사항이 있는지 확인하고 통계 정보 주는 함수
    def get_expense_state(self):
        if self.is_new_change: self.sum_up()
        return self.expenses
    def get_income_state(self):
        if self.is_new_change: self.sum_up()
        return self.incomes
    
    