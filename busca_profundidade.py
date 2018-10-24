def geraarvore(profundidade):
    solucao = []
    for i in range(0,profundidade):
        solucao.append("*")
    jogada = -1
    fsolucaonova = False #indica quando true a troca de folha ou ramo
    for i in range(0,(6**profundidade)):     
        jogada += 1
        if(fsolucaonova):
            solucao[jogada] += 1
            fsolucaonova = False
            if(solucao[jogada]>4):
                    for jogadaAnterior in range(jogada,-1,-1):
                        if(solucao[jogadaAnterior] < 4):
                            solucao[jogadaAnterior] += 1
                            jogada = jogadaAnterior 
                            break
                        solucao[jogadaAnterior] = "*"
        else:        
            solucao[jogada] = 0
        if(jogada >= profundidade - 1):
            jogada -= 1
            fsolucaonova = True
        print("{ ",i," } ","{ ",jogada+1," } ",solucao)
        # Ta aqui o zico!!!!! Acabou o chororo
        testeUltimaJogada = True
        for i in range(0,profundidade):
            if(solucao[i] != 4):
                testeUltimaJogada = False       
        if(testeUltimaJogada):
            break;
        testeUltimaJoagada=False

        
geraarvore(4)
