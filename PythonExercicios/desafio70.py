totalG = prod1000 = 0
barato = 99999999999
nomeN = ''
print('-' * 30)
print('{:-^20}'.format('Supermercado DO MUMUS'))
print('-' * 30)
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    decisao = ' '
    while decisao not in 'sn':
        decisao = str(input('Deseja continuar cadastrando produtos? [s/n]  ')).strip().lower()[0]
    totalG += preco
    if decisao == 'n':
        break
    if preco > 1000:
        prod1000 += 1
    if preco < barato:
        barato = preco
        nomeN = nome

print('{:-^30}'.format(' FIM DAS COMPRAS '))
print(f'''Total gastos nas compras: {totalG}
Quantidade de produtos que valem mais de mil reais: {prod1000}
O nome do produto mais barato é: {nomeN}
''')