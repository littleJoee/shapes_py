import random

class GemHub:
    def __init__(self, game, gem_type, assets):
        self.game = game
        self.gem_type = gem_type
        self.assets = assets
        self.pos = [250, 250]

        self.gem_map = {}

    def update(self, direction):
        if direction[0] == True or direction[1] == True: 
            frame_movement = (direction[0] + random.randint(200, 500), direction[1] + random.randint(200, 500))
            self.append_gem(frame_movement)
    
    # adds gem to a dictionary to keep track for drawing
    def append_gem(self, frame_movement):
        pass

    def change_gem(self):
        pass

    # displays gem in te middle and other gems(appended to a dictionary and then drawn like tilemaps)
    def render(self, surf): 
        surf.blit(self.gem_type, self.pos)


        