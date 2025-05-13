from abc import ABC, abstractmethod
import random
import PIL
from modelPrint import ModelPrint
from datetime import datetime

def modelCPF(*args, **kwargs):
    ...

class FunctionAuthor(ABC):
    def __init__(self):
        super().__init__()

class Author(FunctionAuthor):
    def __init__(self, name:str, age:int, sex:str, work:str, birthday:datetime, nationality:str):
        self.name = name
        self.age = age
        self.sex = sex
        self.work = work  
        self.birthday = birthday
    
    def identity(self, cpf:modelCPF, photo, email = None):
        x, y = (7, 12)
        
    def cnh(self):
        ...
        
    def armyEnlistment(self):
        ...
        
    def web(self):
        ...
        
a = Author('Pedro', 12, 'M', 'Prgramador')
a.identity(1, 1, 1, 1)