from typing import Any

from pydantic import model_validator

from colorado.base.location import LocationEnum, Location
from colorado.internal import BaseModel, validate_attribute_lengths


class Abbreviations(BaseModel):
    """
    A set of abbreviations.
    """
    three_letter: str
    five_letter: str
    seven_letter: str
    fourteen_letter: str

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    @model_validator(mode="after")
    def validate_model(self):
        lengths = {
            'three_letter': 3,
            'five_letter': 5,
            'seven_letter': 7,
            'fourteen_letter': 14
        }
        validate_attribute_lengths(obj=self, lengths=lengths)

        return self


class WithAbbreviations(Location):
    """
    A location with a set of abbreviations.
    """
    abbreviations: Abbreviations
    """
    The abbreviations of the location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class WithAbbreviationsEnum(LocationEnum):
    """
    An enumeration for WithAbbreviations objects.
    """

    def __init__(self, location: WithAbbreviations):
        super().__init__(location)

    @property
    def abbreviations(self) -> Abbreviations:
        """
        The abbreviations of the location.
        :return: The abbreviations of the location.
        :rtype: Abbreviations
        """
        return self._location.abbreviations  # type: ignore
