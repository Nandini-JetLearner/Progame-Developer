import pygame
from pygame.locals import*
import random
import time

pygame.display.set_caption("Catch the Fruits!!!")

pygame.init()
screen=pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

player_x=200
player_y=300
speed=15
x=300
y=0
fruits=0
increase=5

player=pygame.image.load("basket.png")
background=pygame.image.load("corn.jpg")
apple=pygame.image.load("fruit.png")

font=pygame.font.SysFont("Times New Roman", 28)

running=True
start_time = pygame.time.get_ticks()
while running:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    screen.blit(apple,(x,y))
    Text = font.render("Fruits: ",False,(0,0,0))
    Text2 = font.render(str(fruits),False,(0,0,0))
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


    apple_rect = pygame.Rect(x, y, apple.get_width(), apple.get_height())
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

    y+=increase

    if player_rect.colliderect(apple_rect):
        fruits+=1
        print("Caught a fruit!")
        x=random.randint(20,520)
        y=0

    if fruits==15:
        print("Game Over!")
        running=False


    pygame.display.update()
    clock.tick(60)

end_time = pygame.time.get_ticks()
time_taken = (end_time - start_time) / 1000
print("Time Taken: ", time_taken)
    
pygame.quit()