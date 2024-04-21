import sys

import pygame

from engine.assets import AssetDatabase
from engine.debug import display_fps
from engine.events import EventSystem
from game.game_events import GameEvents
from game.player import Player
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self) -> None:
        # Init pygame
        pygame.init()

        # Init window
        pygame.display.set_caption(GAME_NAME)
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        AssetDatabase().load_animation_assets(
            key="player_right", base_path="data/graphics/player/right", convert_alpha=True
        )
        AssetDatabase().load_animation_assets(
            key="player_left", base_path="data/graphics/player/left", convert_alpha=True
        )
        AssetDatabase().load_animation_assets(key="player_up", base_path="data/graphics/player/up", convert_alpha=True)
        AssetDatabase().load_animation_assets(
            key="player_down", base_path="data/graphics/player/down", convert_alpha=True
        )

        # Init clock
        self.clock = pygame.time.Clock()

        # Init events
        for event_type in GameEvents:
            EventSystem().create_custom_event(custom_event_type=event_type)

        # Init game components
        self.entity_group = pygame.sprite.Group()
        self.player = Player((600, 400), self.entity_group)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == EventSystem().user_event_slot:
                    pass

            # Update
            dt: float = self.clock.tick(FPS) / 1000.0
            self.entity_group.update(dt=dt)

            # Draw
            self.display_surface.fill("black")
            display_fps(self.clock, WINDOW_WIDTH)
            self.entity_group.draw(self.display_surface)

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
