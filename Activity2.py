import pygame
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("House Drawing")
WHITE=(255,255,255)
BROWN=(139,69,19)
RED=(255,0,0)
BLUE=(0,0,255)

running=True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    pygame.draw.rect(screen,(0,255,0),(100,280,370,250))
    pygame.draw.rect(screen,BROWN,(200,200,200,180))
    pygame.draw.polygon(screen, RED, [(180,200),(300,100),(420,200)])
    pygame.draw.rect(screen,BLUE,(270,280,60,100))
    pygame.display.update()

pygame.quit()