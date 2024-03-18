from GuiDealInput import GuiDealInput

#딜의 종류마다 각각의 딜에 해당되는 분류 같은 것 불러와서 콤보 박스 생성하고..
class GuiDealInputExpense(GuiDealInput):
    def __init__(self,categoryM) -> None:
        super().__init__(categoryM)
        self.tab_name = "Expense"

    def get_current_category(self): #deal의 종류에 따라 다르다
        self.current_cat = self.categoryM.expense_cat