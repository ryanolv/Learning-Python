class Pessoa:    # Classe mãe, superclasse
    def __init__(self, nome, idade): #não herda nada de suas subclasses
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):  #metodo para a superclasse e todas suas subclasses
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):  #Cliente herda de pessoa, ou seja, cliente é uma pessoa
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')  #metodo especifico desta classe

    def falar(self):
        print('Estou em CLIENTE.')

class ClienteVIP(Cliente):  #cadeia de heraça
    def __init__(self,nome,idade,sobrenome=''):     #sobrepondo o contrutor de pessoa
        super().__init__(nome,idade)      #repassa para Pessoa os atributos recebidos em ClienteVIP
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')


   # def falar(self):  #sobreposição de método
    #    Pessoa.falar(self)
     #   super().falar()  #niveis de hierarquia
      #  print('Outra coisa qualquer.')



class Aluno(Pessoa):  # subclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')  #metodo especifico desta classe

