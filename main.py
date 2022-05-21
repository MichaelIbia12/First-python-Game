#imports

import pygame
from sys import exit
import action

enemy_x = 600
gravity = 20
health_two_m = 150 
health_two_w = 300
health_two_m = health_two_w - health_two_m - health_two_m 
speed = 0.7

WIDTH = 1380
HEIGHT = 820

position = speed


#display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pixelwar")
clock = pygame.time.Clock()
#assets
bg = pygame.image.load("utility\Wallpaper.jpg")

class Players():
    def __init__(self, x):
        self.x = x
        self.frames =  1
        self = pygame.image.load(action.run[0])
        self = pygame.transform.scale(self, (200, 340))
        screen.blit(self, (x,400))
        
    def animatiion(self):
        if int(self.frames) == len(action.run)-1:
           self.frames = 0
        else:
            self.frames += 1
        print(self.frames)
                  
class health():
    def __init__(self,color, margin,innerWidth, width):
        self.width = width
        self.innerWidth = innerWidth
        self.margin = margin
        self.color = color
        self = pygame.Surface((500,30))
        innerSelf = pygame.draw.rect(self, color, [margin, innerWidth, width, self.get_height()])
        screen.blit(self, (50,20))
class timer():
    def __init__(self):
        self = pygame.draw.rect(screen, "black", [460 , 10, 50,50])
 
#Elements

#main function
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                act = action.run
                act_enenmy = action.run
                forward = False
                backward = True
                flip = True
            if event.key == pygame.K_d:
                act = action.run
                act_enenmy = action.run
                backward = False
                forward = True
                flip = False
            if event.key == pygame.K_w:
                act = action.jump
                gravity = 5
                y -= 190
                players_position = False
            if event.key == pygame.K_s:
                act = action.block
            if event.key == pygame.K_SPACE:
               if enemy_x  == x + 100:
                    health_two_m += 50
                    health_two_w -= 50
              
            if event.key == pygame.K_SPACE:             
               act = action.attack
               health_two_m += 50
               health_two_w -= 50
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                act = action.idle
            if event.key == pygame.K_a:
                act = action.idle
                act_enenmy = action.idle
                backward = False
            if event.key == pygame.K_d:
                act = action.idle
                act_enenmy = action.idle
                forward = False
            if event.key == pygame.K_w:
                act = action.idle
            if event.key == pygame.K_s:
                act = action.idle
        
    if players_position == False:
        y += gravity  

    if y >= 140 :
        y = 140
        players_position = True 
        gravity = 5     

    if  y < 50 :
        players_position = False     
        gravity += gravity

    close_Range = x + 100
        
  
    if  x ==  0: 
        x  += 10
        
    if enemy_x == 0 :
        enemy_x += 10
        
    if  x ==  WIDTH - 200:
        x  -= 10    
         
    if enemy_x == WIDTH -200:
        enemy_x -= 10
        
    if forward == True:
        x += 10  
    else:
        x = x  
    if backward == True:
        x -= 10
    else:
        x = x   
    if forward_enemy == True:

        enemy_x -= 10  
    else:
        enemy_x = enemy_x   
    if backward_enemy  == True:

        enemy_x += 10
    else:
        enemy_x = enemy_x    
   

    if enemy_x != x +100:
        forward_enemy = True
    else:
        forward_enemy = False
    
  
    
    if forward:
      
        forward_enemy = True
    else:
     
        forward_enemy = False
    if backward:
  
        forward_enemy = True
    else:

        backward_enemy = False
    if  enemy_x + 100 < x :
        forward_enemy = False     
        backward_enemy = True
        enemy_flip = True
   
  
    screen.fill("grey")
    screen.blit(bg, (0,0))
    
    

    health("red",0,0,50)
    timer()
    
    pygame.display.update()
    clock.tick(25)