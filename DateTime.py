class DateTime(): pass

class DateTime():
    year:int
    month:int
    day:int
    hour:int
    minute:int
    
    def __init__(self) -> None:
        pass

    def set_date(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def set_time(self, hour, minute):
        self.hour = hour
        self.minute = minute
        
    def get_data_as_dict(self):
        result = {}
        result["year"] = self.year
        result["month"] = self.month
        result["day"] = self.day
        result["hour"] = self.hour
        result["minute"] = self.minute
        return result
    
    def get_dict_to_date(self,dict_date):
        self.year = dict_date["year"]
        self.month = dict_date["month"]
        self.day = dict_date["day"]
        self.hour = dict_date["hour"]
        self.minute = dict_date["minute"]

    def check_same(self,dt: DateTime):
        if self.year != dt.year: return False
        if self.month != dt.month: return False
        if self.day != dt.day: return False
        if self.hour != dt.hour: return False
        if self.minute != dt.minute: return False
        return True
    
    def __str__(self):
        result_str = ""
        result_str += "year: " + str(self.year) + "\n"
        result_str += "month: " + str(self.month) + "\n"
        result_str += "day: " + str(self.day) + "\n"
        result_str += "hour: " + str(self.hour) + "\n"
        result_str += "minute: " + str(self.minute) + "\n"
        return result_str


