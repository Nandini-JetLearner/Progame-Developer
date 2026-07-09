import pygame
from pygame.locals import*
from time import*

pygame.init()
screen=pygame.display.set_mode((600,400))

x=300
y=200
speed=1

running=True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
    
    keys=pygame.key.get_pressed()

    if keys[K_w]:
        y-=speed
        
    if keys[K_s]:
        y+=speed
        
    if keys[K_a]:
        x-=speed
        
    if keys[K_d]:
        x+=speed
    
    pygame.draw.rect(screen,(0,0,255),(x,y,40,40))
    pygame.display.update()

pygame.quit()