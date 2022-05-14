
import pygame
import random
from sys import exit
pygame.init()

width, height = 400, 400
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The snake game")
x , y = 200, 200
def random_x():
     food_x = random.randrange(0, width)//10*10
     return food_x
def random_y():
    food_y = random.randrange(0, height)//10*10
    return food_y
x_f = random_x()
y_f = random_y()
delta_x, delta_y = 0, 0
time = pygame.time.Clock()
body_list = [(x,y)]


def snake():
    global x, y
    x += delta_x
    y += delta_y
    
    body_list.append((x,y))
    if x_f == x and y_f == y:      
        while (x_f, y_f) in body_list:
            random_x()
            random_y()
    else:
        del body_list[0]
    game_screen.fill("#212121")
    pygame.draw.rect(game_screen, (255, 3, 99), [x_f, y_f, 10,10])
    pygame.draw.rect(game_screen, "blue", [x, y, 10, 10])
    for i, j in body_list:
       pygame.draw.rect(game_screen, "blue", [i, j, 10, 10]) 
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if delta_x != -10:
                    delta_x = -10
                delta_y = 0
            if event.key == pygame.K_RIGHT:
                if delta_x != 10:
                    delta_x = 10
                delta_y = 0
            if event.key == pygame.K_UP:
                delta_x = 0
                if delta_y != -10:
                     delta_y = -10
            if event.key == pygame.K_DOWN:
                delta_x = 0
                if delta_y != 10:
                      delta_y = 10
            else:
                continue
            if not event:
                snake()
    snake()
    print(x_f)
    print(y_f)
    time.tick(10)