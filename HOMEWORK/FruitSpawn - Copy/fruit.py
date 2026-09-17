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
x2=400
y2=0
fruits=0
increase=5

player=pygame.image.load("basket.png")
background=pygame.image.load("corn.jpg")
apple=pygame.image.load("fruit.png")
banana=pygame.image.load("fruit2.png")
mouse_x,mouse_y=pygame.mouse.get_pos()

font=pygame.font.SysFont("Times New Roman", 28)

running=True
start_time = pygame.time.get_ticks()
while running:
    mouse_x,mouse_y=pygame.mouse.get_pos()

    screen.blit(background,(0,0))
    screen.blit(player,(mouse_x, mouse_y))
    screen.blit(apple,(x,y))
    screen.blit(banana,(x2,y2))
    Text = font.render("Fruits: ",False,(0,0,0))
    Text2 = font.render(str(fruits),False,(0,0,0))
    screen.blit(Text,(100,50)) 
    screen.blit(Text2,(180,50))
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

    if y >550:
        increase+=0.5
        x=random.randint(20,520)
        y=0

    if y2 >550:
            increase+=0.5
            x2=random.randint(20,520)
            y2=0

    apple_rect = pygame.Rect(x, y, apple.get_width(), apple.get_height())
    banana_rect = pygame.Rect(x2, y2, banana.get_width(), banana.get_height())
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())

    y+=increase
    y2+=increase

    if player_rect.colliderect(apple_rect):
        fruits+=1
        print("Caught an apple!")
        x=random.randint(20,520)
        y=0


    if player_rect.colliderect(banana_rect):
        fruits+=2
        print("Caught a banana!")
        x2=random.randint(20,520)
        y2=0


    if fruits==30 or fruits>30:
        print("Game Over!")
        print(str(fruits) + " Fruits Collected!")
        running=False


    pygame.display.update()
    clock.tick(60)

end_time = pygame.time.get_ticks()
time_taken = (end_time - start_time) / 1000
print("Time Taken: ", time_taken)
    
pygame.quit()