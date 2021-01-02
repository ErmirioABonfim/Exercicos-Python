import pygame     #Importa a bilioteca Pygae

pygame.init()
pygame.mixer.init()     #Inicializa o módulo
pygame.mixer.music.load('ex021.mp3') #Aponta o caminho de funcionamento do módulo e carrega o arquivo 
pygame.mixer.music.play() # Aponta o caminho de funcionamento do módulo para tocar o arquivo
input()
pygame.event.wait() #Aponta para as opções de evento do módulo e aguarda o evento(Música) acabar para finalizar o programa
