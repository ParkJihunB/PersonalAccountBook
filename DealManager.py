from Expense import Expense
from Income import Income

class DealManager():
    def __init__(self) -> None:
        self.expenses = []
        self.incomes = []
    
    def add_deal(self,deal_data):
        if(type(deal_data) == Expense):
            self.expenses.append(deal_data)
        elif(type(deal_data) == Income):
            self.expenses.append(deal_data)
    
    def get_expense_list(self): return self.expenses