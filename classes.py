class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self,marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
         print('Maquina está escrevendo...')

####################################################
#Agregracao

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  #recebe objetos

    def inserir_produto(self,produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor

##################################################
#Composição

class Cliente:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self,cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def inform_cliente(self):
        print(self.nome, self.idade)

    def __del__(self):
        print(f'{self.nome} foi apagado.')

class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado.')
