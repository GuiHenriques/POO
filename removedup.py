#linhas, colunas = [int(x) for x in input().split()]
linha, colunas = 3, 3
#matriz = [[i for i in input().split()] for i in range(linhas)]
matriz = [["X","1","1"],["0",'0','1'],['1','0','1']]

caminho = str()
direction = "S"
for i in matriz: print(i)

j = matriz[0].index("X")
i = 0
#i != 0, j!= 0, i+1 < linhasMatriz, j+1 < colunasMatriz

while True:
    if direction == "S":
        if matriz[i][j-1] == "0" and j != 0:  # esquerda
            j -= 1
            direction = "O"
            caminho += "RF"
        elif matriz[i][j+1] == "0" and j < colunas:  # direita
            j += 1
            direction = "L"
            caminho += "LF"
            print(i, j)
        elif matriz[i+1][j] == "0" and i < linha:  # baixo
            i += 1
            caminho += "F"
        else: break
