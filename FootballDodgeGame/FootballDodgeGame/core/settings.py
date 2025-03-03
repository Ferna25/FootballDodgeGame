"""
Postavke igre (Singleton Pattern).

Ova klasa implementira **Singleton Pattern**, jer osigurava da postoji samo
jedna instanca postavki igre koja se koristi u cijelom programu.
"""


import pygame

class Settings:
    """Singleton klasa za postavke igre."""

    def __init__(self):
        """Inicijalizira osnovne postavke igre."""
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        pygame.font.init()
        self.FONT = pygame.font.Font(None, 48)
