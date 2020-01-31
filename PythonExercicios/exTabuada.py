
num = int(input('Digite um número para mostrar a tabuada de multiplicação: '))
i = 0
while i <= 10:
    result = num * i
    print('{} X {} = {}'.format(num, i, result))
    i += 1
