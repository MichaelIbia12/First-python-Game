#imports
from sys import exit

import pygame

import action

FRAME_SPEED = 1
WIDTH = 1380
HEIGHT = 820
player_x = 40
player_y = 400
enemy_x = 1100
enemy_y = 400
frames = 0
players_movement = ""
enemy_movement = ""
PlayersWalkSpeed = 0
PlayersJumpSpeed = 0
PlayersDirection = False
EnemysDirection = False
EnemysWalkSpeed = 0
EnemysJumpSpeed = 0
playerActionFile = action.idle
enemyActionFile = action.idle
PlayerFlip = False
EnemyFlip = False
EnemyAttack = False

AttackCounter = 0
Blockcounter = 0

#display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pixelwar")
clock = pygame.time.Clock()
#assets
bg = pygame.image.load("utility/bitmap.png")
floor = pygame.image.load("utility/rect10833.png")

class Player():
    def __init__(self,x,y,):  
       
   
        self.x = x
        self.y = y
        self = pygame.image.load(playerActionFile[int(frames)])
        if PlayersDirection:
             self = pygame.transform.flip(self, True,False)
        self = pygame.transform.scale(self, (400, 400))
        screen.blit(self, (x,y))
    
 
 
        

class Enemy():
    def __init__(self,x,y):  
   
        self.x = x
        self.y = y
        self = pygame.image.load(enemyActionFile[int(frames)])
        self = pygame.transform.scale(self, (400, 400))
        self = pygame.transform.flip(self, True,False)
        if EnemysDirection:
             self = pygame.transform.flip(self, True,False)
        screen.blit(self, (x,y))
  
    
    
       
class health():
    def __init__(self,color, margin,innerWidth, width, flip):
        self.width = width
        self.innerWidth = innerWidth
        self.margin = margin
        self.color = color
        x = 50
        if flip :
           x  = 850
           margin = 250
           margin = margin - width + margin
        self = pygame.Surface((500,30))

        innerSelf = pygame.draw.rect(self, color, [margin, innerWidth, width, self.get_height()])
        screen.blit(self, (x,20))
class timer():
    def __init__(self):
        self = pygame.draw.rect(screen, "black", [screen.get_width() / 2 , 10, 50,50],50,50)


           

 


#main function
while True:

   
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                players_movement = "up" 
                PlayersJumpSpeed = 50
            if event.key == pygame.K_DOWN:
                players_movement = "down" 
            if event.key == pygame.K_LEFT:
                players_movement = "backward" 

                PlayersWalkSpeed =  10
            if event.key == pygame.K_RIGHT:
                players_movement = "forward" 

                PlayersWalkSpeed = -10
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_UP:
                players_movement = "" 
                PlayersJumpSpeed = -50
                
            if event.key == pygame.K_DOWN:
                players_movement = "" 
            if event.key == pygame.K_LEFT:
                players_movement = "" 
                PlayersWalkSpeed = 0
            if event.key == pygame.K_RIGHT:
                players_movement = "" 
                PlayersWalkSpeed = 0
    
    CloseRange = 200 + player_x        
    screen.fill("grey")
  
    screen.blit(bg, (0,0))
    screen.blit(floor, (0,500))
    frames += FRAME_SPEED
    health("red",0,0,50,False)
    health("blue",0,0,50,True)
    timer()

    user = Player(player_x,player_y)
    enemy = Enemy(enemy_x,enemy_y)
    
    if (int(frames) == len(playerActionFile)-1):
        frames = 0
    if (int(frames) == len(enemyActionFile)-1):
        frames = 0
  
    player_x -= PlayersWalkSpeed
    player_y -= PlayersJumpSpeed
    enemy_x -= EnemysWalkSpeed
    enemy_y -= EnemysJumpSpeed
    
    
    if player_y >= 400:
       PlayersJumpSpeed = 0
    if player_y <= 200:
       PlayersJumpSpeed = 0
       
   
    
    if players_movement == "forward":
       playerActionFile= action.run  
       PlayersDirection = False      
    if players_movement == "backward":
       playerActionFile= action.run
       PlayersDirection = True
    if players_movement == "up":
       playerActionFile= action.jump
    if players_movement == "down":
         pass       
    if players_movement == "":
        playerActionFile= action.idle        
    
    if player_x < enemy_x:
        enemy_movement = "forward"
        print("t")   
    
    EnemysWalkSpeed = 10
    if enemy_x == CloseRange:
            #problem
            enemy_movement = "idle"
            EnemyAttack = True
            EnemysWalkSpeed = 0
  
    if enemy_movement == "forward":
        enemyActionFile= action.run  
        EnemysDirection = False   
        #problem      
    if enemy_movement == "backward":
        enemyActionFile= action.run
        EnemysDirection = True
       
    if enemy_movement == "up":
        enemyActionFile= action.jump
      
    if enemy_movement == "idle":
        enemyActionFile= action.idle  
    if EnemyAttack:
        enemyActionFile = action.attack
        
    #predictions
    
    if players_movement == "forward" and EnemyAttack:
        EnemysWalkSpeed = -10
        
        
    pygame.display.update()
    print(frames)
    clock.tick(60)
