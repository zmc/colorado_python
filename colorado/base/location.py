import enum
from typing import Any

from colorado.internal import BaseModel


class Location(BaseModel):
    """
    A location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class LocationEnum(enum.Enum):
    """
    An enumeration for locations.
    """

    def __init__(self, location: Location):
        self._location = location
