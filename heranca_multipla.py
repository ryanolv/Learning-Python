class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em B.')

class C(A):
    def falar(self):
        print('Falando... Estou em C.')

class D(C, B):    #Problema do diamante  // esquerda pra direita
    pass




