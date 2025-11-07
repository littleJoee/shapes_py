import pygame

IMG_PATH = 'assets/'

def load_image(name):
    img = pygame.image.load(IMG_PATH + name + '.png')
    img.set_colorkey((255, 255, 255))
    return img
    
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)