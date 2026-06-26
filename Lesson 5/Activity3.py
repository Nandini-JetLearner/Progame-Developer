import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Cirlce follows your mouse!")

white=(255,255,255)
blue=(0,128,255)

running=True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
    mouse_x,mouse_y=pygame.mouse.get_pos()
    pygame.draw.circle(screen, blue,(mouse_x, mouse_y), 30)
    pygame.display.update()

pygame.quit()