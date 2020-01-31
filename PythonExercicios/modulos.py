from math import ceil, floor, trunc, pow, sqrt
import emoji
print(emoji.emojize("Ráiz Quadrada :earth_americas:", use_aliases=True))

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {}'.format(num, raiz))