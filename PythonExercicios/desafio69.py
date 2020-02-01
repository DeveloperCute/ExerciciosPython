maioridade = men = woman = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Digite seu sexo: [M/F] ')).lower()[0].strip()
    decisao = ' '
    if idade >= 18:
        maioridade += 1
    if sexo == 'm':
        men += 1
    if sexo == 'f' and idade < 20:
        woman += 1
    while decisao not in '01':
        decisao = str(input('Quer continuar? Digite 1 para continuar e 0 para parar: '))[0]
    if decisao == '0':
        break
print(f'''Quantidade de pessoas maiores de 18 anos: {maioridade}
Quantidade de homens cadastrados: {men}
Quantidade de mulheres com menos de 20 anos: {woman}
''')


