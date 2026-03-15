from typing import Any

from colorado.base.with_abbreviations import WithAbbreviations, WithAbbreviationsEnum, Abbreviations
from colorado.base.with_name import WithName, WithNameEnum


class Airport(WithName, WithAbbreviations):
    """
    Represents a major or regional airport in the state of Colorado.
    """

    iata_code: str
    """
    The IATA code used to identify this airport nationally.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Airports(WithNameEnum, WithAbbreviationsEnum):
    """
    An enumeration of all major and regional airports in the state of Colorado.
    """
    ASPEN_PITKIN = Airport(
        name="Aspen-Pitkin County/Sardy Field",
        iata_code="ASE",
        abbreviations=Abbreviations(
            three_letter="ASE",
            five_letter="ASE",
            seven_letter="ASE",
            fourteen_letter="ASE"
        ),
        latitude=39.221878,
        longitude=-106.868233,
    )
    COLORADO_SPRINGS = Airport(
        name="City Of Colorado Springs Municipal Airport",
        iata_code="COS",
        abbreviations=Abbreviations(
            three_letter="COS",
            five_letter="COS",
            seven_letter="COS",
            fourteen_letter="COS"
        ),
        latitude=38.805817,
        longitude=-104.700776,
    )
    CORTEZ = Airport(
        name="Cortez Municipal Airport",
        iata_code="CEZ",
        abbreviations=Abbreviations(
            three_letter="CEZ",
            five_letter="CEZ",
            seven_letter="CEZ",
            fourteen_letter="CEZ"
        ),
        latitude=37.303002,
        longitude=-108.628044,
    )
    DENVER = Airport(
        name="Denver International Airport",
        iata_code="DEN",
        abbreviations=Abbreviations(
            three_letter="DEN",
            five_letter="DEN",
            seven_letter="DEN",
            fourteen_letter="DEN"
        ),
        latitude=39.861667,
        longitude=-104.673167,
    )
    DURANGO_LA_PLATA = Airport(
        name="Durango-La Plata County Airport",
        iata_code="DRO",
        abbreviations=Abbreviations(
            three_letter="DRO",
            five_letter="DRO",
            seven_letter="DRO",
            fourteen_letter="DRO"
        ),
        latitude=37.151528,
        longitude=-107.753778,
    )
    EAGLE = Airport(
        name="Eagle County Regional Airport",
        iata_code="EGE",
        abbreviations=Abbreviations(
            three_letter="EGE",
            five_letter="EGE",
            seven_letter="EGE",
            fourteen_letter="EGE"
        ),
        latitude=39.64275,
        longitude=-106.915944,
    )
    GRAND_JUNCTION = Airport(
        name="Grand Junction Regional Airport",
        iata_code="GJT",
        abbreviations=Abbreviations(
            three_letter="GJT",
            five_letter="GJT",
            seven_letter="GJT",
            fourteen_letter="GJT"
        ),
        latitude=39.121499,
        longitude=-108.525486,
    )
    GUNNISON_CRESTED_BUTTE = Airport(
        name="Gunnison-Crested Butte Regional Airport",
        iata_code="GUC",
        abbreviations=Abbreviations(
            three_letter="GUC",
            five_letter="GUC",
            seven_letter="GUC",
            fourteen_letter="GUC"
        ),
        latitude=38.534333,
        longitude=-106.93175,
    )
    MONTROSE = Airport(
        name="Montrose Regional Airport",
        iata_code="MTJ",
        abbreviations=Abbreviations(
            three_letter="MTJ",
            five_letter="MTJ",
            seven_letter="MTJ",
            fourteen_letter="MTJ"
        ),
        latitude=38.509806,
        longitude=-107.89425,
    )
    NORTHERN_COLORADO = Airport(
        name="Northern Colorado Regional Airport",
        iata_code="FNL",
        abbreviations=Abbreviations(
            three_letter="FNL",
            five_letter="FNL",
            seven_letter="FNL",
            fourteen_letter="FNL"
        ),
        latitude=40.451816,
        longitude=-105.011326,
    )
    PUEBLO = Airport(
        name="Pueblo Memorial Airport",
        iata_code="PUB",
        abbreviations=Abbreviations(
            three_letter="PUB",
            five_letter="PUB",
            seven_letter="PUB",
            fourteen_letter="PUB"
        ),
        latitude=38.289947,
        longitude=-104.498028,
    )
    SAN_LUIS_VALLEY = Airport(
        name="San Luis Valley Regional/Bergman Field",
        iata_code="ALS",
        abbreviations=Abbreviations(
            three_letter="ALS",
            five_letter="ALS",
            seven_letter="ALS",
            fourteen_letter="ALS"
        ),
        latitude=37.435125,
        longitude=-105.867875,
    )
    SOUTHEAST_COLORADO = Airport(
        name="Southeast Colorado Regional Airport",
        iata_code="LAA",
        abbreviations=Abbreviations(
            three_letter="LAA",
            five_letter="LAA",
            seven_letter="LAA",
            fourteen_letter="LAA"
        ),
        latitude=38.069704,
        longitude=-102.688494,
    )
    STERLING = Airport(
        name="Sterling Municipal Airport",
        iata_code="STK",
        abbreviations=Abbreviations(
            three_letter="STK",
            five_letter="STK",
            seven_letter="STK",
            fourteen_letter="STK"
        ),
        latitude=40.614298,
        longitude=-103.264261,
    )
    TELLURIDE = Airport(
        name="Telluride Regional Airport",
        iata_code="TEX",
        abbreviations=Abbreviations(
            three_letter="TEX",
            five_letter="TEX",
            seven_letter="TEX",
            fourteen_letter="TEX"
        ),
        latitude=37.953806,
        longitude=-107.90875,
    )
    YAMPA_VALLEY = Airport(
        name="Yampa Valley Airport",
        iata_code="HDN",
        abbreviations=Abbreviations(
            three_letter="HDN",
            five_letter="HDN",
            seven_letter="HDN",
            fourteen_letter="HDN"
        ),
        latitude=40.481194,
        longitude=-107.217667,
    )

    @property
    def iata_code(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.iata_code  # type: ignore
