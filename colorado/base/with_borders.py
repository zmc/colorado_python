from typing import Any, Optional

from colorado.base.location import LocationEnum, Location


class WithBorders(Location):
    """
    A location with a polygon of its borders.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def coordinates_within_borders(self, latitude: float, longitude: float) -> bool:
        """
        Returns True if the provided latitude and longitude are within the borders of this location.
        :param latitude: The latitude to check.
        :param longitude: The longitude to check.
        :return: True if the provided latitude and longitude are within the borders of this location.
        :rtype: bool
        """
        raise NotImplementedError()


class WithBordersEnum(LocationEnum):
    """
    An enumeration of WithBorders objects
    """

    def __init__(self, location: WithBorders):
        super().__init__(location)

    def coordinates_within_borders(self, latitude: float, longitude: float) -> bool:
        """
        Returns True if the provided latitude and longitude are within the borders of this location.
        :param latitude: The latitude to check.
        :param longitude: The longitude to check.
        :return: True if the provided latitude and longitude are within the borders of this location.
        :rtype: bool
        """
        return self._location.coordinates_within_borders(latitude=latitude, longitude=longitude)

    @classmethod
    def from_coordinates(cls, latitude: float, longitude: float) -> Optional['WithBordersEnum']:
        """
        Returns the WithBordersEnum member that contains the provided latitude and longitude within its borders.
        :param latitude: The latitude to check.
        :param longitude: The longitude to check.
        :return: The WithBordersEnum member that contains the provided latitude and longitude within its borders, or None if no member contains the coordinates.
        :rtype: WithBordersEnum | None
        """
        for member in cls:
            if member.coordinates_within_borders(latitude=latitude, longitude=longitude):
                return member
        return None
