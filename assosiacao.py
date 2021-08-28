"""
Uma classe utiliza a outra
mas são independentes entre si.
"""

from classes import Escritor, Caneta, MaquinaDeEscrever


escritor = Escritor('joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()


escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
caneta.escrever()