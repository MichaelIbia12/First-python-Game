import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("myGAME")
clock = pygame.time.Clock()

sky = pygame.image.load("graphics/sky.png")
ground = pygame.image.load("graphics/ground.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    pygame.display.update()
    clock.tick(60)
