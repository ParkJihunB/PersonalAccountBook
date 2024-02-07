from AccountBook import AccountBook
from DateTime import DateTime
from Expense import Expense

ab = AccountBook()

dt = DateTime()
dt.set_date(2024,1,1)
ex = Expense()
ab.add_deal(dt,ex)
#pyreverse -o png ./