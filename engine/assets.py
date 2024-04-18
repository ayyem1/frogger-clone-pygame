
from os import listdir, path

import pygame


def load_assets(base_path: str) -> list[pygame.Surface]:
    animations: list[pygame.Surface] = []
    for filename in sorted(listdir(base_path)):
        filepath = path.normpath(path.join(base_path, filename))
        if path.exists(filepath):
            animations.append(pygame.image.load(filepath))
        else:
            print(f"Failed to find file for player animation. path={filepath}")

    return animations
