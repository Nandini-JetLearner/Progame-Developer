import pygame
from pygame.locals import*
import random
import time

pygame.display.set_caption("Dodge and Destroy the Enemies!")

pygame.init()
screen=pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

player_x=200
player_y=300
bullet_x=0
bullet_y=0
speed=15
x=300
y=0
lives=5
increase=5
bullets=[]


player=pygame.image.load("rocket.png")
background=pygame.image.load("space.png")
enemy=pygame.image.load("enemy.png")

font=pygame.font.SysFont("Times New Roman", 28)

running=True
start_time = pygame.time.get_ticks()
while running:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    screen.blit(enemy,(x,y))
    Text = font.render("Lives: ",False,(255,255,255))
    Text2 = font.render(str(lives),False,(255,255,255))
    screen.blit(Text,(100,50)) 
    screen.blit(Text2,(170,50))
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    if y >550:
        increase+=1
        x=random.randint(20,520)
        y=0


    enemy_rect = pygame.Rect(x, y, enemy.get_width(), enemy.get_height())
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())

    bullet=3
    for bullet in bullets:
            pygame.draw.rect(screen,(220,0,0), (0,0,220),(player_rect.x, player_rect.y))

    keys=pygame.key.get_pressed()
#MOVE
    if keys[K_LEFT]:
        player_x-=speed
    if keys[K_RIGHT]:
        player_x+=speed
    if keys[K_DOWN]:
        bullet_y += 10

    y+=increase

    if player_rect.colliderect(enemy_rect):
        lives-=1
        print("Lost a life!")
        x=random.randint(20,520)
        y=0

    if lives==0:
        print("Game Over!")
        running=False


    pygame.display.update()
    clock.tick(60)

end_time = pygame.time.get_ticks()
time_taken = (end_time - start_time) / 1000
print("Time Taken: ", time_taken)
    
pygame.quit()