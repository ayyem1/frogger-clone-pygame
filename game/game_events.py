from engine.events import CustomEventType


class GameEvents(CustomEventType):
    """
    Game specific events.
    Note: CustomEventType is an empty enum so it can be overriden like this.
    """
