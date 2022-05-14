import pygame

#pygame.init()
screen = pygame.display.set_mode((500,500))

#class object(pygame.sprite.Sprite):
#    def __init__(self,x,y):
#        self.image = []
#        self.image.append("utility/1x/attack_0.png")
#        self.image.append("utility/1x/attack_1.png")
#        self.image.append("utility/1x/attack_2.png")
#        self.x = x
#        self.y = y
#        self.current_image = 0
#        self.obj = pygame.image.load(self.image[self.current_image])
#        self.obj = pygame.transform.scale(self.obj, (500,500))
#        screen.blit(self.obj, (self.x, self.y))
#        
#                 
#            
#
#        pygame.display.update()
clock = pygame.time.Clock()   
#player = object(50,50)
screen.fill("blue")
idle = [
    "utility/1x/idle_0.png",
    "utility/1x/idle_1.png",
    "utility/1x/idle_2.png",
    "utility/1x/idle_3.png"
]
attack = [
    "utility/1x/attack_0.png",
    "utility/1x/attack_1.png",
    "utility/1x/attack_2.png"
]

position = 0.2
count = 0.2
action = idle
def object():
    p_up = int(position)
    obj = pygame.image.load(action[int(p_up)])      
    obj = pygame.transform.scale(obj, (500,500))
    player = obj.get_rect(topleft=(100, 300))
    screen.blit(obj, player)    

while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            pygame.quit()
        if x.type == pygame.KEYDOWN:
            if x.key == pygame.K_d:
                action = attack

        
        if x.type == pygame.KEYUP:
            if x.key == pygame.K_d:
                action = idle
             
        
    object()
    if int(position) >= len(action)-1:
        position = 0.2
    else:
        position += 0.1
    print(int(position))
    pygame.display.update()
    clock.tick(60)