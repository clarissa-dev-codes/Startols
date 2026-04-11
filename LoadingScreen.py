import pygame
import time
import threading

class LoadingScreen:
    def __init__(self, width, height, background):
        self.WIDTH = width
        self.HEIGHT = height
        self.bg_image = background
        self.is_loading = False
        self.next_state = None
        self.font = pygame.font.SysFont("Arial", 30)
        self.loading_wheel = pygame.image.load("Loading Wheel.png").convert_alpha()
        self.loading_wheel = pygame.transform.scale(self.loading_wheel, (130,100))
        self.angle = 0

        self.wheel_pos = (self.WIDTH - 100, self.HEIGHT - 100)



    def start_loading(self):
        def load_assets():
            time.sleep(7)
            self.next_state = "GAMEPLAY"

        if not self.is_loading:
            self.is_loading = True
            threading.Thread(target=load_assets, daemon=True).start()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit()

        state_signal = self.next_state
        self.next_state = None
        return state_signal

    def update(self):
        if not self.is_loading:
            self.start_loading()

        self.angle += 3.5
        if self.angle >= 360:
            time.sleep(0.5)
            self.angle = 0

    def draw(self, window):
        window.blit(self.bg_image, (0, 0))

        overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        window.blit(overlay, (0, 0))

        rotate_loading = pygame.transform.rotate(self.loading_wheel, self.angle)
        wheel_rect = rotate_loading.get_rect(center=self.wheel_pos)

        window.blit(rotate_loading, wheel_rect)

