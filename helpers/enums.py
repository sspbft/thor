"""Different enums used in Thor."""
from enum import Enum


class Mode(Enum):
    """Models a mode in which Thor can be run."""

    local = 1
    planetlab = 2

    @classmethod
    def exists(cls, value):
        return any(value == item.value for item in cls)
