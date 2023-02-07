# MC102W - 1s2020
# Aluno: Gabriel Batista
# RA: 212845
# Data: 08/05/2020
# Descrição: Guerra 4.0


class Heroi:
    def __init__(self, nome, vida, dano, block, mana):
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.dano = dano
        self.block = block
        self.mana = mana
        self.manamax = mana
        self.drenagem = 0
        self.durains = 0
        self.custoinsano = 0
        self.duraest = 0
        self.custoestrela = 0
        self.isinsane = False
        self.isstar = False
        self.insano = 0


    def ReceberDano(self, dano, drenagem):
        self.mana = self.mana - drenagem
        if self.mana < 0:
            self.mana = 0
        if self.isstar == True:
            print('{} estava invulnerável'.format(self.nome))
            self.duraest -= 1
            if self.duraest == 0:
                self.isstar = False
            return
        self.vida = self.vida - (dano - int((dano * self.block) / 100))
        if self.vida < 0:
            self.vida = 0
        return

    def Ataque(self):
        if self.isinsane == True:
            return self.dano + self.insano
        return self.dano

    def SituacaoAtual(self):
        print("{} possui {} de vida, {} pontos mágicos, {} de dano e {}% de bloqueio".format(self.nome, str(self.vida), str(self.mana), str(self.dano), str(self.block)))
        return

    def AtualizaEfeitos(self):
        if self.isinsane == True:
            self.durains -= 1
            if self.durains == 0:
                self.isinsane = False
        return

    def Cura(self, custo, pontos):
        if self.mana >= custo:
            if self.vida + pontos <= self.vidamax:
                self.vida = self.vida + pontos
            else:
                self.vida = self.vidamax
            self.mana = self.mana - custo
            return
        print("{} não possui mana suficiente para a mágica".format(self.nome))
        return

    def Forca(self, custo, pontos):
        if self.mana >= custo:
            self.dano = self.dano + pontos
            self.mana = self.mana - custo
            return
        print("{} não possui mana suficiente para a mágica".format(self.nome))
        return

    def Protecao(self, custo, percentual):
        if self.mana >= custo:
            if self.block + percentual <= 100:
                self.block = self.block + percentual
            else:
                self.block = 100
            self.mana = self.mana - custo
            return
        print("{} não possui mana suficiente para a mágica".format(self.nome))
        return

    def Eter(self, pontos):
        if self.mana + pontos <= self.manamax:
            self.mana = self.mana + pontos
        else:
            self.mana = self.manamax
        return

    def DefinirDrenagem(self, pontos):
        if self.drenagem == 0:
            self.drenagem = pontos
        else:
            print('{} já possui a carta Drenagem'.format(self.nome))
        return

    def DefinirInsano(self, custo, n, danoad):
        if self.durains == 0:
            self.custoinsano = custo
            self.durains = n
            self.insano = danoad
        else:
            print('{} já possui a carta Insano'.format(self.nome))
        return

    def DefinirEstrela(self, custo, m):
        if self.duraest == 0:
            self.custoestrela = custo
            self.duraest = m
        else:
            print('{} já possui a carta Estrela'.format(self.nome))
        return

    def AtivarInsano(self):
        if self.durains == 0:
            print('{} não possui a carta Insano'.format(self.nome))
            return
        if self.isinsane == True:
            print('{} já ativou a carta Insano'.format(self.nome))
            return
        if self.mana >= self.custoinsano:
            self.mana = self.mana - self.custoinsano
            self.isinsane = True
            print('{} ativou a carta Insano'.format(self.nome))
            return
        print("{} não possui mana suficiente para a mágica".format(self.nome))
        return

    def AtivarEstrela(self):
        if self.duraest == 0:
            print('{} não possui a carta Estrela'.format(self.nome))
            return
        if self.isstar == True:
            print('{} já ativou a carta Estrela'.format(self.nome))
            return
        if self.mana >= self.custoestrela:
            self.mana = self.mana - self.custoestrela
            self.isstar = True
            print('{} ativou a carta Estrela'.format(self.nome))
            return
        print("{} não possui mana suficiente para a mágica".format(self.nome))
        return


