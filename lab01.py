from decimal import Decimal
num = Decimal(input())
a = int(num // 10)
b = int(num % 10)
c = int(num * 10 % 10)
d = int(num * 100 % 10)
result = str(d)+str(c)+"."+str(b)+str(a)
print("R$",result)