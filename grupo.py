n_grupos = int(input())
grupos = {}
for _ in range(n_grupos):
    grupo, vagas = input().split()
    grupos[grupo] = int(vagas)

participantes = int(input())
selecionados = []
eliminados = []
dados = []

# Ler entradas
entrada = [input() for _ in range(participantes)]
entrada = [e.split() for e in entrada]
for i in entrada: print(i)

for e in entrada:
    dado = {}
    dado["Nome"] = e[0]
    dado["Nota"] = float(e[1])
    dado["Grupo"] = e[2]
    dados.append(dado)

# Selecionar pessoas dos demais grupos
for grupo in grupos:
    print(grupo, grupos[grupo])
    vagas = 0
    for dado in dados:
        if vagas == grupos[grupo]:
            break
        print(dado["Nome"], dado["Nota"], dado["Grupo"])
        if grupo == "G" or dado["Grupo"] == grupo:
            selecionados.append(dado["Nome"])
            eliminados.append(dado)
            vagas += 1
            continue
    for eliminado in eliminados:
        dados.remove(eliminado)
    eliminados.clear()

for selecionado in sorted(selecionados):
    print(selecionado)