# linhas, colunas = [int(x) for x in input().split()]
linha, colunas = 5, 6
matriz = [[i for i in input().split()] for i in range(linhas)]
caminho = str()
direction = "S"
for i in matriz:
    print(i)

j = matriz[0].index("X")
i = 0
while True:
    if direction == "S":
        if matriz[i][j - 1] == "0" and j != 0:  # esquerda
            j -= 1
            direction = "O"
            caminho += "RF"
        elif matriz[i][j + 1] == "0" and j < colunas:  # direita
            j += 1
            direction = "L"
            caminho += "LF"
        elif i < linha - 1 and matriz[i + 1][j] == "0":  # baixo
            i += 1
            caminho += "F"
        else:
            break

    elif direction == "L":
        if matriz[i][j + 1] == "0" and j < colunas:  # direita
            j += 1
            caminho += "F"
        elif i < linha - 1 and matriz[i + 1][j] == "0":  # baixo
            i += 1
            direction = "S"
            caminho += "RF"
        elif matriz[i - 1][j] == "0" and i != 0:  # cima
            i -= 1
            direction = "N"
            caminho += "LF"
        else:
            break

    elif direction == "O":
        if matriz[i][j - 1] == "0" and j != 0:  # esquerda
            j -= 1
            caminho += "F"
        elif i < linha - 1 and matriz[i + 1][j] == "0":  # baixo
            i += 1
            direction = "S"
            caminho += "LF"
        elif matriz[i - 1][j] == "0" and i != 0:  # cima
            i -= 1
            direction = "N"
            caminho += "RF"
        else:
            break

    elif direction == "N":
        if matriz[i][j - 1] == "0":  # esquerda
            j -= 1
            direction = "O"
            caminho += "LF"
        elif matriz[i][j + 1] == "0":  # direita
            j += 1
            direction = "L"
            caminho += "RF"
        elif matriz[i - 1][j] == "0" and i != 0:  # cima
            i -= 1
            caminho += "F"
        else:
            break
print(caminho + "E")
