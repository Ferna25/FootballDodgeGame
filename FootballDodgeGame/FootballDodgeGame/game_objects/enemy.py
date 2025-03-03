"""
Modul koji definira klasu Enemy (State Pattern).

Klasa Enemy koristi **State Pattern**, jer omogućava promjenu stanja neprijatelja
(npr. prelazak iz "velikog" u "malog" kada igrač pokupi power-up).
"""

import pygame
import os
from core.settings import Settings

class Enemy:
    """Klasa koja predstavlja neprijatelja (Sergio Ramos) u igri."""

    def __init__(self, x, y, big=True):
        """Inicijalizira neprijatelja na zadanoj poziciji.

        Args:
            x (int): Početna X koordinata.
            y (int): Početna Y koordinata.
            big (bool): Ako je True, neprijatelj je veći; ako nije, manji.
        """
        self.settings = Settings()
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "assets", "enemy.png"))
        self.original_size = (120, 120) if big else (60, 60)
        self.image = pygame.transform.scale(self.image, self.original_size)

        # Kreiranje pravokutnika koji prati neprijatelja
        self.rect = self.image.get_rect(center=(x, y))

        # Smanjenje hitboxa za preciznije sudare
        hitbox_width = int(self.rect.width * 0.7)
        hitbox_height = int(self.rect.height * 0.7)
        self.hitbox = pygame.Rect(self.rect.x + (self.rect.width - hitbox_width) // 2,
                                  self.rect.y + (self.rect.height - hitbox_height) // 2,
                                  hitbox_width, hitbox_height)

        self.speed = 4

    def move(self):
        """Pomiče neprijatelja prema dolje i ažurira njegov hitbox."""
        self.rect.y += self.speed
        self.hitbox.y += self.speed  # Ažuriranje hitbox pozicije

    def resize(self, big):
        """Smanjuje neprijatelja kad igrač pokupi power-up.

        Args:
            big (bool): Ako je True, neprijatelj ostaje velik; ako nije, smanjuje se.
        """
        self.original_size = (120, 120) if big else (60, 60)
        self.image = pygame.transform.scale(self.image, self.original_size)
        self.rect = self.image.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))

        # Ažuriranje hitboxa
        hitbox_width = int(self.rect.width * 0.7)
        hitbox_height = int(self.rect.height * 0.7)
        self.hitbox = pygame.Rect(self.rect.x + (self.rect.width - hitbox_width) // 2,
                                  self.rect.y + (self.rect.height - hitbox_height) // 2,
                                  hitbox_width, hitbox_height)

    def draw(self, screen):
        """Iscrtava neprijatelja na ekranu.

        Args:
            screen (pygame.Surface): Površina na kojoj se crta neprijatelj.
        """
        screen.blit(self.image, self.rect)
