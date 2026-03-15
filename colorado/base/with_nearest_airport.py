from typing import Any

from colorado.airports import Airports
from colorado.base.location import LocationEnum, Location


class WithNearestAirport(Location):
    """
    A location with a nearest Colorado airport.
    """
    nearest_airport: Airports
    """
    The nearest airport to this location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class WithNearestAirportEnum(LocationEnum):
    """
    An enumeration of WithNearestAirport objects
    """

    def __init__(self, location: WithNearestAirport):
        super().__init__(location)

    @property
    def nearest_airport(self) -> Airports:
        """
        The nearest airport to this location.
        :return: The nearest airport to this location.
        :rtype: Airports
        """
        return self._location.nearest_airport  # type: ignore
