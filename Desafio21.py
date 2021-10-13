import pygame
pygame.init()
print('Vamos tocar uma música de piano.')
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Você está ouvindo a música? ')

