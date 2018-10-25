# -*- coding: utf-8 -*-
import time

opcoesBote = [
        [0,2], #coluna 0 padres coluna 1 canibais
        [0,1],
        [2,0],
        [1,1],
        [1,0]
    ]
quantia = [3,0,3,0]

def mostrajogo():
    m1 = []
    m2 = []
    for i in range(1,7):
        if(quantia[0] >= i):
            m1.append("P")
        elif(i < 4):
            m1.append("*")
        elif((quantia[2] + 3) >= i):
            m1.append("C")
        else:
            m1.append("*")
        
        if(quantia[1] >= i):
            m2.append("P")
        elif(i < 4):
            m2.append("*")
        elif((quantia[3] + 3) >= i):
            m2.append("C")
        else:
            m2.append("*")
    print("\nMargem 1 = ",m1)
    print("Margem 1 = ",m2)
    if(mortes()):
        print("Houve mortes")
    else:
        print("Todos estão vivos!")
    if(objetivo()):
        print("Objetivo atinjido!\n")
    else:
        print("Objetivo não atinjido!\n")

def barco(jogada, dire):
    if(dire == 0):
        if((quantia[0] >= opcoesBote[jogada][0]) and (quantia[2] >= opcoesBote[jogada][1])):
            quantia[0] -= opcoesBote[jogada][0]
            quantia[1] += opcoesBote[jogada][0]
            quantia[2] -= opcoesBote[jogada][1]
            quantia[3] += opcoesBote[jogada][1]
            return True

    else:
        if((quantia[1] >= opcoesBote[jogada][0]) and (quantia[3] >= opcoesBote[jogada][1])):
            quantia[1] -= opcoesBote[jogada][0]
            quantia[0] += opcoesBote[jogada][0]
            quantia[3] -= opcoesBote[jogada][1]
            quantia[2] += opcoesBote[jogada][1]
            return True
    return False

def objetivo():
    if(quantia == [0,3,0,3]):
        return True
    return False

def mortes():
    if(((quantia[0] < quantia[2]) and quantia[0] != 0) or ((quantia[1] < quantia[3] and quantia[1] != 0))):
        return True
    return False

def refaz(jogada, sentido):
    if(sentido == 1):
        barco(jogada,0)
    else:
        barco(jogada,1)

def geraarvore(profundidade):
    solucao = []
    for i in range(0,profundidade):
        solucao.append("*")
    jogada = -1
    fsolucaonova = False #indica quando true a troca de folha ou ramo
    tentativas = 0
    sentido = 0
    #arq = open('dados_busca.txt','a')
    for i in range(0,(6**profundidade)):     
        jogada += 1
        tentativas += 1
        if(fsolucaonova):
            i -= 1
            if(type(solucao[jogada])==str):
                solucao[jogada] = 0
                print("------------------------")
            else:
                solucao[jogada] += 1
            fsolucaonova = False
            if(solucao[jogada] > 4):
                    for jogadaAnterior in range(jogada,-1,-1):
                        if(solucao[jogadaAnterior] < 4):
                            solucao[jogadaAnterior] += 1
                            jogada = jogadaAnterior 
                            break
                        solucao[jogadaAnterior] = "*"
        else:        
            solucao[jogada] = 0
        if(i % 2 == 0):
            sentido = 1
        else:
            sentido = 0
        if(not(barco(solucao[jogada],sentido))):
            fsolucaonova = True
        mostrajogo()
        if(objetivo()):
            break
        if(mortes()):
            fsolucaonova = True
            refaz(solucao[jogada], sentido)

        if(jogada >= profundidade - 1):
            jogada -= 1
            fsolucaonova = True
        print("{ ",i," } ","{ ",jogada+1," } ",solucao)
        #arq.write('{ ')
        #arq.write(str(i))
        #arq.write(' }')
        #arq.write('{ ')
        #arq.write(str(jogada + 1))
        #arq.write(' } ')
        #arq.write(str(solucao))
        #arq.write('\n')
        # Ta aqui o zico!!!!! Acabou o chororo
        testeUltimaJogada = True
        for i in range(0,profundidade):
            if(solucao[i] != 4):
                testeUltimaJogada = False   
        if(testeUltimaJogada):
            break
        testeUltimaJoagada=False
    #arq.close()
    print("{ ",tentativas," } ","{ ",jogada+1," } ",solucao)
    return solucao

inicio = time.time()
#mostrajogo()
geraarvore(11)
fim = time.time()
print("\nTempo de execução em segundos: ",fim - inicio)