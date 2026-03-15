from typing import Any

from colorado.base.location import LocationEnum, Location


class WithCoordinates(Location):
    """
    A location with a latitude/longitude pair
    """
    latitude: float
    """
    The latitude of the location.
    """

    longitude: float
    """
    The longitude of the location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class WithCoordinatesEnum(LocationEnum):
    """
    An enumeration of WithCoordinates objects
    """

    def __init__(self, location: WithCoordinates):
        super().__init__(location)

    @property
    def latitude(self) -> float:
        """
        The latitude of the location.
        :return: The latitude of the location.
        :rtype: float
        """
        return self._location.latitude  # type: ignore

    @property
    def longitude(self) -> float:
        """
        The longitude of the location.
        :return: The longitude of the location.
        :rtype: float
        """
        return self._location.longitude  # type: ignore
