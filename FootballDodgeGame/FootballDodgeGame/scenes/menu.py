import pygame
import sys
import os
from core.settings import Settings

def show_menu(screen):
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    running = True

    # Učitavanje pozadine
    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    title_font = pygame.font.Font(None, 72)  # Veći font za naslov
    blink_font = pygame.font.Font(None, 48)  # Font za trepćući tekst

    show_text = True  # Varijabla za efekt treperenja teksta
    frame_counter = 0  # Brojač za treperenje

    while running:
        screen.blit(background, (0, 0))  # Postavi pozadinsku sliku

        # Prikaz naslova s efektom sjene
        title_text = title_font.render("Football Dodge Game", True, (255, 215, 0))  # Zlatna boja
        shadow = title_font.render("Football Dodge Game", True, (50, 50, 50))  # Siva sjena

        screen.blit(shadow, (202, 152))  # Sjena blago pomaknuta
        screen.blit(title_text, (200, 150))  # Pravi tekst

        # Efekt treperenja za "Press ENTER to Start"
        frame_counter += 1
        if frame_counter % 30 < 15:  # Svakih pola sekunde mijenja vidljivost
            start_text = blink_font.render("Press SPACE to Start", True, (255, 255, 255))
            screen.blit(start_text, (250, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Započinje igra

        clock.tick(30)
