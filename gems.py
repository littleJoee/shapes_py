import random

class GemHub:
    def __init__(self, game, assets):
        self.game = game
        self.assets = assets
        self.pos = [200, 200]

        self.gem_types = ['circle', 'square', 'triangle', 'diamond']
        self.current_gem_type = self.gem_types[1]
        self.gem_map = []

    def update(self, direction):
        if direction[0]: # left
            pos = (random.randint(0, 200), random.randint(200, 300))
        elif direction[1]: # riht
            pos = (random.randint(300, 500), random.randint(200, 300))
        elif direction[2]: # up
            pos = (random.randint(200, 300), random.randint(0, 200))
        elif direction[3]:
            pos = (random.randint(200, 300), random.randint(300, 500))

        self.append_gem(pos)
        self.change_gem()
    
    def append_gem(self, pos):
        '''adds gem to a dictionary to keep track for drawing'''
        self.gem_map.append({'type': self.current_gem_type, 'pos': pos})
        print(self.gem_map)

    def change_gem(self):
        '''change to a random gem'''
        self.current_gem_type = self.gem_types[random.randint(0, len(self.gem_types) - 1)]

    # displays gem in te middle and other gems(appended to a dictionary and then drawn like tilemaps)
    def render(self, surf): 
        for gem in self.gem_map:
            surf.blit(self.assets[gem['type']], gem['pos'])
        surf.blit(self.assets[self.current_gem_type], self.pos)
