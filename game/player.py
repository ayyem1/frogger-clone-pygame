from os import path, walk

import pygame


class Player(pygame.sprite.Sprite):
    """
    TODO: Pull the animation portion of this sprite out into it's own class and
    put it in our engine code
    """

    MOVE_RIGHT_STATUS: str = "right"
    MOVE_LEFT_STATUS: str = "left"
    MOVE_UP_STATUS: str = "up"
    MOVE_DOWN_STATUS: str = "down"

    def __init__(self, pos: tuple[int, int], *groups) -> None:
        super().__init__(*groups)

        self.animations: dict[str, list[pygame.Surface]] = {}
        self.status = self.MOVE_DOWN_STATUS
        self.current_frame: float = 0.0
        self.animation_speed: float = 10.0

        self.import_assets()
        self.image = self.animations[self.status][int(self.current_frame)]

        self.rect = self.image.get_rect(center=pos)
        self.position = pygame.math.Vector2(self.rect.center)

        self.direction = pygame.math.Vector2()
        self.speed: float = 200.0

    def import_assets(self):
        for index, content in enumerate(walk("data/graphics/player")):
            if index == 0:
                for folder_name in content[1]:  # Second arg in tuple is list of folder names
                    self.animations[folder_name] = []
            else:
                for filename in content[2]:
                    filepath = path.normpath(path.join((content[0]), filename))
                    key = path.split(content[0])[1]  # Second element is name of the parent folder
                    if path.exists(filepath):
                        self.animations[key].append(pygame.image.load(filepath))
                    else:
                        print(f"Failed to find path for player animation. path={filepath}")

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
            self.status = self.MOVE_DOWN_STATUS
        elif self.direction.y < 0:
            self.status = self.MOVE_UP_STATUS
        elif self.direction.x > 0:
            self.status = self.MOVE_RIGHT_STATUS
        elif self.direction.x < 0:
            self.status = self.MOVE_LEFT_STATUS

    def handle_movement(self, dt: float):
        self.position += self.direction * self.speed * dt
        self.rect.center = (round(self.position.x), round(self.position.y))

    def animate(self, dt: float):
        if self.direction.length() == 0:
            self.current_frame = 0.0
        else:
            self.current_frame += self.animation_speed * dt
            if self.current_frame >= len(self.animations[self.status]):
                self.current_frame = 0.0

        self.image = self.animations[self.status][int(self.current_frame)]
