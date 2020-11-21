import pygame
from pygame import time
from pygame import mixer
from colors import WHITE, BLUE, RED, GREEN, BLACK

pygame.init()
mixer.init()

screen = pygame.display.set_mode((640, 480))
done = False

pygame.display.set_caption('Fernanda & Yago')

scoreboard = {
    "green":0, 
    "red":0
    } 

font = pygame.font.SysFont("comicsansms", 30)

# cria o Rect para o quadrado
square = pygame.Rect(300, 230, 20, 20)

direction = 0
bip = 0

# cria o Rect para os pads
left_pad = pygame.Rect(20, 210, 10, 60)
right_pad = pygame.Rect(600, 210, 10, 60)
pads = [left_pad, right_pad]

velocity_x = 0.40
velocity_y = 0.60

clock = pygame.time.Clock()

mixer.music.set_volume(0.7)

while not done:
    dt = clock.tick(60)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # usa a função move inplace
    square.move_ip(velocity_x * dt, 0)

    # checa por colisão com os pads
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    keys = pygame.key.get_pressed()

    screen.fill(BLACK)

    # Circle config
    pygame.draw.circle(screen, BLUE, (50, 50), square)
    
    redScore = font.render(str(scoreboard['red']), True, RED)
    greenScore = font.render(str(scoreboard['green']), True, GREEN)

    if square.x < 0 or square.x > 640:
        if square.x < 0:
            scoreboard['green'] += 1
            mixer.music.load("perda.mp3")
            mixer.music.play()
        if square.x > 640:
            scoreboard['red'] += 1
            mixer.music.load("ponto.mp3")
            mixer.music.play()
        print(scoreboard)
        square = pygame.Rect(300, 230, 20, 20)

    #Left Pad Config
    if keys[pygame.K_UP]:
        if left_pad.y >= 60:
            left_pad.move_ip(0, -8)

    if left_pad.y <= 420:
        if keys[pygame.K_DOWN]:
            left_pad.move_ip(0, 8)    

    pygame.draw.rect(screen, RED, left_pad)
    
    #Right Pad Config
    right_pad.move_ip(0, velocity_y * dt)
    if right_pad.y > 420:
        velocity_y = -velocity_y
    if right_pad.y < 60:
        velocity_y = -velocity_y

    screen.blit(redScore, (20, 0))
    screen.blit(greenScore, (460, 0))

    pygame.draw.rect(screen, GREEN, right_pad)


    #ESC button
    if keys[pygame.K_ESCAPE]:
        mixer.music.load("the-end.mp3")
        mixer.music.play()
        done = True

    pygame.display.update()
        

done = False

font = pygame.font.SysFont("comicsansms", 72)
fim = font.render("FIM DE JOGO", True, WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    screen.fill((0, 0, 0))
    screen.blit(fim, (320 - fim.get_width() // 2, 240 - fim.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)


