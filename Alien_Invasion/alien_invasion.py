import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    # Define initiation function
    def __init__(self):

        # Initiate the background through pygame package
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):

        while True:

            self._check_events()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1

    def _update_screen(self):
	# Re-draw the screen every loop
        self.screen.fill(self.settings.bg_color)
	# Show the plane in the screen
        self.ship.blitme()
        # Show the latest refreshed screen
        pygame.display.flip()


if __name__ == '__main__':

    #Set up object and run game
    ai = AlienInvasion()
    ai.run_game()
    
