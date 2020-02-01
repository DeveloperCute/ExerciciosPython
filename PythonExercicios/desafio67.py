while True:
    n = int(input('Digite o número que deseja saber a tabuada: '))
    if n < 0:
        break
    for i in range(1, 11):
        result = n * i
        print(f'{n} X {i} = {result}')
print('FIM!')
