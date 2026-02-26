# the main file where everything will run

import pygame
import sys
import math

pygame.init()

#this is measured in pixels
WIDTH, HEIGHT = 1000, 800


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stardols")

#background loading
try:
    bg_image = pygame.image.load("Background Screen.png").convert()

    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
except pygame.error as message:
    print(f"Cannot load image: Background Screen.png - {message}")
    exit()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

#the objects (eggs and title screen for now)
season_width = 130
season_height = 100

seasonxpos = HEIGHT//1
seasonypos = WIDTH//2.35
commonxpos = HEIGHT//9.94
commonypos = WIDTH//2.35
rarexpos = HEIGHT//3
rareypos = WIDTH//5
legendxpos = HEIGHT//1.2
legendypos = WIDTH//5

try:
    season_image = pygame.image.load("SeasonalEgg.png").convert_alpha()
except pygame.error as message:
    print(f"Cannot load image: SeasonalEgg.png - {message}")

season_rect = season_image.get_rect()
scaled_season_egg = pygame.transform.scale(season_image, (season_width, season_height))
season_egg_rect = scaled_season_egg.get_rect(topleft=(seasonxpos, seasonypos))

#season_rect = pygame.Rect(seasonxpos, seasonypos, season_width, season_height)
common_rect = pygame.Rect(commonxpos, commonypos, season_width, season_height)
rare_rect = pygame.Rect(rarexpos, rareypos, season_width, season_height)
legend_rect = pygame.Rect(legendxpos, legendypos, season_width, season_height)


amp = 20
frequency = 0.002

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = pygame.time.get_ticks()

    vertical_off = amp * math.sin(time * frequency)
    season_egg_rect.y = int(seasonypos + (vertical_off//-0.5))
    common_rect.y = int(commonypos + (vertical_off//-0.9))
    rare_rect.y = int(rareypos + (vertical_off//0.7))
    legend_rect.y = int(legendypos + vertical_off)

    window.blit(bg_image, (0,0))
    window.blit(scaled_season_egg, season_egg_rect)

    pygame.draw.rect(window, WHITE, common_rect)
    pygame.draw.rect(window, WHITE, rare_rect)
    pygame.draw.rect(window, WHITE, legend_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()