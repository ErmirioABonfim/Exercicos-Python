

import random
num =  int (random.randint(0,9))
num2 = int (random.randint(0,9))
num3 = int (random.randint(0,9))
num4 = int (random.randint(0,9))
sorteado = (num, num2,num3,num4)

print('Os números sorteados foram:{}'.format(sorteado))
print('Os números ordenados são: {}'.format(sorted(sorteado)))
print('O maior número é: {}'.format(max(sorteado)))
print('O menor número é: {}'.format(min(sorteado)))

