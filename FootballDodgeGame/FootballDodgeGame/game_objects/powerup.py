"""
Modul koji definira klasu PowerUp.

PowerUp je objekt koji igrač može prikupiti kako bi promijenio stanje neprijatelja.
Koristi **Observer Pattern**, jer igrač prati stanje power-upa i reagira na prikupljanje.
"""


import pygame
import os
from core.settings import Settings

class PowerUp:
    """Klasa koja predstavlja power-up (Gatorade) u igri."""

    def __init__(self, x, y):
        """Inicijalizira power-up na zadanoj poziciji.

        Args:
            x (int): Početna X koordinata.
            y (int): Početna Y koordinata.
        """
        self.settings = Settings()
        self.image = pygame.image.load(os.path.join("assets", "powerup.png"))
        self.image = pygame.transform.scale(self.image, (40, 40))  # Power-up veličina
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3

    def move(self):
        """Pomiče power-up prema dolje."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Iscrtava power-up na ekranu.

        Args:
            screen (pygame.Surface): Površina na kojoj se crta power-up.
        """
        screen.blit(self.image, self.rect)
