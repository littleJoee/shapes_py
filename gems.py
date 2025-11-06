import random

class GemHub:
    def __init__(self, game, assets):
        self.game = game
        self.assets = assets
        self.pos = [200, 200]

        self.gem_types = ['circle', 'square', 'triangle', 'diamond']
        self.correct_dir = {'circle': [False, True, False, False],
                            'square': [False, False, False, True], 
                            'triangle': [False, False, True, False], 
                            'diamond': [True, False, False, False]}
        
        self.current_gem_type = self.gem_types[1]
        self.gem_map = []

    def update(self, direction, timer):
        if direction[0]: # left
            self.correct = False
            pos = (random.randint(0, 120), random.randint(150, 300))
        elif direction[1]: # right
            pos = (random.randint(380, 480), random.randint(150, 300))
        elif direction[2]: # up
            pos = (random.randint(200, 300), random.randint(0, 150))
        elif direction[3]:
            pos = (random.randint(200, 300), random.randint(300, 500))

        self.append_gem(pos)
        self.change_gem()
    
    def append_gem(self, pos):
        '''adds gem to a dictionary to keep track for drawing'''
        self.gem_map.append({'type': self.current_gem_type, 'pos': pos, 's': [3, 3]})

    def change_gem(self):
        '''change to a random gem'''
        self.current_gem_type = self.gem_types[random.randint(0, len(self.gem_types) - 1)]
    
    def funmode(self):
        '''dvd like bouncing'''
        # bouncing off side logic
        for gem in self.gem_map:
            if gem['pos'][0] <= 0 or gem['pos'][0] + 50 <= self.game.screen_width:
                gem['s'[0]] -= gem['s'[0]]
            elif gem['pos'][1] <= 0 or gem['pos'][1] + 50 <= self.game.screen_width:
                gem['s'[1]] -= gem['s'[1]]

            gem['pos'] += gem['s'[0]]
            gem['pos'] += gem['s'[1]]
        
    def is_correct(self, direction):
        if direction == self.correct_dir[self.current_gem_type]:
                return True
        else:
            return False
        


    # displays gem in te middle and other gems(appended to a dictionary and then drawn like tilemaps)
    def render(self, surf): 
        for gem in self.gem_map:
            surf.blit(self.assets[gem['type']], gem['pos'])
        surf.blit(self.assets[self.current_gem_type], self.pos)
