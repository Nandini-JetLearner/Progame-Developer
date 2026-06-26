import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill((0,0,0))
blue=(0,0,166)
pygame.display.update()

class Circle():
    def __init__(self,color,pos,rad,wid):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_rad=rad
        self.circle_wid=wid
        self.circle_surface=screen
    
    def draw_circle(self):
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_rad,self.circle_wid)
    
    def grow(self,r):
        self.circle_rad +=r
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos,self.circle_rad, self.circle_wid)

circle=Circle(blue,(300,300),25,0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            circle.draw_circle()
            pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill((0,0,0))
            circle.grow(20)
            pygame.display.update()

pygame.quit()