import pygame
from core.settings import Settings

def show_game_over(screen, result):
    clock = pygame.time.Clock()
    settings = Settings()
    running = True

    while running:
        screen.fill(settings.BLACK)
        message = "Game Over! Press ENTER to Restart" if not result else "You Lose!"
        game_over_text = settings.FONT.render(message, True, settings.WHITE)

        screen.blit(game_over_text, (300, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        clock.tick(30)
