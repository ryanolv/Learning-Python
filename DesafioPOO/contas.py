from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia, numero,saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        valor = f'R$ {valor:.2f}'
        self.__saldo = valor