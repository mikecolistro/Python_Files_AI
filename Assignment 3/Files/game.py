#import libraries and classes
import pygame
import random
import battlecruiser
import laser
import enemy
from pygame.locals import *
from laser import *
from enemy import *
from battlecruiser import *

#set defaults for colours
white    = ( 255, 255, 255)
black = (0,0,0)

#initiate pygame
pygame.init()
 
#set values for the screen
screen_width=800
screen_height=600
screen=pygame.display.set_mode([screen_width,screen_height])

#create the players battlecruiser
player = Battlecruiser(screen)

#initiate main loop
done = False

#initiate clock
clock = pygame.time.Clock()

#lists tracking enemies and shots fired
shot_list = pygame.sprite.Group()
muta_list = pygame.sprite.Group()

#initiated some variables 
score = 0
x_speed = 0
y_speed = 0
bulletCount = 0
shotFlag = False
shot = []
mutaCount = 0
muta = []

#load the laser sound with exception handling
try:
    s = pygame.mixer.Sound('laser.wav')
except:
    print"Could not load laser.wave"
#main loop
while done==False:
    #event handling
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
                s.play()
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
            
               
    #set background colour
    screen.fill(black)
    #update player
    player.update(x_speed,y_speed,shotFlag,screen)
    #check to see if shot is fired, if so create laser
    if shotFlag == True:
        shot.append(Laser(screen,player.x,player.y))
        shot_list.add(shot[len(shot)-1])
    #make sure only one laser is created    
    shotFlag = False
    #variables to update all lasers
    z = len(shot)
    t = 0
    for t in range(0,z):
        shot[t].update(screen)
    #checks to see if there is 4 mutas, if not creates one and adds to the list
    if mutaCount !=  4:
        mutaCount = mutaCount + 1
        muta.append(Enemy(screen,random.randint(0,screen_width/5),random.randint(0,screen_height/10),None))
        muta_list.add(muta[mutaCount - 1])

    #initial variables for the textbox
    textx = 0
    texty = 0
    size = 0
    #determines wether to display score or game over message
    if player.active == True:
        string = 'Score: ' + `score`
        textx = 10
        texty = 10
        size = 15
    elif player.active == False:
        string = 'Game Over You Lose,Score is:' + `score`
        textx = 400
        texty = 300
        size = 40
        
    myfont = pygame.font.SysFont("monospace", size)
    label = myfont.render(string, 1, (255,255,255))
    screen.blit(label, (10, 10)) 
    #updates for the mutas    
    mutlen = len(muta)
    mutat = 0
    for mutat in range(0,mutlen):
        muta[mutat].update(screen,shot,player,muta_list)

    #check to see if need to respawn a new muta
    mutat = 0
    for mutat in range(0,mutlen):
        if muta[mutat].respawnFlag == True:
            score = score + 100
            muta[mutat] = Enemy(screen,random.randint(0,screen_width/5),random.randint(0,screen_height/10),None)
   
    #controls the fps, currently set to 50
    clock.tick(50)
  
    
    pygame.display.flip()
 
pygame.quit()

