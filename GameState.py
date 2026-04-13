#handles the Game stuff behind the scenes
from Startol import Startol
import ButtonFunction
import pygame

class GameState:
    def __init__(self, width, height, background):
        self.pet = Startol("Bubbles")

        self.last_save_time = pygame.time.get_ticks()
        self.save_interval = 60000

        self.feed_btn = ButtonFunction.ButtonFunction("Feed", 100, 700, 100, 50,self.pet.feed)
        self.clean_btn = ButtonFunction.ButtonFunction("Clean", 250, 700, 100, 50,self.pet.clean)


    def update(self):
        self.pet.update_vitals()

        now = pygame.time.get_ticks()
        if now -self.last_save_time > self.save_interval:
            self.pet.save_game()
            self.last_save_time = now


    def draw(self, window):
        #Draw background and pet image here

        window.blit(self.pet_image, (self.width//2 -100, self.height//2-100))

        if self.showing_evolution_flash:
            pygame.draw.circle(window, (255,255,255), (self.width//2, self.height//2), 150 )
        pygame.draw.rect(window, (255,0,0), (50, 50, self.pet.stats["hunger"],20))
        pygame.draw.rect(window, (0,0,255), (50, 80, self.pet.stats["cleaniness"], 20))

        self.feed_btn.draw(window)
        self.clean_btn.draw(window)