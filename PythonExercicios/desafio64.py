

n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Quantidade de tentativas: {}, e a soma entre os números foram: {}'.format(cont, soma))
