from datetime import datetime
import sys
import os
from pathlib import Path
import modelPrint
import shortuuid
import random

# Função para Importação sem TryException
def ImportDir():
    BASE_DIR = Path(__file__).parent.parent
    sys.path.append(os.path.dirname(BASE_DIR))
    
    return sys.path

# Filtração de Dados
def filter_():
    ...
    
# Padronização de Dados
def default(update_data:bool, *args, **kwargs):
    dataString = ["Data", "Data de Atualização"]
    if kwargs:
        for _, kwg in kwargs.items():
            data = {
                "Id": kwg.get("Id"),
                "Author":kwg.get("Author"),
                "Local":kwg.get("Local"),
                "Others Data": kwg.get("OtherData"),
                f"{dataString[-1] if update_data is True else dataString[0]}": datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            }
            
        return data
        
    return "Passe Kwargs por Favor"

def addEvent(*args, **kwargs):
    ...

class ModelPay():
    def __init__(self, method:str, bank:str, quantityMonths:int):
        self.method = method
        self.bank = bank
        self.quantityMonth = quantityMonths
        
        if quantityMonths not in [i for i in range(1, 13)]:
            print("Valor Incorreto para Meses")
            self.quantityMonth = 12
    
    def verification(self):
        ...
        
class MachinePay(ModelPay):
    def __init__(self,sender:str, receptor:str, value:float,  method, bank, quantityMonths, loan:bool):
        super().__init__(method, bank, quantityMonths)
        self.sender = sender
        self.receptor = receptor
        self.value = value
        self.loan = loan
        self.id = shortuuid.uuid()
        self.machine = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    def printing(self, value_payment_true:int = 0, *args, **kwargs) -> dict:
        for k, otherValue in kwargs.items():
            if value_payment_true:
                name_bank = otherValue.get('Banco', 'Indefinido')
                name_machine = self.machine[random.randint(0, len(self.machine))]
                
                PaySheet = {
                    'Id': self.id,
                    'Receptor': self.receptor,
                    'Emissor': self.sender,
                    'Destaques da Nota': {
                        'Valor': self.value,
                        'Local': otherValue.get('Local', 'Indefinido'),
                        'Impostos': otherValue.get('Impostos', 'Indefinido'),
                    },
                    'Identidade': { #Identidade do Author
                        'Name': otherValue.get('Name', 'Indefinido'), 
                        'Estado Civil': otherValue.get('Estado Civil', 'Indefinido'), 
                        'CPF': otherValue.get('CPF', 'Indefinido'),
                        'Trabalho': otherValue.get('Trabalho', 'Indefinido')
                    },
                    'Patrimônio Empresarial': args[0], # Dados da Empresa
                    'Dia': datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                    'Meios De Pagamento': {
                        'Bank': self.bank,
                        'Empréstimo': self.loan,
                        'Meses de Pagamento': self.quantityMonth,
                        'Método de Pagamento': self.method
                    },
                    'Dúvidas': f'Entre em Contato com {name_bank} Ou {name_machine}'
                }
                printOut = modelPrint.ModelPrint().printingMachinePay(pay = PaySheet)
                return PaySheet
            
            return f'Pagamento Não será Realizado, Receptor não Gostaria Momentaneamente Comprar '
            
    @property
    def getSendMessage(self):
        send = modelPrint.ModelPrint()
        send = send.SendMessageDefault(
            msg = f'{self.sender} Gostaria de Entrar em Contato com {self.receptor}!!', 
            obj = "Compra de Imóvel",
            contact = '211300182',
            sender = self.sender,
            receptor = self.receptor,
            value = self.value
        )
        
        return send

a = MachinePay(
    'Pedro João da Silva', 'Lucas Gabriel Pinheiro', 1299520.99, 'Crédito', 'Bradesco', 13, False
)
a.printing(
    129127.59, 12367816.13,
    note = {
        'Local': 'Rua Ipiranga 128 - João Castro',
        'Impostos': ['Jk', 'Inss', 'Ipca', 'Hlsv']
    },
    identity = {
        'Name':'João Pedro', 
        'Estado Civil': 'Solteiro', 
        'CPF': 129810,
        'Trabalho': 'Analista de Estratégias Comerciais'
    },
)