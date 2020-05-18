#Nomes: Henrique José e Marcos Assis

##Herr henry, leia os comentarios >:(
import random
from random import choice

##mbaralhamento de cartas
baralhoUm = [4.23, 4.22, 4.14, 4.13, 4.12, 4.11, 4.7, 4.6, 4.5, 4.4, 3.23, 3.22, 3.14, 3.13, 3.12, 3.11, 3.7, 3.6, 3.5,
             3.4, 2.23, 2.22, 2.14, 2.13, 2.12, 2.11, 2.7, 2.6, 2.5, 2.4, 1.23, 1.22, 1.14, 1.13, 1.12, 1.11, 1.7, 1.6,
             1.5, 1.4]  # cria um vetor com as cartas que vao ser sorteadas

cart1 = choice(baralhoUm)  # Sortei a primeira carta do jogador
baralhoDois = list(baralhoUm)  # Tire uma copia da baralhoUm
baralhoDois.remove(cart1)  # remove do baralhoDois a carta ja sorteada no baralhoUm
cart2 = choice(baralhoDois)
baralhoTres = list(baralhoDois)
baralhoTres.remove(cart2)
cart3 = choice(baralhoTres)
hand = [cart1, cart2, cart3]  # cria um vetor para mao do jogador

baralhoQuatro = list(baralhoTres)
baralhoQuatro.remove(cart3)
mcart1 = choice(baralhoQuatro)  # sorteia a primeira carta da maquina
baralho5 = list(baralhoQuatro)  # Tire uma copia da baralhoQuatro
baralho5.remove(mcart1)  # remove do baralho5 a carta ja sorteada no baralhoQuatro
mcart2 = choice(baralho5)
baralho6 = list(baralho5)
baralho6.remove(mcart2)
mcart3 = choice(baralho6)
mHand = [mcart1, mcart2, mcart3]  # cria um vetor para a mao da maquina
mSort = choice(mHand)  # sorteia a carta que a maquina vai jogar

##regras
print("")

print("Sequencia da maior para a menor:")
print("3|2|A|K|J|Q|7|6|5|4")
print("Sequencia de Nipes maior para a menor: ")
print("Paus = 4|Copas = 3|Espada = 2|Ouros = 1")
print("--------------------------------------------------------------------------------")
print("ATENCAO: ")
print("As cartas sao representadas por dois numeros: sendo o primeiro o seu Naipe e o segundo seu numero. Exemplo:")
print("4.23 = 3 de paus|3.5 = 5 de copas|2.11 = Valete de Espadas|1.7 = 7 de Ouros")
print("--------------------------------------------------------------------------------")
##Fim das regras
print("")
print("Suas cartas: ", "Carta 1:", cart1, "  Carta 2:", cart2, "  Carta 3:", cart3)
#print("Cartas da Máquina:", "Carta 1:", mcart1, "  Carta 2:", mcart2, "  Carta 3:", mcart3)
print("")
print('RODADA 1')
opt1 = int(input("Escolhe uma carta para jogar [1/2/3]: "))

