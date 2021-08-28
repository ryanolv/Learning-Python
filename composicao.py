"""
Uma classe é dona de objetos
de outra classe.
"""

from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.inform_cliente()
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.inform_cliente()
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Joao', 19)
cliente3.insere_endereco('Sao Paulo', 'SP')
cliente3.inform_cliente()
cliente3.lista_enderecos()
del cliente3
print()

print('############################################################')