import pygame

class Ship:

    def __init__(self,ai_game):

        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

	# Load the ship image
        self.image = pygame.image.load('image/ship.bmp')

        self.rect = self.image.get_rect()

	# Put the ship image at the mid-bottom position of the screen
        self.rect.midbottom = self.screen_rect.midbottom
  
    def blitme(self):

	# Draw the ship at a given postion
        self.screen.blit(self.image, self.rect)
