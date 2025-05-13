from Functions import default, ImportDir
ImportDir()

from city.create_file import CreateFile


class RegisterUser():
    def __init__(self,enterprise:str = None, *args, **kwargs):
        self._ = args
        self.id = set()
        self.name = kwargs.get("authors")
        self.data_house = kwargs.get("house")
        self.vehicle = kwargs.get("vehicle")
        self.enterprise = enterprise or None
        self.list_register_user = []
    
    def verification(self):
        ...    
    
    def register(self, name_file:str) -> None:
        id_ = (len(self.id) + 1) or 1
        self.list_register_user.append(
            default(update_data=True, file = {
                "Id": id_,
                "Local": {
                    "CEP": "12015-123",
                    "Endereço": "Rua Cristaldo",
                    "Número": 39,
                    "Adicional": "Casa C Azul"
                },
                "Others Data": None,
                "Author": {
                    "Name": "Pedro Lucas",
                    "Age": 18,
                    "Trabalho": "Programador Python"
                }
            })
        )
        self.id.add(id_)
        f = CreateFile(name_file).post(*self.list_register_user, mode='a')
        return 
    
    
    @property
    def test(self):
        print(self.list_register_user)

a = RegisterUser()
a.register('RegisterUserCity.csv')
a.test