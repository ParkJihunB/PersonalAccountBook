
class CategoryManager():
    def __init__(self,data) -> None:
        self.expense_cat = data["Expense"]
        self.income_cat = data["Income"]
        self.transfer_cat = data["Transfer"]