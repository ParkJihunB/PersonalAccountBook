
class StatisticManager():
    file_name = "statistic.json"

    def __init__(self) -> None:
        pass

    def get_json_data(self,json_data):
        self.json_data = json_data

    def update_statistic(self,year_,month_,day):
        #새로운 데이터가 들어오면 그걸 기반으로 통계를 수정한다
        #day 하나만 들어와도 전체가 바뀌니까 년/월/일 다 수정
        #하면서 파일에 저장도 해주기
        pass

    def get_yearly_data(self,year_): pass

    def get_monthly_data(self,year_,month_): pass

    def get_daily_data(self,year_,month_,day_): pass