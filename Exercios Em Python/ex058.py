import random
import emoji
from time import sleep
NumPC = random.randrange(0,10,1)
print('\033[1;31;47m -=-'*10)

Rungame = ''
tried = 0
while Rungame != 'f':
    NumUsuario= int(input('\033[1;33;42m Pense em um número e quando estiver pronto digite '))
    print('-=-'*10)
    print('\033[1;31;47m Processando...'.upper())
    sleep(1)
    if NumPC == NumUsuario:
        print(emoji.emojize('\033[1;33;42m Parabéns você acertou :thumbsup:', use_aliases=True))
        Rungame = 'f'
    else:
        print(emoji.emojize('Você errou :hankey:', use_aliases=True))
        tried += 1
        
print('Você acertou com {} tentativas'. format(tried + 1 ))
print('Eu pensei no {}, Obrigado por jogar'.format(NumPC))