class Guidelines:
    def __init__(self, assets):
        self.assets = assets

        self.disable = False
        self.dir = [False, False, False, False]

        self.pos = [
            (18, 230), # red diamon on left 
            (430, 230), # yellow circle on right
            (230, 18), # blue square down
            (230, 420)  # green triangle up
        ]
        self.guides = {
            'left': (self.assets['diamond_g'], self.pos[0]),
            'right': (self.assets['circle_g'], self.pos[1]),
            'up': (self.assets['triangle_g'], self.pos[2]),
            'down': (self.assets['square_g'], self.pos[3])
        }
    
    def update(self, direction):
        for i in range(0, 4):
            if direction[i] == True:
                self.dir[i] = direction[i] 

        self.disable = all(self.dir)

    def reset(self):
        self.disable = False
        self.dir = [False, False, False, False]
    
    def render(self, surf):
        if not self.disable:
            for img in self.guides:
                surf.blit(self.guides[img][0], self.guides[img][1])