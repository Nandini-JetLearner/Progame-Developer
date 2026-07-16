import pygame
from pygame.locals import*


pygame.init()
screen=pygame.display.set_mode((600,270))

x=300
y=135
x2=100
y2=135
speed=1


player=pygame.image.load("cat.png")
background=pygame.image.load("corn.jpg")
player2=pygame.image.load("enemy.png")
mouse=pygame.image.load("mouse.png")

running=True
while running:

    screen.blit(background,(0,0))
    screen.blit(player,(x,y))
    screen.blit(player2,(x2,y2))
    screen.blit(mouse(300,70))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
            
    keys=pygame.key.get_pressed()
#MOVE
    if keys[K_UP]:
        y-=speed
    if keys[K_DOWN]:
        y+=speed
    if keys[K_LEFT]:
        x-=speed
    if keys[K_RIGHT]:
        x+=speed

    if keys[K_w]:
        y2-=speed
    if keys[K_s]:
        y2+=speed
    if keys[K_a]:
        x2-=speed
    if keys[K_d]:
        x2+=speed
#BORDER
    if x<0:
        x+=5
    if x>530:
        x-=5
    if y<0:
        y+=5
    if y>200:
        y-=5
       
    if x2<0:
        x2+=5
    if x2>530:
        x2-=5
    if y2<0:
        y2+=5
    if y2>200:
        y2-=5
    

    
    pygame.display.update()


pygame.quit()



"""screen.blit(mouse,(400,115))
mouse=pygame.image.load("mouse.png")"""