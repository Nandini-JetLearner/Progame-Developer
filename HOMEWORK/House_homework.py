import pygame
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("House Drawing")
BLUE=(135,206,250)
BROWN=(139,69,19)
RED=(245,0,0)
TAN=(205,133,63)

running=True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #Grass
    pygame.draw.rect(screen,(0,180,0),(0,210,600,350))
    pygame.draw.rect(screen,(0,195,0),(0,240,600,350))
    pygame.draw.rect(screen,(0,205,0),(0,270,600,350))
    #Building
    pygame.draw.rect(screen,BROWN,(200,200,200,180))
    pygame.draw.rect(screen,(100,60,19),(200,380,200,30))
    pygame.draw.polygon(screen, (190,0,0), [(170,210),(300,90),(430,210)])
    pygame.draw.polygon(screen, RED, [(180,200),(300,100),(420,200)])
    pygame.draw.rect(screen,(160,82,45),(270,265,60,115))
    pygame.draw.rect(screen,TAN,(275,270,50,110))
    #Tree
    pygame.draw.rect(screen,BROWN,(60,200,60,180))
    pygame.draw.polygon(screen, (0,130,0), [(30,200),(90,100),(150,200)])
    pygame.draw.polygon(screen, (0,130,0), [(25,260),(90,100),(155,260)])
    pygame.draw.polygon(screen, (0,130,0), [(25,320),(90,100),(155,320)])
    #Sun
    pygame.draw.circle(screen,(255,165,0),(470,100), 45)
    pygame.draw.circle(screen,(255,215,0),(470,100), 30)
    pygame.display.update()

pygame.quit()