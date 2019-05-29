from random import randint


#ENTRADA
print('Suas opções')
print("INFORME 0 PARA PEDRA\n""INFORME 1 PARA PAPEL\n""INFORME 2 PARA TESOURA")
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
jogador2 = randint(0, 2)
jogador1 = int(input('Qual sua jogada? '))

while jogador1 < 0 or jogador1 > 2:
    jogador1 = int(input("Opção invalida, digite novamente: "))


print('='*23)
print('Você jogou {}\nAdversário jogou {}'.format(opcoes[jogador1], opcoes[jogador2]))
print('=' * 23)
print('')


#CONDIÇÃO
if opcoes[jogador2] == opcoes[jogador1]:
    print('\033[35mEMPATOU! :/')
elif jogador2 == 0 and jogador1 == 2:
    print('\033[36mVocê GANHOU! :)')
elif jogador2 == 1 and jogador1 == 0:
    print('\033[36mVocê GANHOU! :)')
elif jogador2 == 2 and jogador1 == 1:
    print('\033[36mVocê GANHOU! :)')
else:
    print('\033[31mVocê PERDEU! :(')