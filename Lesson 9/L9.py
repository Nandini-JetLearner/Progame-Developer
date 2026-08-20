import pygame
pygame.init()

screen = pygame.display.set_mode((900,600))

pygame.display.set_caption("Match The Game to The Name!")

white=(255,255,255)
black=(0,0,0)
green=(0,150,0)
red=(200,0,0)

screen.fill(white)

subway = pygame.image.load("subway.png")
ludo = pygame.image.load("ludo.png")
temple=pygame.image.load("temple.png")
candy=pygame.image.load("candycrush.jpg")

font=pygame.font.SysFont("Times New Roman", 28)

images=[
    (subway,(100,80),"Subway Surfer"),
    (ludo,(100,180),"Ludo"),
    (temple,(100,280),"Temple Run"),
    (candy,(100,380),"Candy Crush")
]

right_names=[
    ("Ludo",(600,100)),
    ("Candy Crush",(600,200)),
    ("Subway Surfer", (600,300)),
    ("Temple Run",(600,400))
]

for img, pos, names in images:
    screen.blit(img,pos)
for text, pos in right_names:
    t=font.render(text,True,black)
    screen.blit(t, pos)

pygame.display.update()

selected_left = None
selected_pos = None
match_count = 0
wrong_match = False
total_attemts = 0

while True:
    event=pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        for img, pos, name in images:
            rect = img.get_rect(topleft=pos)
            if rect.collidepoint(x,y):
                selected_left = name
                selected_pos = (pos[0]+120, pos[1]+40)

        for text, pos in right_names:
            text_surface = font.render(text, True,black)
            text_rect = text_surface.get_rect(topleft=pos)

            if text_rect.collidepoint(x,y) and selected_left:
                pygame.draw.line(screen, black, selected_pos, (pos[0], pos[1]+15),3)

                pygame.display.update()

                total_attemts+=1

                if selected_left == text:
                    match_count +=1
                else:
                    wrong_match = True

                selected_left = None

        if total_attemts == 4:
            pygame.time.delay(1000)
            screen.fill(white)
            if wrong_match:
                result = font.render("LOSER", True, red)

            else:
                result = font.render("WINNER", True, green)

            screen.blit(result,(350,250))
            pygame.display.update()
            pygame.time.delay(1000)
            break