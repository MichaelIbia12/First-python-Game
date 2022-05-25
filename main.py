#imports


import fileinput
import pygame
from sys import exit
import action


FRAME_SPEED = 0.7
WIDTH = 1380
HEIGHT = 820
player_x = 40
player_y = 400
enemy_x = 1100
enemy_y = 400
frames = 0
players_movement = ""
PlayersWalkSpeed = 0
PlayersJumpSpeed = 0
PlayersDirection = False
EnemysWalkSpeed = 0
EnemysJumpSpeed = 0
playerActionFile = action.idle

#display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pixelwar")
clock = pygame.time.Clock()
#assets
bg = pygame.image.load("utility\Wallpaper.jpg")

class Players():
    def __init__(self,x,y,file,enemy):  
        self.file = file
        self.x = x
        self.y = y
        self.enemy = enemy

        self = pygame.image.load(self.file[int(frames)])
        self = pygame.transform.scale(self, (200, 340))
        if PlayersDirection:
            self = pygame.transform.flip(self,True,False) 
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


           
#Elements


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
    
             
    screen.fill("grey")
    screen.blit(bg, (0,0))
    frames += FRAME_SPEED
    health("red",0,0,50,False)
    health("blue",0,0,50,True)
    timer()
    user = Players(player_x,player_y,playerActionFile,False)
    enemy = Players(enemy_x,enemy_y, playerActionFile,True)
    
    if (int(frames) == len(user.file)-1):
        frames = 0
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
   
    player_x -= PlayersWalkSpeed
    player_y -= PlayersJumpSpeed
    enemy_x -= EnemysWalkSpeed
    enemy_y -= EnemysJumpSpeed
    if player_y >= 400:
       PlayersJumpSpeed = 0
    if player_y <= 200:
       PlayersJumpSpeed = 0
    pygame.display.update()
    print(player_y)
    clock.tick(60)