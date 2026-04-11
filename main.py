# the main file where everything will run
import pygame
import sys
import time
from StartScreen import StartScreen
from LoadingScreen import LoadingScreen

class MainManager:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1000,800
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.shared_bg = pygame.image.load("Background Screen.png")
        self.shared_bg = pygame.transform.scale(self.shared_bg,(self.WIDTH,self.HEIGHT))

        self.states = {
            "START": StartScreen(self.WIDTH, self.HEIGHT),
            "LOADING": LoadingScreen(self.WIDTH, self.HEIGHT, self.shared_bg )
        }
        self.current_state = self.states["START"]


    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            new_state_key = self.current_state.handle_events(events)
            if new_state_key:
                self.current_state = self.states[new_state_key]


            self.current_state.update()
            self.current_state.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = MainManager()
    game.run()