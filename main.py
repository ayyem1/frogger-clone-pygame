import sys

import pygame

from engine.debug import display_fps
from engine.events import EventSystem
from game.game_events import GameEvents
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self) -> None:
        # Init pygame
        pygame.init()

        # Init window
        pygame.display.set_caption(GAME_NAME)
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Init clock
        self.clock = pygame.time.Clock()

        # Init events
        for event_type in GameEvents:
            EventSystem().create_custom_event(custom_event_type=event_type)

        # Init game components

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == EventSystem().user_event_slot:
                    pass

            dt: float = self.clock.tick(FPS) / 1000.0

            self.display_surface.fill("black")

            display_fps(self.clock, WINDOW_WIDTH)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
