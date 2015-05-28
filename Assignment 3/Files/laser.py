import pygame
import random


class Laser(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 3
    dy = 3
    screen = None
    image = None
    image_w = 0
    image_h = 0
    active = False
    def __init__(self,screen1,beginX,beginY):
        screen = screen1
        self.x = beginX + 60
        self.y = beginY
        active = True
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load("laser.gif")
        except:
            print "could not load laser image"
        self.rect = self.image.get_rect()
        
    def update(self,screen):
        self.y = self.y - self.dy
        self.draw(screen)
        self.rect.topleft = [self.x,self.y]
        
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))

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
    bulletCount = 0
    shot = []

    while done==False:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            

        screen.fill(black)
     
        shot.append(Laser(screen,random.randint(0,screen_width),screen_height))
        z = len(shot)
        t = 0
        for t in range(0,z):
            shot[t].update(screen)
        

        clock.tick(50)
     

        pygame.display.flip()
     
    pygame.quit()
