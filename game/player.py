import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], *groups) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface((50, 50))
        self.image.fill("red")

        self.rect = self.image.get_rect(center=pos)
        self.position = pygame.math.Vector2(self.rect.center)

        self.direction = pygame.math.Vector2()
        self.speed: float = 200.0

    def update(self, dt: float):
        keys = pygame.key.get_pressed()
        # We convert the boolean sotred in keys to an int (0 or 1) to
        # determine the direction
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        if self.direction.length_squared() > 0:
            self.direction.normalize_ip()

        self.position += self.direction * self.speed * dt
        self.rect.center = (round(self.position.x), round(self.position.y))
