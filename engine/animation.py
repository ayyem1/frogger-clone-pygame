import pygame


class Animation:
    def __init__(self, images: list[pygame.Surface], img_dur: float = 5, loop: bool = True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done: bool = False
        self.frame: float = 0.0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self, dt: float):
        self.frame += dt
        # Reset or clamp frame depending on whether the animation is looping
        if self.loop and self.frame >= self.img_duration * len(self.images):
            self.frame = 0.0
        elif self.frame >= self.img_duration * len(self.images) - 1:
            self.frame = self.img_duration * len(self.images) - 1
            self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]
