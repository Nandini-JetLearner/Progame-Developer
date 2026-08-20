import pygame
from pygame.locals import*
import time

pygame.init()
screen=pygame.display.set_mode((500,350))

x=100
y=135
speed=1

cat1=pygame.image.load("cat1.png")
cat2=pygame.image.load("cat2.png")
background=pygame.image.load("tech.jpg")



running=True
while running:

    screen.blit(background,(0,0))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    moving  = False
    keys=pygame.key.get_pressed()
#MOVE
    if keys[K_UP]:
        y-=speed
        moving = True
    if keys[K_DOWN]:
        y+=speed
        moving = True
    if keys[K_LEFT]:
        x-=speed
        moving =True
    if keys[K_RIGHT]:
        x+=speed
        moving =True

    if moving:
        screen.blit(cat2, (x, y))
    else:
         screen.blit(cat1, (x, y))
   
    pygame.display.update()

pygame.quit()


