from typing import Any

from colorado._base import PlaceEnum, Place, PlaceAbbreviations


class Landmark(Place):
    """
    Represents a landmark in the state of Colorado.
    """
    regions: list[PlaceEnum]

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Landmarks(PlaceEnum):
    """
    An enumeration of notable landmarks in the state of Colorado.
    """
    PIKES_PEAK = Landmark(
        name="Pikes Peak",
        abbreviations=PlaceAbbreviations(
            three_letter="PPK",
            five_letter="PIKES",
            seven_letter="PIKESPK",
            fourteen_letter="PIKES PEAK"
        ),
        regions=[]
    )

    @property
    def regions(self) -> list[PlaceEnum]:
        """
        Get the list of regions that this landmark is located in.
        :return: A list of regions that this landmark is located in.
        """
        return self._place.regions  # type: ignore
