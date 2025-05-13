from pathlib import Path
import os
import csv

BASE_DIR = Path(__file__).parent

class CreateFile():
    def __init__(self, name_file:str) -> None:
        self.name_file = name_file
        
    def post(self, value:dict, mode = 'w'):
        data = [i for i in os.listdir(BASE_DIR) if i == 'data']
        
        try:
            file = os.path.join(BASE_DIR, *data, self.name_file)
            with open(file, mode = mode, encoding='utf-8', newline='') as f:
                fields = value.keys()
                writer = csv.DictWriter(f, fieldnames=fields)
                
                
                if not os.path.getsize(file):
                    print(f"Arquivo Zerado, Inserindo Headers no Arquivo {self.name_file}")
                    writer.writeheader()
                
                writer.writerow(value)

        except Exception as e:
            raise e
            
            
