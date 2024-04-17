import pygame

pygame.init()
debug_font = pygame.font.Font(None, 30)


def log_debug(info: any, y: int = 10, x: int = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = debug_font.render(str(info), True, "white")
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, "black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)


def display_fps(clock: pygame.Clock, window_width: float):
    display_surface = pygame.display.get_surface()
    fps_text = f"{clock.get_fps():.2f}"
    fps_surface: pygame.Surface = debug_font.render(fps_text, True, "white")
    fps_rect: pygame.Rect = fps_surface.get_rect(topright=(window_width - 10, 10))
    display_surface.blit(fps_surface, fps_rect)
    pygame.draw.rect(display_surface, "white", fps_rect.inflate(10, 10), width=2, border_radius=5)
