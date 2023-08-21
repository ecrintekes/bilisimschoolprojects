import pygame
import random
import cv2
import mediapipe
import numpy

pygame.init()

dosya = cv2.VideoCapture(0)
dosya.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
dosya.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


FPS = 30
saat = pygame.time.Clock()
genislik = 1280
yukseklik = 720

skor = 0
can = 5
deger = 5
deger_2 = 10

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

dx2 = random.choice([-1,1])
dy2 = random.choice([-1,1])

goruntu_yuzeyi = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("monkey game")


karakter = pygame.image.load("monkey.png")
karakter_koordinati = karakter.get_rect()

x = 500
y = 300

banana = pygame.image.load("banana.png")
banana_koordinati = banana.get_rect()
banana_koordinati.center = (random.randint(50, genislik - 50), random.randint(50, yukseklik - 50))

lime = pygame.image.load("lime.png")
lime_koordinati = lime.get_rect()
lime_koordinati.center = (random.randint(50, genislik-50), random.randint(50, yukseklik-50))

x = random.randint(0, 255)
y = random.randint(0, 255)
z = random.randint(0, 255)

font = pygame.font.Font("Malgun gothic semilight.ttf", 32)

skor_metni = font.render("SKOR:" +str(skor), True, (x, y, z))
skor_metni_koordinati = skor_metni.get_rect()
skor_metni_koordinati.topleft = (10,10)

can_metni = font.render("CAN:" +str(can),True,(x, y, z))
can_metni_koordinati = can_metni.get_rect()
can_metni_koordinati.topright = (yukseklik-10,10)

ses_efekti_1 = pygame.mixer.Sound("winfinal.wav")
ses_efekti_2 = pygame.mixer.Sound("losefinal.wav")

pygame.mixer.music.load("backgroundfinal.wav")
pygame.mixer.music.play(-1,0.0)



el_model = mediapipe.solutions.hands


with el_model.Hands(min_tracking_confidence=0.5,min_detection_confidence=0.5) as el:
    while True:
        kontrol, webcam = dosya.read()
        yukseklik, genislik, kanal = webcam.shape
        rgb = cv2.cvtColor(webcam, cv2.COLOR_BGR2RGB)
        sonuc = el.process(rgb)
        if sonuc.multi_hand_landmarks:
            for hand_mark in sonuc.multi_hand_landmarks:
                for koordinat in el_model.HandLandmark:
                    mark = hand_mark.landmark[8]
                    x = int(mark.x*genislik)
                    y = int(mark.y*yukseklik)

        karakter_koordinati.center = (x, y)
        rgb = numpy.rot90(rgb)
        web_cam_goruntu_yuzeyi = pygame.surfarray.make_surface(rgb).convert()
        web_cam_goruntu_yuzeyi = pygame.transform.flip(web_cam_goruntu_yuzeyi, True, False)

        if banana_koordinati.colliderect(karakter_koordinati):
            banana_koordinati.x = random.randint(200, genislik - 200)
            banana_koordinati.y = random.randint(200, yukseklik - 200)

        banana_koordinati.x = banana_koordinati.x + (deger * dx)
        banana_koordinati.y = banana_koordinati.y + (deger * dy)

        if banana_koordinati.left < 0 or banana_koordinati.right > genislik:
            dx = -1 * dx
        if banana_koordinati.top < 0 or banana_koordinati.bottom > yukseklik:
            dy = -1 * dy


        if lime_koordinati.colliderect(karakter_koordinati):
            lime_koordinati.x = random.randint(200, genislik - 200)
            lime_koordinati.y = random.randint(200, yukseklik - 200)

        lime_koordinati.x = lime_koordinati.x + (deger * dx2)
        lime_koordinati.y = lime_koordinati.y + (deger * dy2)

        if lime_koordinati.left < 0 or lime_koordinati.right > genislik:
            dx2 = -1 * dx2
        if lime_koordinati.top < 0 or lime_koordinati.bottom > yukseklik:
            dy2 = -1 * dy2

        if banana_koordinati.colliderect(karakter_koordinati):
            skor += 1
            ses_efekti_1.play()
            deger += 1
            banana_koordinati.x = random.randint(50, genislik - 50)
            banana_koordinati.y = random.randint(50, yukseklik - 50)


        if lime_koordinati.colliderect(karakter_koordinati):
            can -= 1
            ses_efekti_2.play()
            lime_koordinati.x = random.randint(50, genislik - 50)
            lime_koordinati.y = random.randint(50, yukseklik - 50)



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

        goruntu_yuzeyi.blit(web_cam_goruntu_yuzeyi, (0, 0))
        goruntu_yuzeyi.blit(banana, banana_koordinati)
        goruntu_yuzeyi.blit(karakter, karakter_koordinati)
        goruntu_yuzeyi.blit(lime, lime_koordinati)

        pygame.display.update()
        saat.tick(FPS)
pygame.quit()
