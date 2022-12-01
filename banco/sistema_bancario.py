from banco import Banco

bc = Banco("Banco do Brejo", 999)

nj = bc.abre_conta("Joãozinho", 23456)
nm = bc.abre_conta("Mariazinha", 123456)

bc.deposito(nj, 100)
bc.deposito(nm, 250)
bc.saque(nj, 50)
bc.transferencia(nm, nj, 20)

print(bc.saldo(nj))
print(bc.saldo(nm))