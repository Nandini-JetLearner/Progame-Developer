import pygame
import random
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Click the Circle!")

white=(255,255,255)

circle_x=300
circle_y=200
radius=100
circle_color=(0,128,255)

running=True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            distance= ((mouse_x-circle_x)*0*2 +(mouse_y-circle_y)**2)**0.5
            if distance<=radius:
                circle_color=(
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255))
                
    pygame.draw.circle(screen,circle_color,(circle_x,circle_y),radius)
    pygame.display.update()
pygame.quit()