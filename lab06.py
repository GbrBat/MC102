# MC102W - 1s2020
# Aluno: Gabriel Batista
# RA: 212845
# Data: 03/05/2020
# Descrição: Fábrica de Cajuínas


def Classificação(i):
    return int(i * 2 / 3)


def Prensagem(x):
    if x >= 10:
        y = x * 2
    else:
        y = x * 5
    return y


def Filtragem(y):
    if y > 45:
        z = y / 10
    else:
        z = y * 8 / 9
    return int(z)


def Tratamento(z):
    a = z * 2
    return a

def Saida(instante, remessas, processos, saida):
    print("T={} | {} -> {} -> {}".format(instante, remessas, processos, saida))
    return

remessas = int(input())
n = 0
cajus = []
while n < remessas:
    remessa = int(input())
    if remessa <= 1:
        print("É necessário pelo menos dois cajus para produção de cajuína!")
        break
    else:
        cajus.append(remessa)
    n += 1

if len(cajus) == remessas:
    processos = [0, 0, 0, 0]
    saida = []
    Saida(0, cajus, processos, saida)
    for i in range(remessas+4):
        if processos[3] > 0:
            saida.append(processos[3])
        if i < remessas:
            classificados = Classificação(cajus[i])
            cajus[i] = 0
        else:
            classificados = 0
        prensados = Prensagem(processos[0])
        filtrados = Filtragem(processos[1])
        tratados = Tratamento(processos[2])

        processos[0] = classificados
        processos[1] = prensados
        processos[2] = filtrados
        processos[3] = tratados

        Saida(i+1, cajus, processos, saida)