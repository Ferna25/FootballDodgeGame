import pygame
import os
from core.settings import Settings

class Player:
    def __init__(self, x, y):
        self.settings = Settings()
        self.image = pygame.image.load(os.path.join("assets", "player.png"))
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.speed = 5
        self.powered_up = False
        self.powerup_timer = 0  # Vreme trajanja power-upa
        self.powerup_icon = None  # Čuva sliku aktivnog power-upa

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.settings.SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:  # Kretanje gore
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.settings.SCREEN_HEIGHT:  # Kretanje dole
            self.rect.y += self.speed


        self.hitbox.x = self.rect.x
        self.hitbox.y = self.rect.y

    def activate_powerup(self, powerup_image, duration=150):
        self.powered_up = True
        self.powerup_timer = duration
        self.powerup_icon = pygame.transform.scale(powerup_image, (30, 30))  # Skaliranje ikone

    def update(self):
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
        else:
            self.powered_up = False
            self.powerup_icon = None  # Uklanja ikonu kada power-up istekne

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def draw_progress_bar(self, screen):
        if self.powered_up:
            bar_width = 200
            bar_height = 20
            bar_x = self.settings.SCREEN_WIDTH - bar_width - 20
            bar_y = 20
            fill_width = (self.powerup_timer / 150) * bar_width  

            pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))  
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, fill_width, bar_height))  

            if self.powerup_icon:
                screen.blit(self.powerup_icon, (bar_x - 35, bar_y - 5))  # Prikaz slike pored progress bara
