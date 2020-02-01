from random import randint

totalWin = soma = vitoria = 0

print('JOGO DO PAR OU ÍMPAR')
while vitoria == 0:
    computer = randint(0, 10)
    player = int(input('Digite um valor: '))
    decisao = ' '
    soma = player + computer
    while decisao not in 'pi':
        decisao = str(input('[I/P] Par ou Ímpar?')).lower()[0]
    print(f'O computador jogou {computer} e você jogou {player} e resultado foi {soma}, por isso: \n')
    #print('Deu par' if soma % 2 == 0 else 'Deu ímpar!')
    if soma % 2 == 0:
        if decisao == 'p':
            print(f'Você ganhou jogando par, continue!')
            totalWin += 1
        else:
            print('Você perdeu jogando ímpar! Tente novamente depois!')
            break
    else:
        if decisao == 'i':
            print('Você ganhou jogando ímpar, continue!')
            totalWin += 1
        else:
            print('Você perdeu jogando par! Tente novamente!')
            break
print(f'A quantidade de vezes que você ganhou foram {totalWin}')



