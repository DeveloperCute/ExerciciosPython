soma = i =  0
while True:
    n = int(input('Digite um número: [999 For Stop]: \n'))
    if n == 999:
        break
    soma += n
    i += 1
print(f'A soma dos números foram: {soma}, e a quantidade de números digitados foram: {i}')
print('FIM!')