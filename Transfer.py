from Deal import Deal

class Transfer(Deal):
    def __init__(self) -> None:
        super().__init__()
        self.current_type = "Transfer"
        self.withdrawl_account = None #TODO: 자산 클래스 만들어야 함
        self.deposit_account = None