cont = 0  # conta os pontos do jogador
Mcont = 0  # conta os pontos da maquina
##arrumar os ifs
if (opt1 == 1):
    print('você jogou: ', cart1, 'a maquina joga: ', mSort)
    if (cart1 > mSort):
        print("voce ganhou a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart1)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        cont1 = cont + 1
        print('RODADA 2')
        opt2 = int(input("Escolhe uma carta para jogar [2/3]: "))
        if (opt2 == 2):
            #isso
            print('você jogou: ', cart2, 'a maquina joga: ', mSort2)
            if (cart2 > mSort2):
                print("voce ganhou a rodada 2")
                cont2 = cont1 + 1
                print("Voce ganhou o jogo!!!")

            else:
                print("vc perdeu a rodada 2")
                Mcont1 = Mcont+1
                hand3 = list(hand2)
                hand3.remove(cart2)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                print('RODADA FINAL')
                print('Sua unica carta é: ',cart3, 'a maquina joga: ',mSort3)
                if (cart3 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
        else:
            #isso
            print('você jogou: ', cart3, 'a maquina joga: ', mSort)
            if (cart3 > mSort2):
                print("voce ganhou a rodada 2")
                cont2 = cont1 + 1
                print("Voce ganhou o jogo")

            else:
                print("vc perdeu a rodada 2")
                Mcont1 = Mcont + 1
                hand3 = list(hand2)
                hand3.remove(cart3)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                print('Sua unica carta é: ', cart2, 'a maquina joga: ', mSort3)
                if (cart2 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
    else:
        print("voce perdeu a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart1)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        Mcont1 = Mcont + 1
        opt2 = int(input("Escolhe uma carta para jogar [2/3]: "))
        if (opt2 == 2):
            print('você jogou: ', cart2, 'a maquina joga: ', mSort2)
            if (cart2 > mSort2):
                print("voce ganhou a rodada 2")
                cont1 = cont+1
                hand3 = list(hand2)
                hand3.remove(cart2)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('você jogou: ', cart3, 'a maquina joga: ', mSort3)
                if (cart3 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")
        else:
            print('você jogou: ', cart3, 'a maquina joga: ', mSort2)
            if (cart3 > mSort2):
                print("voce ganhou a rodada 2")
                Mcont1 = Mcont+1
                hand3 = list(hand2)
                hand3.remove(cart3)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('Sua ultima carta: ', cart2, 'a maquina joga: ', mSort3)
                if (cart2 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")
#aqui
elif (opt1 == 2):
    print('você jogou: ', cart2, 'a maquina joga: ', mSort)
    if (cart2 > mSort):
        print("voce ganhou a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart2)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        cont1 = cont + 1
        opt2 = int(input("Escolhe uma carta para jogar [1/3]: "))
        if (opt2 == 1):
            print('você jogou: ', cart2, 'a maquina joga: ', mSort2)
            if (cart1 > mSort2):
                print("voce ganhou a rodada 2")
                cont2 = cont1 + 1
                print("Voce ganhou o jogo")
            else:
                print("vc perdeu a rodada 2")
                Mcont1 = Mcont + 1
                hand3 = list(hand2)
                hand3.remove(cart1)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('Sua ultima carta: ', cart3, 'a maquina joga: ', mSort3)
                if (cart3 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
        else:
            print('você jogou: ', cart3, 'a maquina joga: ', mSort2)
            if (cart3 > mSort2):
                print("voce ganhou a rodada 2")
                Mcont1 = Mcont+1
                hand3 = list(hand2)
                hand3.remove(cart3)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('Sua ultima carta: ', cart2, 'a maquina joga: ', mSort3)
                if (cart2 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")

    else:
        print("voce perdeu a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart2)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        Mcont1 = Mcont + 1
        opt2 = int(input("Escolhe uma carta para jogar [1/3]: "))
        if (opt2 == 1):
            if (cart1 > mSort2):
                print("voce ganhou a rodada 2")
                cont1 = cont + 1
                hand3 = list(hand2)
                hand3.remove(cart1)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('você jogou: ', cart3, 'a maquina joga: ', mSort3)
                if (cart3 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")
        else:
            print('você jogou: ', cart3, 'a maquina joga: ', mSort2)
            if (cart3 > mSort2):
                print("voce ganhou a rodada 2")
                Mcont1 = Mcont + 1
                hand3 = list(hand2)
                hand3.remove(cart3)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                print('Sua ultima: ', cart1, 'a maquina joga: ', mSort3)
                if (cart1 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")

else:
    print('você jogou: ', cart3, 'a maquina joga: ', mSort)
    if (cart3 > mSort):
        print("voce ganhou a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart3)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        cont1 = cont + 1
        opt2 = int(input("Escolhe uma carta para jogar [1/2]: "))
        if (opt2 == 1):
            print('você jogou: ', cart1, 'a maquina joga: ', mSort2)
            if (cart1 > mSort2):
                print("voce ganhou a rodada 2")
                cont2 = cont1 + 1
                print("Voce ganhou o jogo")
            else:
                print("vc perdeu a rodada 2")
                Mcont1 = Mcont + 1
                hand3 = list(hand2)
                hand3.remove(cart1)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('sua ultima carta: ', cart1, 'a maquina joga: ', mSort3)
                if (cart1 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
        else:
            print('você jogou: ', cart2, 'a maquina joga: ', mSort2)
            if (cart2 > mSort2):
                print("voce ganhou a rodada 2")
                Mcont1 = Mcont+1
                hand3 = list(hand2)
                hand3.remove(cart2)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('Sua ultima carta: ', cart1, 'a maquina joga: ', mSort3)
                if (cart1 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")

    else:
        print("voce perdeu a rodada 1")
        hand2 = list(hand)
        hand2.remove(cart3)
        mHand2 = list(mHand)
        mHand2.remove(mSort)
        #print(hand2, mHand2)
        mSort2 = choice(mHand2)
        Mcont1 = Mcont + 1
        opt2 = int(input("Escolhe uma carta para jogar [1/2]: "))
        if (opt2 == 1):
            print('você jogou: ', cart1, 'a maquina joga: ', mSort2)
            if (cart1 > mSort2):
                print("voce ganhou a rodada 2")
                cont1 = cont + 1
                hand3 = list(hand2)
                hand3.remove(cart1)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                #print(hand3, mHand3)
                print('Sua ultima: ', cart3, 'a maquina joga: ', mSort3)
                if (cart2 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")
        else:
            print('você jogou: ', cart2, 'a maquina joga: ', mSort2)
            if (cart2 > mSort2):
                print("voce ganhou a rodada 2")
                Mcont1 = Mcont + 1
                hand3 = list(hand2)
                hand3.remove(cart2)
                mHand3 = list(mHand2)
                mHand3.remove(mSort2)
                mSort3 = choice(mHand3)
                print('Sua ultima: ', cart1, 'a maquina joga: ', mSort3)
                if (cart1 > mSort3):
                    print("vc ganhou o jogo")
                else:
                    print("VC PERDEU O JOGO")
            else:
                print("Voce perdeu o jogo")


