import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((128, 128), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('1.png').convert()
background1 = pygame.image.load('1.png').convert()
background2 = pygame.image.load('2.png').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if background == background1:
                background = background2
            else:
                background = background1
    screen.blit(background, (0,0))
    pygame.display.update()
