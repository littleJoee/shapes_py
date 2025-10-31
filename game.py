import sys
import os
import math

from util import load_image
from gems import GemHub

import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500, 500), 0, 32)
        self.clock = pygame.time.Clock()
        self.square = pygame.image.load('assets/square.png')
        self.square.set_colorkey((255, 255, 255))

        self.assets = {
            'circle': load_image('circle'),
            'diamond': load_image('diamond'),
            'square': load_image('square'),
            'triangle': load_image('triangle'),
        }

        self.Gem = GemHub(self, assets) # idk how t do gem type

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            # self.screen.blit(self.square, (100, 100))
            self.Gem.render(self.screen)
            pygame.display.update()
            self.clock.tick(60)

Game().run()