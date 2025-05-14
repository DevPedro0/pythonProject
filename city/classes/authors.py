from abc import ABC, abstractmethod
import random
import PIL
from modelPrint import ModelPrint, _
from datetime import datetime
import regex
from Functions import addEvent

def modelCPF(*args, **kwargs) -> int:
    
    regexCPF = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    while True:
        if (regex.search(regexCPF, kwargs.get('cpf'))):
            print(f"{_()}Cadastrando com Sucesso")
            for i in range(1, 6):
                _()
            return kwargs
        
        print("Formato Inválido, Insira Novamente")
        inputIn = input("Insira Novamente um Formato: ")
        kwargs = {
            'cpf': inputIn
        }
        

class FunctionAuthor(ABC):
    def __init__(self):
        super().__init__()
        self.presence = True
        self.Event = {}
        
    def toWork(self):
        print("Trabalhando")
        self.presence = False
        
    def returnHome(self):
        self.presence = True
        ...
    
    def registerChildren(self, name, nationality, sex, birthday):
        ...
        
    def registerEvent(self, event:str, initialEvent:datetime, finallyEvent:datetime = None):
        self.presence = True
        
        addEvent(event = {event, initialEvent, finallyEvent})
        
    @staticmethod
    def children():
        ...

class Author(FunctionAuthor):
    def __init__(self, name:str, age:int, sex:str, work:str, birthday:datetime, nationality:str):
        self.name = name
        self.age = age
        self.sex = sex
        self.work = work  
        self.birthday = birthday
        self.nationality = nationality
    
    def identity(self, cpf:modelCPF, photo, email = None):
        x, y = (7, 12)
        for i in range(x):
            print(x)
        
    def cnh(self, identityAuto):
        ...
        
    def armyEnlistment(self):
        ...
        
    def web(self):
        ...
        
a = Author('Pedro', 12, 'M', 'Prgramador', '12/09/1221', 'Brasileiro')
a.identity(
    modelCPF(cpf = '155.212.516-12'),None, 'devtest@gmail.com'
)
