# MC102W - 1s2020
# Aluno: Gabriel Batista
# RA: 212845
# Data: 29/05/2020
# Descrição: Respondenator 3000


from PontStop import *


def Limpeza(palavras, sinonimos):
    palavras_limp = []
    for ele in palavras:
        palavra_limpa = []
        for caracter in ele:
            if caracter not in pontuacoes:
                palavra_limpa.append(caracter)
        ele = "".join(palavra_limpa)
        for chave, valor in sinonimos.items():
            if ele in valor:
                ele = chave
        if ele not in stop_words and ele not in palavras_limp:
            palavras_limp.append(ele)
    return palavras_limp

sinonimos = {}
z = input()
if z[-1] != "}":
    y = input()
    while y != "}":
        chave = y.split(":")[0]
        valor = y.split(":")[1].split(",")
        sinonimos[chave] = valor
        y = input()
pergunta = input()
perg_simp = pergunta.lower().split()
desc_perg = Limpeza(perg_simp, sinonimos)
n = int(input())
x = 0
respostas = []
respostas_limp = []
while x < n:
     resposta = input()
     resp_simp = resposta.lower().split()
     desc_resp = Limpeza(resp_simp, sinonimos)
     respostas.append(resposta)
     respostas_limp.append(desc_resp)
     x += 1




for i in range(len(respostas_limp)):
    resp_correta = True
    for p in desc_perg:
        if p not in respostas_limp[i]:
            resp_correta = False
            break
    if resp_correta == True:
        break

if resp_correta == False or len(pergunta) == 0:
    resp_fim = 42
else:
    resp_fim = respostas[i]


print("Descritor pergunta:", ",".join(sorted(desc_perg)))
x = 0
while x < n:
    print("Descritor resposta {}:".format(x+1), ",".join(sorted(respostas_limp[x])))
    x += 1
print()
print('A resposta para a pergunta "{}" é "{}"'.format(pergunta, resp_fim))