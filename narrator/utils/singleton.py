class Singleton(type):
    """
    Singleton metaclass.
    This can be added to any class to make it a singleton.

    e.g.
    class GlobalSettings(metaclass=Singleton):
        pass

    usage:
    settings1 = GlobalSettings()
    settings2 = GlobalSettings()
    settings1 is settings2  # True
    """

    _instances = {}  # type: ignore

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
