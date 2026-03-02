from typing import Any

from colorado._base import Place, PlaceEnum, PlaceAbbreviations


class UnincorporatedArea(Place):
    """
    Represents an unincorporated area in the state of Colorado.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class UnincorporatedAreas(PlaceEnum):
    """
    An enumeration of unincorporated areas in the state of Colorado.
    """
    HIGHLANDS_RANCH = UnincorporatedArea(
        name="Highlands Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="HLD",
            five_letter="HGHLN",
            seven_letter="HGHLND",
            fourteen_letter="HIGHLANDSRANCH"
        )
    )
    HENDERSON = UnincorporatedArea(
        name="Henderson",
        abbreviations=PlaceAbbreviations(
            three_letter="HND",
            five_letter="HENDR",
            seven_letter="HENDRSN",
            fourteen_letter="HENDERSON"
        )
    )
