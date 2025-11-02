import pygame

IMG_PATH = 'assets/'

def load_image(name):
    img = pygame.image.load(IMG_PATH + name + '.png')
    img.set_colorkey((255, 255, 255))
    return img