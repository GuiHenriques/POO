def find_dir(linha, posicao):
    contador = 0
    while True:
        if linha[posicao+contador] != 0:
            return linha[posicao+contador]
        contador += 1

def find_esq(linha, posicao):
    contador = 1
    while True:
        if linha[posicao-1-contador] != 0:
            return linha[posicao-contador-1]
        contador += 1

def boom(linha, posicao, dif):
    if dif > 0:
        for i in range(1, dif+1):        
            if linha[posicao-i-1] != 0:
                return True
        return False
    
    else:
        # dif = -2
        i = 1
        while i < abs(dif):
            if linha[posicao-i-1] != 0:
                return True
            i += 1
        return False
            
def game(nlinha, ncoluna, posicao):
    
    while True:
        if nlinha == ncoluna == posicao == 0:
            break

        for i in range(1, nlinha+1):
            linha = [int(i) for i in input().split()] # len = ncoluna
            
            direita = find_dir(linha, posicao)
            esquerda = find_esq(linha, posicao)
            dif = direita - esquerda
            
            if boom(linha, posicao, dif):
                return f"BOOM {nlinha} {ncoluna}"
            
            posicao -= dif
            print(dif)
            print(posicao)
            
        return f"OUT {posicao}"


nlinha, ncoluna, posicao = [int(i) for i in input().split()]
print(game(nlinha, ncoluna, posicao))
