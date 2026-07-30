import pygame
from pygame.locals import*
import time

pygame.init()
screen=pygame.display.set_mode((500,350))

x=100
y=135
speed=10


cat1=pygame.image.load("cat1.png")
cat2=pygame.image.load("cat2.png")
background=pygame.image.load("tech.jpg")


def switch():
    screen.blit(cat2,(x,y))
    pygame.display.update()

running=True
while running:

    screen.blit(background,(0,0))
    screen.blit(cat1,(x,y))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    keys=pygame.key.get_pressed()
#MOVE
    if keys[K_UP]:
        y-=speed
        switch()
    if keys[K_DOWN]:
        y+=speed
        switch()
    if keys[K_LEFT]:
        switch()
        x-=speed
    if keys[K_RIGHT]:
        switch()
        x+=speed
        
       
   
    pygame.display.update()


pygame.quit()


