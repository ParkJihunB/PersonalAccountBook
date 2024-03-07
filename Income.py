from Deal import Deal

class Income(Deal):
	def __init__(self) -> None:
		super().__init__()
		self.current_type = "Income"