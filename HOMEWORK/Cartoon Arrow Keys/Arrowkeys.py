import pygame
from pygame.locals import*
import random


pygame.init()
screen=pygame.display.set_mode((600,270))

x=300
y=135
x2=100
y2=135
speed=1

score1 = 0
score2 = 0



player=pygame.image.load("cat.png")
background=pygame.image.load("corn.jpg")
player2=pygame.image.load("enemy.png")
mouse=pygame.image.load("mouse.png")

mousex = 300
mousey = 70

running=True
while running:

    screen.blit(background,(0,0))
    screen.blit(player,(x,y))
    screen.blit(player2,(x2,y2))
    screen.blit(mouse,(mousex, mousey))
    font = pygame.font.SysFont("Arial", 35)
    text = font.render("Snake's Score: "+str(score1), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    text2 = font.render("Cat's Score: "+str(score2), True, (255, 255, 255))
    screen.blit(text2, (250, 10))

    player_rect = pygame.Rect(x, y, player.get_width(), player.get_height())
    player2_rect = pygame.Rect(x2,y2, player2.get_width(), player2.get_height())
    mouse_rect = pygame.Rect(mousex, mousey, mouse.get_width(), mouse.get_height())

    if player_rect.colliderect(mouse_rect):
        score2 += 1

        mousex = random.randint(0, 600 - mouse.get_width())
        mousey = random.randint(0, 270 - mouse.get_height())

    if player2_rect.colliderect(mouse_rect):
        score1 += 1

        mousex = random.randint(0, 600 - mouse.get_width())
        mousey = random.randint(0, 270 - mouse.get_height())
    
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


