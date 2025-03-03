import pygame
import random
from core.settings import Settings
from game_objects.player import Player
from game_objects.enemy import Enemy
from game_objects.powerup import PowerUp

def run_game(screen):
    clock = pygame.time.Clock()
    settings = Settings()
    player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 60)
    enemies = []
    powerups = []
    enemy_spawn_timer = 0
    powerup_spawn_timer = 0

    running = True
    while running:
        screen.fill(settings.WHITE)
        player.draw(screen)

        enemy_spawn_timer += 1
        if enemy_spawn_timer > 30:
            enemy_spawn_timer = 0
            enemies.append(Enemy(random.randint(50, settings.SCREEN_WIDTH - 50), 0))

        powerup_spawn_timer += 1
        if powerup_spawn_timer > 200:
            powerup_spawn_timer = 0
            powerups.append(PowerUp(random.randint(50, settings.SCREEN_WIDTH - 50), 0))

        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
            if player.rect.colliderect(enemy.rect):
                return False

        for powerup in powerups:
            powerup.move()
            powerup.draw(screen)
            if player.rect.colliderect(powerup.rect):
                player.activate_powerup()
                powerups.remove(powerup)

        keys = pygame.key.get_pressed()
        player.move(keys)

        enemies = [enemy for enemy in enemies if enemy.rect.y < settings.SCREEN_HEIGHT]
        powerups = [powerup for powerup in powerups if powerup.rect.y < settings.SCREEN_HEIGHT]

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        clock.tick(60)
