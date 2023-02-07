nome = input()
horas = float(input())
valor = float(input())
base = valor * 8 * 22
extra = horas - 8
caso1 = extra * valor * 1.25 * 22 + base
caso2 = extra * valor * 1.5 * 22 + base
if 8 <= horas <= 14:
    if horas <= 12:
        print("O salário do(a) funcionário(a) {} será de R${:.2f} para esse mês".format(nome,caso1));
    else:
        print("O salário do(a) funcionário(a) {} será de R${:.2f} para esse mês".format(nome,caso2));
else:
    print("Número de horas diárias não admitido")