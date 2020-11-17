import pygame
import colors

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Fernanda Ferry & Yago Teixeira')

# cria o Rect para o quadrado
square = pygame.Rect(300, 230, 20, 20)

y_axis = 210

# cria o Rect para os pads
left_pad = pygame.Rect(20, y_axis, 10, 60)
right_pad = pygame.Rect(600, y_axis, 10, 60)

pads = [left_pad, right_pad]

velocity_x = 0.25

clock = pygame.time.Clock()

while True:
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

    if keys[pygame.K_UP]:
        y_axis += velocity_x

    screen.fill(colors.BLACK)

    # desenha o quadrado usando o Rect
    pygame.draw.rect(screen, colors.WHITE, square)

    # desenha os pads
    for pad in pads:
        pygame.draw.rect(screen, colors.WHITE, pad)

    pygame.display.update()