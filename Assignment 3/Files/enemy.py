import pygame
import random
from pygame.locals import *
score = 0

class Enemy(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 3
    dy = 3
    screen = None
    image = None
    image_w = 0
    image_h = 0
    active = False
    thePlayer = None
    explosion = None
    counter = 0
    respawnFlag = False
    s = None
    
    def __init__(self,screen1,beginX,beginY,player):
        screen = screen1
        self.x = beginX + 60
        self.y = beginY
        self.active = True
        thePlayer = player
        pygame.sprite.Sprite.__init__(self)
        
        try:
            self.image = pygame.image.load("mutalisk.gif")
            self.explosion = pygame.image.load("laser_explosion.gif")
        except:
            print "could not load laser image"
        try:
            self.s = pygame.mixer.Sound('death_explode.wav')
        except:
            print "could not load the death_explode.wav"
        self.rect = self.image.get_rect()
       
    def update(self,screen,shot,player,list1):
        
        if self.x + self.dx > 800 or self.x + self.dy < 0:
            self.dx *= -1
        if self.y + self.dy > 600 or self.y + self.dy < 0:
            self.dy *= -1
        self.y += self.dy
        self.x += self.dx
        self.rect.topleft = [self.x,self.y]
        t = 0
        if shot:
            for t in range(0,len(shot)):
                if self.rect.colliderect(shot[t].rect):
                    shot[t].x = -440
                    self.active = False
        if player:
            if self.rect.colliderect(player.rect):
                self.s.play()
                player.active = False
        self.draw(screen)
        
    def draw(self,screen):
       
        if self.active == True:
            screen.blit(self.image, (self.x, self.y))   
        if self.active == False:
            self.counter = self.counter + 1
            screen.blit(self.explosion, (self.x, self.y))
            self.dx = 0
            self.dy = 0
            if self.counter == 20:
                self.x = -50
                self.y = -50
                self.respawnFlag = True
            
if __name__ == "__main__":
    
    white    = ( 255, 255, 255)
    black = (0,0,0)

    pygame.init()
     

    screen_width=800
    screen_height=600
    screen=pygame.display.set_mode([screen_width,screen_height])


    done = False
     

    clock = pygame.time.Clock()
    x_speed = 0
    y_speed = 0
    mutaCount = 0
    muta = []
    

    while done==False:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            

        screen.fill(white)
        if mutaCount != 11:
            mutaCount = mutaCount + 1
            muta.append(Enemy(screen,random.randint(0,screen_width),random.randint(0,screen_height),None))
        z = len(muta)
        t = 0
        for t in range(0,z):
            muta[t].update(screen,None,None,None)
        
        clock.tick(50)
     
        pygame.display.flip()
     
    pygame.quit()
