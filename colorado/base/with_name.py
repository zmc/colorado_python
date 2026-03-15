from typing import Any

from colorado.base.location import LocationEnum, Location


class WithName(Location):
    """
    A location with a name.
    """
    name: str
    """
    The name of the location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class WithNameEnum(LocationEnum):
    """
    An enumeration for named locations.
    """

    def __init__(self, location: WithName):
        super().__init__(location)

    @property
    def name(self) -> str:
        """
        The name of the location.
        :return: The name of the location.
        :rtype: str
        """
        return self._location.name  # type: ignore
