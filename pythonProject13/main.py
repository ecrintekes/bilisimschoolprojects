import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tennis game")

player1_score = 0
player2_score = 0

player1_image = pygame.image.load("tennis (1).png")
player2_image = pygame.image.load("tennis.png")
ball = pygame.image.load("tennis (2).png")

player1_x = 50
player1_y = height // 2 - 50
player2_x = width - 50
player2_y = height // 2 - 50
ball_x = width // 2
ball_y = height // 2

ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

black = (0, 0, 0)

player1_score = 0
player2_score = 0


clock = pygame.time.Clock()

durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < height - 100:
        player1_y += 5
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < height - 100:
        player2_y += 5

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0:
        player2_score += 1
    if ball_x >= width:
        player1_score += 1


    if ball_x <= 0 or ball_x >= width:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0 or ball_y >= height:
        ball_speed_y = -ball_speed_y

    if player1_x <= ball_x <= player1_x + 10 and player1_y <= ball_y <= player1_y + 100:
        ball_speed_x = -ball_speed_x
    if player2_x - 10 <= ball_x <= player2_x and player2_y <= ball_y <= player2_y + 100:
        ball_speed_x = -ball_speed_x

    screen.fill(black)


    screen.blit(player1_image, (player1_x, player1_y))
    screen.blit(player2_image, (player2_x, player2_y))
    screen.blit(ball, (ball_x, ball_y))

    font = pygame.font.Font(None, 36)
    player1_text = font.render(f"Player 1: {player1_score}", True, (255, 255, 255))
    player2_text = font.render(f"Player 2: {player2_score}", True, (255, 255, 255))
    screen.blit(player1_text, (10, 10))
    screen.blit(player2_text, (width - player2_text.get_width() - 10, 10))



    pygame.display.update()
    clock.tick(60)










pygame.quit()
