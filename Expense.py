from Deal import Deal

class Expense(Deal):
    def __init__(self) -> None:
        super().__init__()
        self.current_type = "Expense"