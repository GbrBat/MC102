valor = float(input())
taxa = float(input())
meses = int(input())

montante = 0
atual = 0
while atual < meses:
    montante = valor * (1 + taxa)
    capital = montante + float(input())
    while capital < 0:
        print("Valor inválido no mês {}. Tente novamente.".format(atual))
        capital = montante + float(input())
    atual += 1
    valor = capital

print("O total após {} meses é de R$ {:.2f}.".format(meses, valor))