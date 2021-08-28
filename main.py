from contapoucanca import ContaPoupanca
from cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('\n#########################')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)

cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)