import pygame
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.settings import Settings
from game_objects.player import Player
from game_objects.enemy import Enemy
from game_objects.powerup import PowerUp

def run_game(screen):
    clock = pygame.time.Clock()
    settings = Settings()
    player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 100)
    enemies = []
    powerups = []
    enemy_spawn_timer = 0
    powerup_spawn_timer = 0

    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    font = pygame.font.Font(None, 36)
    start_time = pygame.time.get_ticks()
    score = 0

    max_score = 1500  
    progress_bar_width = 300  
    progress_bar_height = 20  
    progress_bar_x = (settings.SCREEN_WIDTH - progress_bar_width) // 2  
    progress_bar_y = 20  

    running = True
    while running:
        screen.blit(background, (0, 0))  
        player.draw(screen)

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  
        score = elapsed_time * 10  

        if elapsed_time < 30:
            progress_color = (0, 150, 255)
        elif elapsed_time < 60:
            progress_color = (0, 200, 0)
        elif elapsed_time < 90:
            progress_color = (255, 165, 0)
        else:
            progress_color = (255, 0, 0)

        score_percentage = min(score / max_score, 1)  
        filled_width = int(progress_bar_width * score_percentage)  

        pygame.draw.rect(screen, (50, 50, 50), (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height), border_radius=10)
        pygame.draw.rect(screen, progress_color, (progress_bar_x, progress_bar_y, filled_width, progress_bar_height), border_radius=10)

        score_text = font.render(f"{score}", True, (255, 255, 255))
        screen.blit(score_text, (progress_bar_x + progress_bar_width // 2 - 20, progress_bar_y - 5))

        time_text = font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
        screen.blit(time_text, (20, 50))

        enemy_spawn_timer += 1
        if enemy_spawn_timer > 30:
            enemy_spawn_timer = 0
            new_enemy = Enemy(random.randint(50, settings.SCREEN_WIDTH - 50), 0, big=True)
            enemies.append(new_enemy)

        powerup_spawn_timer += 1
        if powerup_spawn_timer > 200:
            powerup_spawn_timer = 0
            powerups.append(PowerUp(random.randint(50, settings.SCREEN_WIDTH - 50), 0))

        for enemy in enemies:
            if hasattr(enemy, 'move'):  
                enemy.move()
                enemy.draw(screen)
            else:
                print("Greška: Objekt neprijatelja nema metodu move()!")

            if player.hitbox.colliderect(enemy.hitbox):
                return score  

        for powerup in powerups:
            powerup.move()
            powerup.draw(screen)

            if player.hitbox.colliderect(powerup.rect):
                player.activate_powerup(powerup.image)  # Prosleđujemo sliku power-upa
                for enemy in enemies:
                    enemy.resize(big=False)  
                powerups.remove(powerup)

        keys = pygame.key.get_pressed()
        player.move(keys)

        enemies = [enemy for enemy in enemies if enemy.rect.y < settings.SCREEN_HEIGHT]
        powerups = [powerup for powerup in powerups if powerup.rect.y < settings.SCREEN_HEIGHT]

        player.update()
        player.draw_progress_bar(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        clock.tick(60)
    
    return score