def Atacar(atacante, defensor):
    if atacante.isinsane == True:
        print('{} deu um ataque insano em {}'.format(atacante.nome, defensor.nome))
    else:
        print('{} atacou {}'.format(atacante.nome, defensor.nome))
    defensor.ReceberDano(dano=atacante.Ataque(), drenagem=atacante.drenagem)
    return


def JogadasHeroi(heroi):
    jogada = input().split(" ")
    while jogada[0] != 'A':
        if jogada[0] == 'M':
            if jogada[1] == 'C':
                print('{} encontrou a carta Cura'.format(heroi.nome))
                heroi.Cura(int(jogada[2]), int(jogada[3]))
            elif jogada[1] == 'F':
                print('{} encontrou a carta Força'.format(heroi.nome))
                heroi.Forca(int(jogada[2]), int(jogada[3]))
            elif jogada[1] == 'P':
                print('{} encontrou a carta Proteção'.format(heroi.nome))
                heroi.Protecao(int(jogada[2]), int(jogada[3]))
            elif jogada[1] == 'E':
                print('{} encontrou a carta Éter'.format(heroi.nome))
                heroi.Eter(int(jogada[2]))
            elif jogada[1] == 'D':
                print('{} encontrou a carta Drenagem'.format(heroi.nome))
                heroi.DefinirDrenagem(int(jogada[2]))
            elif jogada[1] == 'I':
                print('{} encontrou a carta Insano'.format(heroi.nome))
                heroi.DefinirInsano(int(jogada[2]), int(jogada[3]), int(jogada[4]))
            elif jogada[1] == 'S':
                print('{} encontrou a carta Estrela'.format(heroi.nome))
                heroi.DefinirEstrela(int(jogada[2]), int(jogada[3]))
            elif jogada[1] == 'X':
                print('{} não encontrou nenhuma carta'.format(heroi.nome))
        elif jogada[0] == 'I':
            heroi.AtivarInsano()
        elif jogada[0] == 'S':
            heroi.AtivarEstrela()
        jogada = input().split(" ")
    return


heroi1 = Heroi(input(), int(input()), int(input()), int(input()), int(input()))
heroi2 = Heroi(input(), int(input()), int(input()), int(input()), int(input()))


print("O reino Snowland indicou o herói {}\nO reino Sunny Kingdom indicou o herói {}".format(heroi1.nome, heroi2.nome))
rodada = 1
while heroi1.vida > 0 and heroi2.vida > 0:
    heroi = input().split(" ")[1]
    if heroi == '1':
        heroiatacante = heroi1
        heroidefensor = heroi2
    else:
        heroiatacante = heroi2
        heroidefensor = heroi1
    print("Rodada {}: vez de {}".format(rodada, heroiatacante.nome))
    JogadasHeroi(heroiatacante)
    Atacar(heroiatacante, heroidefensor)
    if heroidefensor.vida == 0:
        break
    heroi = input().split(" ")[1]
    if heroi == '1':
        heroiatacante = heroi1
        heroidefensor = heroi2
    else:
        heroiatacante = heroi2
        heroidefensor = heroi1
    print("Rodada {}: vez de {}".format(rodada, heroiatacante.nome))
    JogadasHeroi(heroiatacante)
    Atacar(heroiatacante, heroidefensor)
    heroi1.SituacaoAtual()
    heroi2.SituacaoAtual()
    heroi1.AtualizaEfeitos()
    heroi2.AtualizaEfeitos()
    rodada += 1
if heroi1.vida == 0:
    print('O herói {} do reino Sunny Kingdom venceu o duelo'.format(heroi2.nome))
else:
    print('O herói {} do reino Snowland venceu o duelo'.format(heroi1.nome))
heroi1.SituacaoAtual()
heroi2.SituacaoAtual()