from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__nome


class Cliente(Pessoa):
    def __init__(self,nome,idade,conta):
        super().__init__(nome,idade)
        self.conta = conta


