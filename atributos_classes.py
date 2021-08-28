
class A:
    vc = 123 # atributo de classe, variável disponível para
             # todas as instancias

    def __init__(self):
        self.vc = 321   #variável de instancia

a1 = A()
a2 = A()

a1.vc = 21   #não altera o valor da variavel, e sim criando um atributo direto na instancia



print(a1.vc)
print(a2.vc)
print(A.vc)