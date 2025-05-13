from abc import ABC, abstractmethod

class Func(ABC):
    def __init__(self):
        ...
        
        
class Vehicle(Func):
    def __init__(self):
        super().__init__()
        
    