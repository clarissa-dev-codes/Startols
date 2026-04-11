import pygame
import sys

import LoadingScreen

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 32)


class ButtonFunction:
    def __init__(self, text, x, y, width, height, action=None):

        self.image = pygame.image.load("Start Button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200,140))
        self.rect = self.image.get_rect(center=(x+100, y+50))

        self.text = text
        self.action = action

        # 3. Center the text on our new rect
        self.text_surface = font.render(text, True, (0, 0, 0))  # Using black for 'Start!'
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        # Draw the image using its own rect coordinates
        screen.blit(self.image, self.rect)

        # Draw text exactly in the center
        screen.blit(self.text_surface, self.text_rect)

        # DEBUG: The red box will now perfectly outline the PNG
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
