import sys
import os
import math

from util import load_image, draw_text
from gems import GemHub
from guides import Guidelines
from timer import Timer

import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 500
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.clock = pygame.time.Clock()
        self.square = pygame.image.load('assets/square.png')
        self.square.set_colorkey((255, 255, 255))
        self.score_font = pygame.font.SysFont('arial', 30)
        self.font = pygame.font.SysFont('arial', 20)
        

        self.images = {
            'circle': load_image('circle'),
            'diamond': load_image('diamond'),
            'square': load_image('square'),
            'triangle': load_image('triangle'),
            'circle_g': load_image('guides/circle'),
            'diamond_g': load_image('guides/diamond'),
            'square_g': load_image('guides/square'),
            'triangle_g': load_image('guides/triangle'),
        }
        self.direction = [False, False, False, False]
        self.score = 0
        
        self.current_state = 'start'

        self.gem = GemHub(self, self.images) # idk how t do gem type
        self.guides = Guidelines(self.images)
        self.timer = Timer()

    def game_over(self):
        run = True
        while run:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_state = 'play'
                        run = False

            draw_text(str(self.score), self.score_font, (255, 255, 255), self.screen, 250, 250)
            draw_text('press space to play again', self.font, (255, 255, 255), self.screen, 200, 300)

            pygame.display.update()
            self.clock.tick(60)
            

    def state(self):
        pass

    def run(self): # numbers go brrr use bool instead and switch change to false if keyup
        is_pressed = False
        correct = False

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


            # start page
            if self.current_state == 'start':
                if is_pressed:
                    self.current_state = 'run'

            # play updates
            if self.current_state == 'run':
                if is_pressed:
                    self.guides.update(self.direction)
                    correct = self.gem.is_correct(self.direction)
                    if correct:
                        self.score += 1
                    self.gem.update(self.direction, self.current_state)

                self.timer.update(correct)
                if self.timer.timer <= 0:
                    self.current_state = 'game_over'
                is_pressed = False
                correct = False

            # game over updates
            if self.current_state == 'game_over':
                self.gem.funmode()
                draw_text(str(self.score), self.score_font, (255, 255, 255), self.screen, 250, 250)
                if is_pressed:
                    self.current_state = 'play'

            # renders
            self.timer.render(self.screen)
            self.gem.render(self.screen)
            self.guides.render(self.screen)
            pygame.display.update()
            self.clock.tick(60)

Game().run()