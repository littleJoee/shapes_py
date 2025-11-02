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

        self.images = {
            'circle': load_image('circle'),
            'diamond': load_image('diamond'),
            'square': load_image('square'),
            'triangle': load_image('triangle'),
        }
        self.direction = [False, False, False, False]

        self.Gem = GemHub(self, self.images) # idk how t do gem type

    def run(self): # numbers go brrr use bool instead and switch change to false if keyup
        is_pressed = False
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
                    if event.key == pygame.K_LEFT:
                        if not is_pressed:
                            is_pressed = True
                            self.direction[0] = True
                    if event.key == pygame.K_RIGHT:
                         if not is_pressed:
                            is_pressed = True
                            self.direction[1] = True
                    if event.key == pygame.K_UP:
                         if not is_pressed:
                            is_pressed = True
                            self.direction[2] = True
                    if event.key == pygame.K_DOWN:
                         if not is_pressed:
                            is_pressed = True
                            self.direction[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.direction[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.direction[1] = False
                    if event.key == pygame.K_UP:
                        self.direction[2] = False
                    if event.key == pygame.K_DOWN:
                        self.direction[3] = False
                    is_pressed = False

            # update to given dir
            if is_pressed:
                self.Gem.update(self.direction)
            # print(is_pressed, self.direction)
            is_pressed = False

            self.Gem.render(self.screen)
            pygame.display.update()
            self.clock.tick(60)

Game().run()