import pygame
import laser
import random
from battlecruiser import *
from laser import *

class Battlecruiser(pygame.sprite.Sprite):
    x = 200
    y = 400
    dx = 3
    dy = 3
    screen = None
    image = None
    image_w = 0
    image_h = 0
    active = False
    bulletCount = 0
    explosion = None
    counter = 0
    def __init__(self,screen1):
        
        self.active = True
        screen = screen1
        pygame.sprite.Sprite.__init__(self) 
        
            
        try:
            self.image = pygame.image.load("Battlecruiser.gif")
            self.explosion = pygame.image.load("laser_explosion.gif")
        except:
            print "Could not load battlecruiser image"
        self.rect = self.image.get_rect()
        
    def update(self,newX,newY,sFlag,screen):
        if newX < 0:
            self.x = self.x - self.dx
        elif newX > 0:
            self.x = self.x + self.dx
        if newY < 0:
            self.y = self.y - self.dy
        elif newY > 0:
            self.y = self.y + self.dy
        if sFlag:
            self.bulletCount = self.bulletCount + 1
        self.draw(screen)
        self.rect.topleft = [self.x,self.y]
        
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
        
if __name__ == "__main__":

    white = (255,255,255)
    black = (0,0,0)

    pygame.init()
     
    screen_width=800
    screen_height=600
    screen=pygame.display.set_mode([screen_width,screen_height])
     


    player = Battlecruiser(screen)
    
    done = False
     

    clock = pygame.time.Clock()
     
    score = 0
    x_speed = 0
    y_speed = 0
    bulletCount = 0
    shotFlag = False
    shot = []
    
    while done==False:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                elif event.key == pygame.K_SPACE:
                    shotFlag = True
                elif event.key == pygame.K_ESCAPE:
                    done = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP:
                    y_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = 0
                elif event.key == pygame.K_SPACE:
                    shotFlag = False
                
        screen.fill(black)
     
        player.update(x_speed,y_speed,shotFlag,screen)
        if shotFlag == True:
            shot.append(Laser(screen,player.x,player.y))
        shotFlag = False
        z = len(shot)
        t = 0
        for t in range(0,z):
            shot[t].update(screen)

        clock.tick(50)

        pygame.display.flip()
     
    pygame.quit()
