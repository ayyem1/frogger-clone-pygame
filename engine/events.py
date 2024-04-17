from enum import Enum
from typing import Self, Union

import pygame


class CustomEventType(Enum):
    """
    Empty enum that can be overriden by games.
    This allows us to decouple the EventSystem from game logic.
    """

    pass


class EventSystem(object):
    """
    We reserve a slot in Pygame's event system for our game's custom events.
    Anything listening to events can use this slot by referencing
        EventSystem().user_event_slot
    Each of these events will have a subtype which will be in the CustomEventType
    enum. Game's will extend this enum with their own event types.
    """

    user_event_slot: int

    _instance: Union[Self, None] = None
    _custom_events: dict[CustomEventType, pygame.event.Event] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventSystem, cls).__new__(cls)
            cls._instance.user_event_slot = pygame.event.custom_type()

        return cls._instance

    def create_custom_event(self, **kwargs):
        """
        Creates a pygame event for a given event type.
        kwargs must contain custom_event_type: CustomEventType.
        kwargs can optionally contain event data.
        """
        custom_event_type: CustomEventType = kwargs.get("custom_event_type")
        if not custom_event_type:
            print("[Error] Event kwargs does not contain custom_event_type")
            return

        if custom_event_type in self._custom_events:
            print(
                f"[Warning] Event already exists. Will not create duplicate. event={custom_event_type}"
            )
            return

        self._custom_events[custom_event_type] = pygame.event.Event(
            self.user_event_slot, kwargs
        )

    def get_custom_event(
        self, custom_event_type: CustomEventType
    ) -> Union[pygame.event.Event, None]:
        if custom_event_type not in self._custom_events:
            return None

        return self._custom_events[custom_event_type]
