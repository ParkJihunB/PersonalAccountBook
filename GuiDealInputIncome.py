from GuiDealInput import GuiDealInput

class GuiDealInputIncome(GuiDealInput):
    def __init__(self,categoryM) -> None:
        super().__init__(categoryM)
        self.tab_name = "Income"

    def get_current_category(self): #deal의 종류에 따라 다르다
        self.current_cat = self.categoryM.income_cat