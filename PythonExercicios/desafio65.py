media = mediaF= maior = cont = 0
menor = 99999999
ans = 's'
listN = []
while ans == 's':#ou while ans in 'Ss'
    cont += 1
    n = int(input('Digite um valor: '))
    listN.append(n)
    ans = str(input('Deseja continuar? [S/N]: ')).lower()
    media += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
mediaF = media / cont
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))
print('A média dos números é: {}'.format(mediaF))
print('Os números digitados foram: {}'.format(listN))
