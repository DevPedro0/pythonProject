from abc import ABC
import modelPrint

class Contrucao(ABC):
    def __init__(self, area:float,volume:float, material:list, nicho:str, price:float, local:str, percent_tax):
        self.__area = area
        self.__volume = volume
        self.__h = None
        self.__material = material
        self.__nicho = nicho.capitalize()    
        self.__price = price
        self.__local = local
        self.__tax = percent_tax
        
    def sell():
        ...
        
    def update():
        ...
        
    def rent():
        ...
    
    def constructionPlace(self, name:str, price:float, *args ,**kwargs): 
        '''
            KWG Para Folheto de Pagamento 
            Args para Materiais da Construção
        '''
        ...
        
    def destroiyPlace(self, name:str, *args, **kwargs):
        ...
        
