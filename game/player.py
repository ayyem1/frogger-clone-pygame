
import pygame

from engine.assets import load_assets


class Player(pygame.sprite.Sprite):
    """
    TODO: Pull the animation portion of this sprite out into it's own class and
    put it in our engine code
    """

    MOVE_RIGHT: str = "right"
    MOVE_LEFT: str = "left"
    MOVE_UP: str = "up"
    MOVE_DOWN: str = "down"

    def __init__(self, pos: tuple[int, int], *groups) -> None:
        super().__init__(*groups)

        self.animations: dict[str, list[pygame.Surface]] = {
            self.MOVE_RIGHT: load_assets("data/graphics/player/right"),
            self.MOVE_LEFT: load_assets("data/graphics/player/left"),
            self.MOVE_UP: load_assets("data/graphics/player/up"),
            self.MOVE_DOWN: load_assets("data/graphics/player/down"),
        }
        self.action = self.MOVE_DOWN
        self.current_frame: float = 0.0
        self.animation_speed: float = 10.0

        self.image = self.animations[self.action][int(self.current_frame)]

        self.rect = self.image.get_rect(center=pos)
        self.position = pygame.math.Vector2(self.rect.center)

        self.direction = pygame.math.Vector2()
        self.speed: float = 200.0


    def update(self, dt: float):
        self.handle_input()
        self.handle_movement(dt=dt)
        # if self.check_animation_time():
        self.animate(dt=dt)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        # We convert the boolean sotred in keys to an int (0 or 1) to
        # determine the direction
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        if self.direction.length_squared() > 0:
            self.direction.normalize_ip()

        if self.direction.y > 0:
            self.action = self.MOVE_DOWN
        elif self.direction.y < 0:
            self.action = self.MOVE_UP
        elif self.direction.x > 0:
            self.action = self.MOVE_RIGHT
        elif self.direction.x < 0:
            self.action = self.MOVE_LEFT

    def handle_movement(self, dt: float):
        self.position += self.direction * self.speed * dt
        self.rect.center = (round(self.position.x), round(self.position.y))

    def animate(self, dt: float):
        if self.direction.length() == 0:
            self.current_frame = 0.0
        else:
            self.current_frame += self.animation_speed * dt
            if self.current_frame >= len(self.animations[self.action]):
                self.current_frame = 0.0

        self.image = self.animations[self.action][int(self.current_frame)]
