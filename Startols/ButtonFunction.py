import pygame
import sys

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 32)

class ButtonFunction:
    def __init__(self, text, x, y, width, height, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = BUTTON_COLOR
        self.text_surface = font.render(text, True, TEXT_COLOR)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()