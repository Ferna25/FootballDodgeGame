"""
Football Dodge Game - Glavna datoteka za pokretanje igre.

Ova datoteka pokreće igru i povezuje sve module.
Koristi **Observer Pattern** za detekciju završetka igre i prelazak između scena.
"""

import sys
import os

# Postavljanje ispravnog putanje za module
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pygame
from scenes.menu import show_menu
from scenes.game import run_game
from scenes.game_over import show_game_over

def main():
    """Pokreće glavnu petlju igre, prikazuje meni i upravlja scenama."""
    pygame.init()
    from core.settings import Settings

    settings = Settings()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Football Dodge Game")
    
    while True:
        if show_menu(screen):
            game_result = run_game(screen)
            show_game_over(screen, game_result)

if __name__ == "__main__":
    main()
