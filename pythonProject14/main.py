import pygame
import random

pygame.init()

FPS = 60
saat = pygame.time.Clock()

width = 1280
height = 720

skor = 0
can = 5
deger = 5
deger_2 = 10

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

dx2 = random.choice([-1,1])
dy2 = random.choice([-1,1])


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("monkey game")

karakter = pygame.image.load("monkey.png")
karakter_koordinati = karakter.get_rect()
karakter_koordinati.center = (width//2, height//2 + 200)

background = pygame.image.load("arkaplan.jpg")
background_koordinati = background.get_rect()
background_koordinati.topleft = (0,0)

banana = pygame.image.load("banana.png")
banana_koordinati = banana.get_rect()
banana_koordinati.center = (random.randint(50, width - 50), random.randint(50, height - 50))

lime = pygame.image.load("lime.png")
lime_koordinati = lime.get_rect()
lime_koordinati.center = (random.randint(50, width-50), random.randint(50, height-50))

x = random.randint(0, 255)
y = random.randint(0, 255)
z = random.randint(0, 255)

font = pygame.font.Font("Malgun gothic semilight.ttf", 32)

skor_metni = font.render("SKOR:" +str(skor), True, (x,y,z))
skor_metni_koordinati = skor_metni.get_rect()
skor_metni_koordinati.topleft = (10,10)

can_metni = font.render("CAN:" +str(can),True,(x,y,z))
can_metni_koordinati = can_metni.get_rect()
can_metni_koordinati.topright = (height-10,10)

ses_efekti_1 = pygame.mixer.Sound("winfinal.wav")
ses_efekti_2 = pygame.mixer.Sound("losefinal.wav")

pygame.mixer.music.load("backgroundfinal.wav")
pygame.mixer.music.play(-1,0.0)











durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and karakter_koordinati.left > 0:
        karakter_koordinati.x -= deger_2

    elif tus[pygame.K_RIGHT] and karakter_koordinati.right < width:
        karakter_koordinati.x += deger_2

    elif tus[pygame.K_UP] and karakter_koordinati.top > 0:
        karakter_koordinati.y -= deger_2

    elif tus[pygame.K_DOWN] and karakter_koordinati.bottom < height:
        karakter_koordinati.y += deger_2

    banana_koordinati.x = banana_koordinati.x + (deger * dx)
    banana_koordinati.y = banana_koordinati.y + (deger * dy)

    if banana_koordinati.left < 0 or banana_koordinati.right > width:
        dx = -1 * dx
    if banana_koordinati.top < 0 or banana_koordinati.bottom > height:
        dy = -1 * dy

    lime_koordinati.x = lime_koordinati.x + (deger * dx2)
    lime_koordinati.y = lime_koordinati.y + (deger * dy2)

    if lime_koordinati.left < 0 or lime_koordinati.right > width:
        dx2 = -1 * dx2
    if lime_koordinati.top < 0 or lime_koordinati.bottom > height:
        dy2 = -1 * dy2

    if banana_koordinati.colliderect(karakter_koordinati):
        skor += 1
        ses_efekti_1.play()
        deger += 1
        banana_koordinati.x = random.randint(50, width - 50)
        banana_koordinati.y = random.randint(50, height - 50)
        skor_metni = font.render("SKOR:" + str(skor), True, (x, y, z))

    if lime_koordinati.colliderect(karakter_koordinati):
        can -= 1
        ses_efekti_2.play()
        lime_koordinati.x = random.randint(50, width - 50)
        lime_koordinati.y = random.randint(50, height - 50)
        can_metni = font.render("CAN:" + str(can), True, (x, y, z))

    if can == 0:
        screen.blit(background, background_koordinati)
        pygame.mixer.music.stop()
        pygame.display.update()
        durdu = True
        while durdu:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key == pygame.K_SPACE:
                        durdu = False
                        skor = 0
                        can = 5
                        pygame.mixer.music.play(-1, 0.0)
                        can_metni = font.render("CAN:" + str(can), True, (x, y, z))
                        skor_metni = font.render("SKOR:" + str(skor), True, (x, y, z))
                if etkinlik.type == pygame.QUIT:
                    durdu = False
                    durum = False

    screen.fill((0, 0, 0))
    screen.blit(banana, banana_koordinati)
    screen.blit(lime, lime_koordinati)
    screen.blit(karakter, karakter_koordinati)
    screen.blit(skor_metni, skor_metni_koordinati)
    screen.blit(can_metni, can_metni_koordinati)






    pygame.display.update()
    saat.tick(FPS)



pygame.quit()
