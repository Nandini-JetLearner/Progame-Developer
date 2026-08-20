import pygame
from pygame.locals import*
import random
import time

pygame.init()
screen=pygame.display.set_mode((600,600))

player_x=200
player_y=300
speed=1
x=300
y=0
lives=5

player=pygame.image.load("rocket.png")
background=pygame.image.load("space.png")
asteroid=pygame.image.load("spaceship_red (1).png")

running=True
while running:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    screen.blit(asteroid,(x,y))
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    if y >550:
        x=random.randint(0,200)
        y=0


    asteroid_rect = pygame.Rect(x, y, asteroid.get_width(), asteroid.get_height())
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())

    
    keys=pygame.key.get_pressed()
#MOVE
    if keys[K_UP]:
        player_y-=speed
    if keys[K_DOWN]:
        player_y+=speed
    if keys[K_LEFT]:
        player_x-=speed
    if keys[K_RIGHT]:
        player_x+=speed

    y+=1

    if player_rect.colliderect(asteroid_rect):
        lives-=1
        print("Lost a life!")
        x=random.randint(0,200)
        y=0

    if lives==0:
        print("Game Over!")
        running=False

    pygame.display.update()
    
pygame.quit()