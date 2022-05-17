#importsaaaa
from pickle import FALSE
from turtle import backward
import pygame
from sys import exit
import action

x = 50
y = 140
x_u = 0
long_Range = x + 200
enemy_x = 600
gravity = 20
players_position= True
health_two_m = 150 
health_two_w = 300
health_two_m = health_two_w - health_two_m - health_two_m 
speed = 0.7
forward = False
backward = False
forward_enemy = False
backward_enemy = False
attack = True
enemy_actions = ["run", "attack","block","jump"]
actions = "run"
WIDTH = 960
HEIGHT = 480
act = action.idle
act_enenmy = action.idle
position = speed
flip = False
enemy_flip = False

#display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pixelwar")
clock = pygame.time.Clock()
#assets
bg = pygame.image.load("utility/arena.png")

class Person():
    def __init__(self, x, y,  f):
        
          self.p = int(position)
          self.f = f
          self = pygame.image.load(self.f[self.p])
          self = pygame.transform.scale(self, (300,300))
          screen.blit(self, (x,y))
    

user = Person(x,140,action.idle)


#def player():
#    p_up = int(position)
#    obj = pygame.image.load(act[int(p_up)])     
#    obj = pygame.transform.scale(obj, (300,300)) 
#    player = obj.get_rect(center=(x,290))
#    
#    if flip:
#        obj = pygame.transform.flip(obj, True,False)
#    else:
#        obj = pygame.transform.flip(obj, False,False)
#    screen.blit(obj, player)    

def enemy():
    p_up = int(position)
    obj = pygame.image.load(act_enenmy[int(p_up)])      
    obj = pygame.transform.scale(obj, (300,300))
    obj = pygame.transform.flip(obj, True, False)
    enemy = obj.get_rect(center=(enemy_x,290))
    if enemy_flip:
        obj = pygame.transform.flip(obj, True,False)
    else:
        obj = pygame.transform.flip(obj, False,False)
    screen.blit(obj, enemy)    

def healthplayer():
    sprite = pygame.Surface((300,10))   
    inner_bar = pygame.draw.rect(sprite, "#ff0000", [0, 0, 100,sprite.get_height()],10)
    screen.blit(sprite, (50, 10))
def healthenemy():
    sprite = pygame.Surface((300,10))
    pygame.draw.rect(sprite, "#ff0000", [health_two_m, 0, health_two_w,sprite.get_height()], 10)
    screen.blit(sprite, (600, 10))

def timer():
    pygame.draw.rect(screen, "black", [460 , 10, 50,50])
 
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
   
    if int(position) >= len(act)-1 or int(position) >= len(act_enenmy)-1:
        position = speed
    else:
        position += speed

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
    
    
    enemy()

    healthplayer()
    healthenemy()
    timer()
    pygame.display.update()
    clock.tick(25)