from typing import Any

from colorado.base.location import LocationEnum, Location
from colorado.counties import Counties


class WithCounty(Location):
    """
    A location with counties.
    """
    counties: list[Counties]
    """
    The counties of the location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class WithCountyEnum(LocationEnum):
    """
    An enumeration for WithCounty objects.
    """

    def __init__(self, location: WithCounty):
        super().__init__(location)

    @property
    def counties(self) -> list[Counties]:
        """
        The counties of the location.
        :return: The counties of the location.
        :rtype: list[Counties]
        """
        return self._location.counties  # type: ignore
