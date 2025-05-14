import random

def _():
    from time import sleep
    sleep((random.randint(1, 2) / 2))
    return ''

class ModelPrint(dict):
    def __init__(self, *args, **kwargs):
        self.kwg = kwargs
    
    def modelPrintFunction(self):
        ...
        
    def modelPrintIdentity(self, x:int, y:int):
        ...
        
    def SendMessageDefault(self, msg: str, obj: str, *args, **kwargs) -> int:
        unit = 60
        sender = kwargs.get('sender', 'Desconhecido')
        receptor = kwargs.get('receptor', 'Desconhecido')
        value = kwargs.get('value', 'Indefinido')

        print(f"{_()}#" * unit)
        print(f"#{_()} {{:^56}} #".format("[INFO] -> SISTEMA INFORMA"))
        print(f"{_()}#" * unit)
        print(f"{_()}# De       : {sender}")
        print(f"{_()}# Para     : {receptor}")
        print(f"{_()}#")
        print(f"{_()}# Mensagem : {msg}")
        print(f"{_()}# Objetivo : {obj}")
        print(f"{_()}# Valor    : R$:{value}")
        print(f"{_()}#")
        print(f"{_()}# {sender} gostaria de conversar sobre '{obj}'?")
        print(f"{_()}# Se sim, entre em contato com '{kwargs.get('contact')}' para mais informações.")
        print("#" * unit)

        return_message = random.randint(1, 2)
        
        if return_message:
            print(f"[INFO] -> {receptor} irá Retornar em Breve")
            return return_message
        
        print(f"[INFO] -> {receptor} Atualmente não Se Interessa Na Oferta, Tente Novamente")
        
        return return_message
    
    def printingMachinePay(self, *args, **kwargs):
        unit = 70
        line = "#" * unit
        center = lambda text: f"# {text.center(unit - 4)} #"
        
        for k, v in kwargs.items():
            printIn = v
        
        print(line)
        print(center("RECIBO DE PAGAMENTO - INFORMAÇÕES GERAIS"))
        print(line)
        
        print(f"# ID              : {printIn.get('Id', 'N/A')}")
        print(f"# Emissor         : {printIn.get('Emissor', 'N/A')}")
        print(f"# Receptor        : {printIn.get('Receptor', 'N/A')}")
        print(f"# Data da Transação: {printIn.get('Dia', 'N/A')}")
        print(f"# Patrimônio Empresarial: R$ {printIn.get('Patrimônio Empresarial', 0):,.2f}")
        print("#")

        print(center("DESTAQUES DA NOTA"))
        nota = printIn.get('Destaques da Nota', {})
        print(f"# Valor           : R$ {nota.get('Valor', 0):,.2f}")
        print(f"# Local           : {nota.get('Local', 'N/A')}")
        print(f"# Impostos        : {nota.get('Impostos', 'N/A')}")
        print("#")

        print(center("IDENTIDADE"))
        ident = printIn.get('Identidade', {})
        print(f"# Nome            : {ident.get('Name', 'N/A')}")
        print(f"# Estado Civil    : {ident.get('Estado Civil', 'N/A')}")
        print(f"# CPF             : {ident.get('CPF', 'N/A')}")
        print(f"# Trabalho        : {ident.get('Trabalho', 'N/A')}")
        print("#")

        print(center("MEIOS DE PAGAMENTO"))
        mp = printIn.get('Meios De Pagamento', {})
        print(f"# Banco           : {mp.get('Bank', 'N/A')}")
        print(f"# Empréstimo?     : {'Sim' if mp.get('Empréstimo') else 'Não'}")
        print(f"# Parcelamento    : {mp.get('Meses de Pagamento', 0)} Meses")
        print(f"# Método          : {mp.get('Método de Pagamento', 'N/A')}")
        print("#")

        print(center("OBSERVAÇÕES"))
        print(f"# {printIn.get('Dúvidas', '')}")
        print(line)
    
    
    @property
    def DisplayInfo(self):
        print(self.keys_, self.values_)

