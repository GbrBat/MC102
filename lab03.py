print("Você apresenta pelo menos 4 dos sintomas principais do COVID-19? (Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)\n(1) sim\n(2) não")
q1 = input()
if q1 == "1":
    print("Você realizou o teste do COVID-19 desde que esses sintomas surgiram?\n(1) não\n(2) sim, deu positivo\n(3) sim, deu negativo")
    q2 = input()
    if q2 == "1":
        print("Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19")
    elif q2 == "2":
        print("Você se encontra em estado grave de saúde?\n(1) sim\n(2) não")
        q3 = input()
        if q3 == "1":
            print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
        elif q3 == "2":
            print("Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; fumante; pessoa de extremos de idade, seja criança ou idoso)\n(1) sim\n(2) não")
            q4 = input()
            if q4 == "1":
                print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
            elif q4 == "2":
                print("Baseado em suas respostas, a orientação é que você entre em isolamento")
            else:
                print("Opção inválida, recomece a avaliação")
        else:
            print("Opção inválida, recomece a avaliação")
    elif q2 == "3":
        print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
    else:
        print("Opção inválida, recomece a avaliação")
elif q1 == "2":
    print("Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?\n(1) sim\n(2) não")
    q5 = input()
    if q5 == "1":
        print("Baseado em suas respostas, a orientação é que você entre em isolamento")
    elif q5 == "2":
        print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
    else:
        print("Opção inválida, recomece a avaliação")
else:
    print("Opção inválida, recomece a avaliação")
