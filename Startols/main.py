# the main file where everything will run

import pygame
import sys
import math
import ButtonFunction

pygame.init()

#where the icon code should go (needs to be 32x32)


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
commonxpos = HEIGHT//11
commonypos = WIDTH//2.35
rarexpos = HEIGHT//4
rareypos = WIDTH//5
legendxpos = HEIGHT//1.2
legendypos = WIDTH//5
titlexpos = HEIGHT//1.8
titleypos = WIDTH//2.7

try:
    season_image = pygame.image.load("SeasonalEgg.png").convert_alpha()
    common_image = pygame.image.load("CommonEgg.png").convert_alpha()
    rare_image = pygame.image.load("RareEgg.png").convert_alpha()
    legend_image = pygame.image.load("LegendaryEgg.png").convert_alpha()
except pygame.error as message:
    print(f"Cannot load image: SeasonalEgg.png - {message}")

season_rect = season_image.get_rect()
scaled_season_egg = pygame.transform.scale(season_image, (season_width, season_height))
season_egg_rect = scaled_season_egg.get_rect(topleft=(seasonxpos, seasonypos))

common_rect = common_image.get_rect()
scaled_common_egg = pygame.transform.scale(common_image, (season_width, season_height))
common_egg_rect = scaled_common_egg.get_rect(topleft=(commonxpos, commonypos))

rare_rect = rare_image.get_rect()
scaled_rare_egg = pygame.transform.scale(rare_image, (season_width, season_height))
rare_egg_rect = scaled_rare_egg.get_rect(topleft=(rarexpos, rareypos))

legend_rect = legend_image.get_rect()
scaled_legend_egg = pygame.transform.scale(legend_image, (season_width, season_height))
legend_egg_rect = scaled_legend_egg.get_rect(topleft=(legendxpos, legendypos))

start_button = ButtonFunction.ButtonFunction("Start", titlexpos, titleypos +200, 100, 50, None)
buttons = [start_button]

amp = 20
frequency = 0.002

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(event)

    time = pygame.time.get_ticks()

    vertical_off = amp * math.sin(time * frequency)
    season_egg_rect.y = int(seasonypos + (vertical_off//-0.5))
    common_egg_rect.y = int(commonypos + (vertical_off//-0.9))
    rare_egg_rect.y = int(rareypos + (vertical_off//0.7))
    legend_egg_rect.y = int(legendypos + vertical_off)

    window.blit(bg_image, (0,0))
    window.blit(scaled_season_egg, season_egg_rect)
    window.blit(scaled_common_egg, common_egg_rect)
    window.blit(scaled_rare_egg, rare_egg_rect)
    window.blit(scaled_legend_egg, legend_egg_rect)

    pygame.draw.rect(window, WHITE, (titlexpos, titleypos, 100, 30), 0)

    for button in buttons:
        button.draw(window)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()