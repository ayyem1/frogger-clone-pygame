from os import listdir, path
from typing import Self

import pygame


def load_assets(base_path: str, convert_alpha: bool = False) -> list[pygame.Surface]:
    """
    Helper method in case you don't want to go through the Asset Database

    Args:
        base_path (str): Path to folder that contains assets

    Returns:
        list[pygame.Surface]: List of assets loaded into pygame surfaces
    """
    animations: list[pygame.Surface] = []
    for filename in sorted(listdir(base_path)):
        filepath = path.normpath(path.join(base_path, filename))
        if path.exists(filepath):
            if convert_alpha:
                animations.append(pygame.image.load(filepath).convert_alpha())
            else:
                animations.append(pygame.image.load(filepath).convert())
        else:
            print(f"Failed to find file for player animation. path={filepath}")

    return animations


class AssetDatabase:
    """
    This class is responbile for holding all assets for your game.
    The internal structure is a dictionary of key to a list of assets.
    In the future, this will need to be cleaned up to use an Asset class,
    but for now this will do.

    If the asset is not part of an animation, the list will have only 1 item
    """

    _instance: Self | None = None
    _assets: dict[str, list[pygame.Surface]] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def load_animation_assets(self, key: str, base_path: str, convert_alpha: bool = False) -> list[pygame.Surface]:
        self._assets[key] = load_assets(base_path=base_path, convert_alpha=convert_alpha)

    def get_asset(self, key: str) -> list[pygame.Surface]:
        return self._assets[key]
