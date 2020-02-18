valor = int(input('Digite o valor a ser sacado: '))
cinquenta = vinte = dez = um = 0
ced = 50
'''código do professor: 
total = 0
while True:
    if valor >= ced:
        valor -= ced
        total += 1
    else:
        if total > 0:
            print(f'Total de {total} cédulas de {ced}')
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total = 0
        if total == 0:
            break'''



while valor >= 50:
    cinquenta += 1
    valor -= 50
while valor >= 20:
    vinte += 1
    valor -= 20
while valor >= 10:
    dez += 1
    valor -= 10
while valor >= 1:
    um += 1
    valor -= 1

print(f'''Quantidade de notas de cinquenta: {cinquenta}
Quantidade de notas de vinte: {vinte}
Quantidade de notas de dez: {dez}
Quantidade de notas de um: {um}
''')