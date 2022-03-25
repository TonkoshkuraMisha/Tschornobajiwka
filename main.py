import pygame

pygame.init()
bg_image = pygame.image.load('tank.jpg')

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.music.load("terminator_2.mp3")
pygame.mixer.music.play(loops=-1)

size = (850, 550)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tschornobajiwka forever!')

font = pygame.font.SysFont('Arial', 72)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

Tschornobajiwka1 = font.render('Чорнобаївка', True, BLUE)
Tschornobajiwka2 = font.render('Чорнобаївка', True, YELLOW)

x, y = 250, 600
clock = pygame.time.Clock()
FPS = 60
direct_y = -1

running = True
while running:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    # screen.fill(BLACK)

    screen.blit(Tschornobajiwka1, (x, y))
    screen.blit(Tschornobajiwka2, (x, y + 90))
    screen.blit(Tschornobajiwka1, (x, y + 180))
    screen.blit(Tschornobajiwka2, (x, y + 270))
    screen.blit(Tschornobajiwka1, (x, y + 360))
    screen.blit(Tschornobajiwka2, (x, y + 450))

    y += direct_y
    if y < -500:
        x, y = 250, 600
    pygame.display.update()
