from banco import Banco

bc = Banco("Banco do Brejo", 999)

joao = bc.abre_conta("Joãozinho", 23456)
maria = bc.abre_conta("Mariazinha", 123456)

bc.deposito(joao, 100)
bc.deposito(maria, 250)
bc.saque(joao, 50)
bc.transferencia(maria, joao, 20)
print(bc.saldo_medio())
