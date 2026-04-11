import pygame
import math
import ButtonFunction

class StartScreen:
    def __init__(self, width, height):
        self.WIDTH, self.HEIGHT = width, height
        self.WHITE = (255, 255, 255)

        self.bg_image = pygame.image.load('Background Screen.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))

        self.season_width, self.season_height = 130, 100
        self.setup_eggs()

        self.titlexpos, self.titleypos = self.HEIGHT // 1.8, self.WIDTH // 2.7
        self.start_button = ButtonFunction.ButtonFunction(" ", self.titlexpos-40, self.titleypos+150, 100, 50, self.on_start_click)
        self.next_state = None

    def setup_eggs(self):
        self.seasonxpos = self.HEIGHT // 1
        self.seasonypos = self.WIDTH // 2.35
        self.commonxpos = self.HEIGHT // 11
        self.commonypos = self.WIDTH // 2.35
        self.rarexpos = self.HEIGHT // 4
        self.rareypos = self.WIDTH // 5
        self.legendxpos = self.HEIGHT // 1.2
        self.legendypos = self.WIDTH // 5

        season_image = pygame.image.load("SeasonalEgg.png").convert_alpha()
        common_image = pygame.image.load("CommonEgg.png").convert_alpha()
        rare_image = pygame.image.load("RareEgg.png").convert_alpha()
        legend_image = pygame.image.load("LegendaryEgg.png").convert_alpha()

        self.season_rect = season_image.get_rect()
        self.scaled_season_egg = pygame.transform.scale(season_image, (self.season_width, self.season_height))
        self.season_egg_rect = self.scaled_season_egg.get_rect(topleft=(self.seasonxpos, self.seasonypos))

        self.common_rect = common_image.get_rect()
        self.scaled_common_egg = pygame.transform.scale(common_image, (self.season_width, self.season_height))
        self.common_egg_rect = self.scaled_common_egg.get_rect(topleft=(self.commonxpos, self.commonypos))

        rare_rect = rare_image.get_rect()
        self.scaled_rare_egg = pygame.transform.scale(rare_image, (self.season_width, self.season_height))
        self.rare_egg_rect = self.scaled_rare_egg.get_rect(topleft=(self.rarexpos, self.rareypos))

        legend_rect = legend_image.get_rect()
        self.scaled_legend_egg = pygame.transform.scale(legend_image, (self.season_width, self.season_height))
        self.legend_egg_rect = self.scaled_legend_egg.get_rect(topleft=(self.legendxpos, self.legendypos))


    def on_start_click(self):
        print("Start Button Clicked")
        self.next_state = "LOADING"

    def handle_events(self, events):
        for event in events:
            self.start_button.handle_event(event)

        if self.next_state:
            state_signal = self.next_state
            self.next_state = None
            return state_signal
        return None

    def update(self):
        time = pygame.time.get_ticks()
        amp, frequency = 20, 0.002
        vertical_off = amp * math.sin(time * frequency)
        self.season_egg_rect.y = int(self.seasonypos + (vertical_off // -0.5))
        self.common_egg_rect.y = int(self.commonypos + (vertical_off // -0.9))
        self.rare_egg_rect.y = int(self.rareypos + (vertical_off // 0.7))
        self.legend_egg_rect.y = int(self.legendypos + vertical_off)


    def draw(self, window):
        window.blit(self.bg_image, ((0,0)))
        window.blit(self.scaled_season_egg, self.season_egg_rect)
        window.blit(self.scaled_common_egg, self.common_egg_rect)
        window.blit(self.scaled_rare_egg, self.rare_egg_rect)
        window.blit(self.scaled_legend_egg, self.legend_egg_rect)
        pygame.draw.rect(window, self.WHITE, (self.titlexpos, self.titleypos, self.season_width, self.season_height))
        self.start_button.draw(window)
