n = int(input())
choque = False
grade = [[None for coluna in range(5)] for i in range(14)]
mapeamento = ['0730', '0820', '0910', '1010', '1100', '1330',
              '1420', '1510', '1620', '1710', '1830', '1920', '2020', '2110']

for i in range(n):
    # INE5603 218304 418302
    info = input().split()
    materia = info[0]
    
    for aula in info[1:]:
        dia = int(aula[0]) - 2
        hora = aula[1:-1]
        qtd = int(aula[-1])
    
        for i in range(qtd):
            if not grade[mapeamento.index(hora)+i][dia]:
                grade[mapeamento.index(hora)+i][dia] = materia
            else:
                choque = True
                print(grade[mapeamento.index(hora)+i][dia], materia)
                break
        if choque: break
    if choque: break
