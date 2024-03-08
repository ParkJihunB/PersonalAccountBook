import json

class JsonManager():
    file_name = "data.json"
    def __init__(self) -> None:
        self.data = self.load_data()

    def load_data_file(self, file_name):
        with open(file_name, encoding='UTF8') as f:
            data = json.load(f)
        return data

    def load_data(self):
        with open(self.file_name, encoding='UTF8') as f:
            data = json.load(f)
        return data
    
    def save_data(self,data,file_name = ""):
        if file_name == "": file_name = self.file_name
        with open(file_name, 'w',encoding='UTF8') as f:
            json.dump(data,f,indent=4,ensure_ascii=False)