import pygame
pygame.init()
WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Harry Potter Lesson Animation!🪄")


img=pygame.image.load("img1.jpeg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while (True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    #Edwardian Script ITC
    font = pygame.font.SysFont("Monotype Corsiva",72, bold=False, italic=True)
    font2 = pygame.font.SysFont("Arial", 40, bold=False, italic=True)
    font3 = pygame.font.SysFont("Arial", 26, bold=False, italic=True)

#IMAGE 1
    text1= font.render("Harry", True, (255,255,255))
    text2= font.render("Potter", True, (255,255,255))
    text3= font.render("Lesson!", True, (255,255,255))

    display_surface.blit(image,(0,0))
    display_surface.blit(text1,(130,160))
    display_surface.blit(text2,(110,244))
    display_surface.blit(text3,(110,322))

    pygame.display.update()
    pygame.time.delay(2000)


#IMAGE 2
    image2=pygame.image.load("img2.png")
    text4= font2.render("Harry Potter is ", True, (0,0,0))
    text5= font2.render("a book series written ", True, (0,0,0))
    text6= font2.render("by J.K. Rowling.", True, (0,0,0))

    display_surface.blit(image2,(0,0))
    display_surface.blit(text4,(30,75))
    display_surface.blit(text5,(30,120))
    display_surface.blit(text6,(30,165))

    pygame.display.update()
    pygame.time.delay(2000)


#IMAGE 3
    image3=pygame.image.load("img3.jpg")
    text7= font2.render("Harry Potter's parents were killed ", True, (0,0,0))
    text8= font2.render("by the evil wizard Voldemort, ", True, (0,0,0))
    text9= font2.render("who tried to kill Harry, but ", True, (0,0,0))
    text10= font2.render("he mysteriously disappeared instead. ", True, (0,0,0))

    display_surface.blit(image3,(0,0))
    display_surface.blit(text7,(20,120))
    display_surface.blit(text8,(20,180))
    display_surface.blit(text9,(20,240))
    display_surface.blit(text10,(20,300))

    pygame.display.update()
    pygame.time.delay(2000)

    
#IMAGE 4
    image4=pygame.image.load("img4.jpg")
    text11= font3.render("Harry Potter grew up with his normal aunt & uncle, who ", True, (0,0,0))
    text12= font3.render("hated magic. On Harry's 11th B-day, a stranger named ", True, (0,0,0))
    text13= font3.render("Hagrid arrived, told Harry he was a wizard, and set ", True, (0,0,0))
    text14= font3.render("him on his way on a train to ", True, (0,0,0))
    text15= font3.render("Hogwarts School of Witchcraft ", True, (0,0,0))
    text16= font3.render("and Wizardry!", True, (0,0,0))

    display_surface.blit(image4,(0,0))
    display_surface.blit(text11,(15,80))
    display_surface.blit(text12,(15,140))
    display_surface.blit(text13,(15,200))
    display_surface.blit(text14,(15,260))
    display_surface.blit(text15,(15,320))
    display_surface.blit(text16,(15,380))

    pygame.display.update()
    pygame.time.delay(2000)


#IMAGE 5
    image5=pygame.image.load("img5.jpg")
    text17= font2.render("At Hogwarts, Harry met his best friends: Ron  ", True, (255,255,255))
    text18= font2.render("and Hermione. Ron was super funny ", True, (255,255,255))
    text19= font2.render("and Hermione was a bit of a know-it-all!", True, (255,255,255))

    display_surface.blit(image5,(0,0))
    display_surface.blit(text17,(30,250))
    display_surface.blit(text18,(30,290))
    display_surface.blit(text19,(30,330))

    pygame.display.update()
    pygame.time.delay(2000)

#Image 6 
    image5=pygame.image.load("img5.jpg")
    text20= font2.render("Through out the years, ", True, (255,255,255))
    text21= font2.render("the trio went on many adventures together.", True, (255,255,255))
 

    display_surface.blit(image3,(0,0))
    display_surface.blit(text20,(30,250))
    display_surface.blit(text21,(30,290))
    
    pygame.display.update()
    pygame.time.delay(2000)


#Image 7
    image5=pygame.image.load("img5.jpg")
    text22= font2.render("Finally at the battle of Hogwarts, ", True, (255,255,255))
    text23= font2.render("Harry Potter vanquished Voldemort!", True, (255,255,255))
 

    display_surface.blit(image1,(0,0))
    display_surface.blit(text22,(30,250))
    display_surface.blit(text23,(30,290))
    
    pygame.display.update()
    pygame.time.delay(2000)

pygame.quit()