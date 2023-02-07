mens =[int(i) for i in list(input())]
poli =[int(i) for i in list(input())]

tam_mens = len(mens)
tam_poli = len(poli)
tam_crc = tam_poli - 1

crc = [int(i) for i in list((tam_poli - 1) * '0')]
msg = mens + crc
for i in range(0, len(mens)):
    if msg[i] == 1:
        for k in range(0, len(poli)):
            if i+k < len(msg):
                if msg[i+k] != poli[k]:
                    msg[i+k] = 1
                else:
                    msg[i+k] = 0
for i in msg[-tam_crc:]:
    print(i,end='')
print()


