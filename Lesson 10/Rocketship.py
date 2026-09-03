import pygame

pygame.init()

pygame.display.set_caption('Rocket in Space')
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode([screen_width, screen_height])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect=self.image.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
                    self.rect.move_ip(5,0)

        if self.rect.left<0:
            self.rect.left = 0
        elif self.rect.right>screen_width:
            self.rect.right = screen.width
        if self.rect.top<=0:
            self.rect,top=0
        elif self.rect.bottom>=screen_height:
            self.rect.bottom = screen_height
sprites = pygame.sprite.Group()
def startgame():
    player=Player()
    sprites.add(player)
    start_time=pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():

            if event.type == pygame == pygame.QUIT:
                pygame.quit()
                exit()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(pygame.image.load("space.png"),(0,0))
        sprites.draw(screen)
        pygame.display.update()

    end_time = pygame.time.get_ticks()
    time_taken = (end_time-start_time)/1000
    print("Time Taken: ",time_taken," seconds")

startgame()