from pygame.draw import circle

class Timer:
    def __init__(self):
        self.max_timer = 200
        self.timer = 200
        self.color = (0, 0, 28)
        self.center = (250, 250)

    def update(self, correct):
        self.timer -= 1.5
        # math for circle size
        if correct:
            self.timer = min(self.timer + 60, self.max_timer)

    def reset(self):
        self.timer = self.max_timer

    def render(self, surf):
        circle(surf, self.color, self.center, self.timer, 15)