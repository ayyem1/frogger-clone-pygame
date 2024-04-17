from engine.events import CustomEventType


class GameEvents(CustomEventType):
    """
    Game specific events.
    Note: CustomEventType is an empty enum so it can be overriden like this.
    """

    PLAYER_PRIMARY_SHOOT = 1
    METEOR_TIMER_COMPLETE = 2
    SHIP_DESTROYED = 3
    METEOR_DESTROYED = 4
