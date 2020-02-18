# coding: iso-8859-1 -*-
valores = list()
for v in range(0,5):
  valor = int(input('Digite um número: '))
  i = 1
  if v == 0:
    valores.append(valor)
  if v >= 1:
    while True:
      if valor == valores[i-1]:
        valores.insert(i-1, valor)
        break
      if valor > valores[i-1]:
        if len(valores) == i:
          valores.append(valor)
          break
        i += 1
      else:
        valores.insert(i-1, valor)
        break
  print(valores)
print(valores)