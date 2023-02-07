# MC102W - 1s2020
# Aluno: Gabriel Batista
# RA: 212845
# Data: 14/05/2020
# Descrição: Auxílio Emergencial


class Governo:
    def __init__(self):
        self.benepend = []
        self.beneatual = []
        self.recursos = 0

    def BenePend(self):
        print('Beneficiários avaliados')
        print('Lista de beneficiários atualizada')
        for ben in self.benepend:
            if ben.Apto():
                self.beneatual.append(ben)
                ben.status = "Com auxílio"
            else:
                ben.status = "Negado"
        self.benepend = []
        #         informações
        return
        # Avalia os beneficiarios pendentes e concede ou recusa o beneficio

    def BeneAtual(self):
        print('Beneficiários atuais:')
        for ben in self.beneatual:
            print("{}.{}.{}-{}: {} {}".format(ben.cpf[:3], ben.cpf[3:6], ben.cpf[6:9], ben.cpf[9:], ben.nome, ben.sobrenome))
        return

    def AdicRecursos(self, valor):
        self.recursos = self.recursos + valor
        print('Recursos adicionados')
        return

    def Recursos(self):
        print('Recursos disponíveis: R$ {:.2f}'.format(self.recursos))
        return

    def EnvAuxilio(self):
        for ben in self.beneatual:
            if self.recursos < 600:
                print("Recursos insuficientes")
                return
            elif ben.xrecebimento < 3:
                ben.money += 600
                ben.xrecebimento += 1
                self.recursos -= 600
            else:
                self.beneatual.remove(ben)
                ben.status = "Auxílio finalizado"
        print("Auxílio mensal enviado")
        return


class Beneficiario:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.cpf = ""
        self.status = "Perfil incompleto"
        self.rendapc = 0
        self.rendatotal = 0
        self.idade = 0
        self.emprego = ""
        self.xrecebimento = 0
        self.money = 0
        self.auxilio = False
        self.cadastro = False

    def NomeCompleto(self):
        return "Nome completo: {} {}".format(self.nome, self.sobrenome)

    def Status(self):
        return "Status: {}".format(self.status)

    def CPF(self):
        return "CPF: {}.{}.{}-{}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])

    def PrintCPF(self):
        return "{}.{}.{}-{}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])

    def RendaPC(self):
        return "Renda per capita: R$ {:.2f}".format(float(self.rendapc))

    def RendaTT(self):
        return "Renda total: R$ {:.2f}".format(float(self.rendatotal))

    def Idade(self):
        return "Idade: {}".format(self.idade)

    def Emprego(self):
        return "Emprego: {}".format(self.emprego)

    def TempoDeReceb(self):
        return "Tempo de recebimento: {} meses".format(self.xrecebimento)

    def Transferencia(self, conta):
        print("Valor de R$ {:.2f} transferido para a conta corrente {}".format(self.money, conta))
        self.money = 0
        return

    def Login(self):
        return "{}.{}.{}-{}: {} {}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:], self.nome, self.sobrenome)

    def TodasInfos(self):
        print(self.NomeCompleto())
        print(self.Status())
        if self.cpf == '':
            print("CPF: ")
        else:
            print(self.CPF())
        print(self.RendaPC())
        print(self.RendaTT())
        print(self.Idade())
        print(self.Emprego())
        print(self.TempoDeReceb())
        return

    def ValidaCadastroCompleto(self):
        return self.nome != "" and self.cpf != "" and self.rendatotal != 0 and self.idade != 0 and self.emprego != ""

    def Apto(self):
        return self.ValidaCadastroCompleto() and self.idade > 18 and (self.emprego.lower() == "desempregado" or self.emprego.lower() == "desempregada" or self.emprego.lower() == "autonomo" or self.emprego.lower() == "autonoma" or self.emprego.lower() == "microempreendedor" or self.emprego.lower() == "microempreendedora") and (self.rendapc <= 522.50 or self.rendatotal <= 3135.00) and self.status != "Auxílio finalizado" and self.status != "Com auxílio" and self.status != "Negado"

    def Perfil(self):
        operacao = input().split(" ")
        while operacao[0] != 'F':
            if operacao[0] == '1':
                del (operacao[0])
                self.nome = operacao.pop(0).upper()
                self.sobrenome = " ".join(operacao).upper()
                print("Nome inserido")
            elif operacao[0] == '2':
                del (operacao[0])
                self.cpf = "".join(operacao).replace('-', '').replace('.', '')
                print("CPF inserido")
            elif operacao[0] == '3':
                del (operacao[0])
                self.rendapc = float(operacao[0])
                print("Renda per capita inserida")
            elif operacao[0] == '4':
                del (operacao[0])
                self.rendatotal = float(operacao[0])
                print("Renda total inserida")
            elif operacao[0] == '5':
                del (operacao[0])
                self.idade = int("".join(operacao))
                print("Idade inserida")
            elif operacao[0] == '6':
                del (operacao[0])
                self.emprego = "".join(operacao)
                print("Emprego inserido")
            elif operacao[0] == '7':
                if self.ValidaCadastroCompleto() and self.status == "Perfil incompleto":
                    self.status = "Perfil completo"
                if self.status == "Perfil completo":
                    print("Auxílio solicitado, aguarde avaliação")
                    self.status = 'Pendente'
                elif self.status == "Perfil incompleto":
                    print("Complete seu perfil e tente novamente")
            elif operacao[0] == '8':
                self.Transferencia(operacao[1])
            elif operacao[0] == '9':
                print(self.NomeCompleto())
            elif operacao[0] == '10':
                if self.ValidaCadastroCompleto() and self.status == "Perfil incompleto":
                    self.status = "Perfil completo"
                print(self.Status())
            elif operacao[0] == '11':
                print(self.CPF())
            elif operacao[0] == '12':
                if self.ValidaCadastroCompleto() and self.status == "Perfil incompleto":
                    self.status = "Perfil completo"
                self.TodasInfos()
            operacao = input().split(" ")
        if self.ValidaCadastroCompleto() and self.status == "Perfil incompleto":
            self.status = "Perfil completo"
        return

beneficiarios = []
governo = Governo()

operacao = input().lower().split(" ")
while operacao[0] != 'x':
    if operacao[0] == 'beneficiario':
            if len(operacao) < 2:
                benef = Beneficiario()
                benef.Perfil()
                beneficiarios.append(benef)
            else:
                for benef in beneficiarios:
                    if benef.cpf == operacao[1].replace(".", "").replace("-", ""):
                        break
                benef.Perfil()
            if benef.status == "Pendente" and benef not in governo.benepend:
                governo.benepend.append(benef)
    elif operacao[0] == 'governo':
        while operacao[0] != 'F':
            operacao = input().split(" ")
            if operacao[0] == '1':
                governo.BenePend()
            elif operacao[0] == '2':
                governo.AdicRecursos(float(operacao[1]))
            elif operacao[0] == '3':
                governo.Recursos()
            elif operacao[0] == '4':
                governo.BeneAtual()
            elif operacao[0] == '5':
                governo.EnvAuxilio()
    operacao = input().lower().split(" ")
