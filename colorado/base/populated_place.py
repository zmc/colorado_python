from typing import Any

from colorado.base.with_abbreviations import WithAbbreviations, WithAbbreviationsEnum, Abbreviations
from colorado.base.with_coordinates import WithCoordinates, WithCoordinatesEnum
from colorado.base.with_county import WithCounty, WithCountyEnum
from colorado.base.with_name import WithName, WithNameEnum
from colorado.base.with_nearest_airport import WithNearestAirport, WithNearestAirportEnum


class PopulatedPlace(WithName, WithAbbreviations, WithCoordinates, WithCounty, WithNearestAirport):
    """
    A place where people reside in the state of Colorado.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class PopulatedPlaceEnum(WithNameEnum, WithAbbreviationsEnum, WithCoordinatesEnum, WithCountyEnum,
                         WithNearestAirportEnum):
    """
    An enumeration of PopulatedPlace.
    """

    def __init__(self, location: PopulatedPlace):
        super().__init__(location=location)
