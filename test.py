#import pygame
#import action
#pygame.init()
##
#screen = pygame.display.set_mode((500,500))
#clock = pygame.time.Clock()

#class person:
#    def __init__(self, x, y, flip,array):
#        self.x = x
#        self.y = y
#        self.speed = 0.10
#        self.current_frame_count = self.speed
#        self.frame = int(self.current_frame_count)
#        self.animation_array = array
#        flip = flip
#        self = pygame.image.load(array[self.frame])
#        self = pygame.transform.scale(self, (300, 300))
#        if flip == True :
#            self = pygame.transform.flip(self, True, False)
#        screen.blit(self, (x,y))
        
#def animation(className):
#    if int(className.current_frame_count) >= len(className.animation_array)-1:
#            className.current_frame_count = 0
#    className.current_frame_count += className.speed
#    print(className.current_frame_count)
   
#david = person(90,240,True, action.run)
#oceans = person(40,240,False, action.run)

#while False:
#    for e in pygame.event.get():
#        if e.type == pygame.QUIT:
#            quit()
#    animation(david)
#    pygame.display.update()
#    clock.tick(25)