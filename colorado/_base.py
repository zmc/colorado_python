import enum
from typing import Any

from pydantic import model_validator

from colorado.internal import BaseModel, validate_attribute_lengths


class PlaceAbbreviations(BaseModel):
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


class Place(BaseModel):
    name: str
    abbreviations: PlaceAbbreviations

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class PlaceEnum(enum.Enum):
    def __init__(self, place: Place):
        self._place = place

    @property
    def name(self) -> str:
        return self._place.name

    @property
    def abbreviations(self) -> PlaceAbbreviations:
        return self._place.abbreviations
