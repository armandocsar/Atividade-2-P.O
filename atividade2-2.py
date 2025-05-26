class Info:
    def __init__(self,nome,sobrenome,idade,cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

    def infoSaida(self):
        print(f"Olá,meu nome é ",self.nome, "e eu tenho", self.idade,"anos,", "meu sobrenome é",self.sobrenome , ",moro na cidade: ",self.cidade)

    
user1   = Info(input('nome 1 '),input('Sobrenome 1 '),input('Idade 1 '),input('Cidade 1 '))
user2   = Info(input('nome 2 '),input('Sobrenome 2 '),input('Idade 2 '),input('Cidade 2 '))
user3   = Info(input('nome 3 '),input('Sobrenome 3 '),input('Idade 3 '),input('Cidade 3 '))

user1.infoSaida()
user2.infoSaida()
user3.infoSaida()