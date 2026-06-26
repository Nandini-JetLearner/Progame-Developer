import pygame
pygame.init()

WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Birthday Greeting Animation!")

img=pygame.image.load("bg1.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))


while (True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    #Edwardian Script ITC
    font = pygame.font.SysFont("Monotype Corsiva",72, bold=False, italic=True)
    text1= font.render("Happy", True, (0,0,0))
    text2= font.render("Birthday!", True, (0,0,0))
    
    display_surface.blit(image,(0,0))
    display_surface.blit(text1,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    pygame.time.delay(2000)

    image2=pygame.image.load("bg2.jpg")

    font2 = pygame.font.SysFont("Arial", 36)
    text3= font.render("Wish you a bright future ahead.", True, (0,0,0))

    display_surface.blit(image2,(0,0))
    display_surface.blit(text3,(30,30))
    pygame.display.update()
    pygame.time.delay(2000)

    image3=pygame.image.load("bg3.jpg")
    
    display_surface.blit(image3,(0,0))
    pygame.display.update()
    pygame.time.delay(2000)


