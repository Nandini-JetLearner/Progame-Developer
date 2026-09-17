import pygame
from pygame.locals import*
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 700

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird!")

font = pygame.font.Sysfont("Arial",60)
white = (255,255,255)

ground_scroll = 0
scroll_speed = 0
flying = False
pipe_gap = 220
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

bg=pygame.image.load("assets/bg.png")
ground_img = pygame.image.load("assets/ground.png")
button_img = pygame.image.load("assets/restart.png")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def reset_game():
    pipe-group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height/2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)  #super.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0

        for num in range(1,4):
            img = pygame.image.load(f"asset/bird{num}.png")
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 668:
                self.rect.y += int(self.vel)
