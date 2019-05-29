from random import randint

partidas = 0
pontosj1 = 0
pontosj2 = 0
empates = 0

while True:
    #ENTRADA
    print('Suas opções:')
    print("INFORME 0 PARA PEDRA\n""INFORME 1 PARA PAPEL\n""INFORME 2 PARA TESOURA")
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    jogador1 = int(input('Qual sua jogada?\n'))
    jogador2 = randint(0, 2)

    while jogador1 < 0 or jogador1 > 2:
        jogador1 = int(input("Opção invalida, digite novamente: "))


    print('='*23)
    print('Você jogou {}\nAdversário jogou {}'.format(opcoes[jogador1], opcoes[jogador2]))
    print('=' * 23)
    print('')


    #CONDIÇÃO
    if opcoes[jogador2] == opcoes[jogador1]:
        print('EMPATOU! :/')
        partidas += 1
        empates += 1
    elif jogador1 == 0 and jogador2 == 2 or jogador1 == 1 and jogador2 == 0 or jogador1 == 2 and jogador2 == 1:
        print('Você GANHOU! :)')
        partidas += 1
        pontosj1 += 1
    else:
        print('Você PERDEU! :(')
        partidas += 1
        pontosj2 += 1
    if input('Deseja jogar novamente? sim/nao\n') == 'nao':
        break
    else:
        pass
print('Partidas jogadas:', partidas)
print('Vitórias Jogador1:', pontosj1)
print('Vitórias Jogador2:', pontosj2)
print('Empates:', empates)
