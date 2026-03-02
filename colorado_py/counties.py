from typing import Any

from colorado_py import LicensePlateCodes
from colorado_py._base import Place, PlaceEnum, PlaceAbbreviations
from colorado_py.zones import Zones


class County(Place):
    """
    Represents a county in the state of Colorado.
    """

    zone: Zones
    """
    The zone classification of the county, from the Colorado Consortium for Prescription Drug Abuse Prevention.
    """

    api_code: str
    """
    The API code representing the county, from the Colorado Department of Natural Resources.
    """

    license_plate_codes: LicensePlateCodes
    """
    A set of 2-letter and 3-letter prefix ranges that were historically used on Colorado license plates to indicate the county of registration.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Counties(PlaceEnum):
    """
    An enumeration of all counties in the state of Colorado.
    """
    ADAMS = County(
        name="Adams",
        abbreviations=PlaceAbbreviations(
            three_letter="ADM",
            five_letter="ADAMS",
            seven_letter="ADAMS",
            fourteen_letter="ADAMS"
        ),
        zone=Zones.URBAN,
        api_code="001",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["TE-UF", "GA-GG"],
            three_letter_prefix_ranges=["SAA-TZZ"]
        )
    )
    ALAMOSA = County(
        name="Alamosa",
        abbreviations=PlaceAbbreviations(
            three_letter="ALM",
            five_letter="ALAMS",
            seven_letter="ALAMOSA",
            fourteen_letter="ALAMOSA"
        ),
        zone=Zones.RURAL,
        api_code="003",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XE-XG"],
            three_letter_prefix_ranges=["EAA-EBD"],
        )
    )
    ARAPAHOE = County(
        name="Arapahoe",
        abbreviations=PlaceAbbreviations(
            three_letter="APH",
            five_letter="ARAPH",
            seven_letter="ARAPAHO",
            fourteen_letter="ARAPAHOE"
        ),
        zone=Zones.URBAN,
        api_code="005",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["PH-RP", "FA-FG"],
            three_letter_prefix_ranges=["PAA-RZZ"]
        )
    )
    ARCHULETA = County(
        name="Archuleta",
        abbreviations=PlaceAbbreviations(
            three_letter="ARL",
            five_letter="ARCHL",
            seven_letter="ARCHULT",
            fourteen_letter="ARCHULETA"
        ),
        zone=Zones.FRONTIER,
        api_code="007",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YU"],
            three_letter_prefix_ranges=["FAA-FAL"]
        )
    )
    BACA = County(
        name="Baca",
        abbreviations=PlaceAbbreviations(
            three_letter="BAC",
            five_letter="BACA",
            seven_letter="BACA",
            fourteen_letter="BACA"
        ),
        zone=Zones.FRONTIER,
        api_code="009",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WG"],
            three_letter_prefix_ranges=["EBE-EBW"]
        )
    )
    BENT = County(
        name="Bent",
        abbreviations=PlaceAbbreviations(
            three_letter="BNT",
            five_letter="BENT",
            seven_letter="BENT",
            fourteen_letter="BENT"
        ),
        zone=Zones.FRONTIER,
        api_code="011",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XC"],
            three_letter_prefix_ranges=["EBX-ECL"]
        )
    )
    BOULDER = County(
        name="Boulder",
        abbreviations=PlaceAbbreviations(
            three_letter="BLD",
            five_letter="BOULD",
            seven_letter="BOULDER",
            fourteen_letter="BOULDER"
        ),
        zone=Zones.URBAN,
        api_code="013",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ML-NF", "FH-FP"],
            three_letter_prefix_ranges=["MAA-NZZ"]
        )
    )
    BROOMFIELD = County(
        name="Broomfield",
        abbreviations=PlaceAbbreviations(
            three_letter="BRM",
            five_letter="BROOM",
            seven_letter="BROOMFL",
            fourteen_letter="BROOMFIELD"
        ),
        zone=Zones.SUBURBAN,
        api_code="014",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=[],
            three_letter_prefix_ranges=[]
        )
    )
    CHAFFEE = County(
        name="Chaffee",
        abbreviations=PlaceAbbreviations(
            three_letter="CHF",
            five_letter="CHAFF",
            seven_letter="CHAFFEE",
            fourteen_letter="CHAFFEE"
        ),
        zone=Zones.RURAL,
        api_code="015",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XH-XK"],
            three_letter_prefix_ranges=["FAM-FCC"]
        )
    )
    CHEYENNE = County(
        name="Cheyenne",
        abbreviations=PlaceAbbreviations(
            three_letter="CHY",
            five_letter="CHYEN",
            seven_letter="CHYENNE",
            fourteen_letter="CHEYENNE"
        ),
        zone=Zones.FRONTIER,
        api_code="017",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YR"],
            three_letter_prefix_ranges=["ECM-ECT"]
        )
    )
    CLEAR_CREEK = County(
        name="Clear Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CLC",
            five_letter="CLEAR",
            seven_letter="CLEARCK",
            fourteen_letter="CLEARCREEK"
        ),
        zone=Zones.RURAL,
        api_code="019",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YY-YZ"],
            three_letter_prefix_ranges=["ECU-EDU"]
        )
    )
    CONEJOS = County(
        name="Conejos",
        abbreviations=PlaceAbbreviations(
            three_letter="CNJ",
            five_letter="CONJO",
            seven_letter="CONEJOS",
            fourteen_letter="CONEJOS"
        ),
        zone=Zones.FRONTIER,
        api_code="021",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WS"],
            three_letter_prefix_ranges=["EDV-EEK"]
        )
    )
    COSTILLA = County(
        name="Costilla",
        abbreviations=PlaceAbbreviations(
            three_letter="CTL",
            five_letter="CSTIL",
            seven_letter="COSTILL",
            fourteen_letter="COSTILLA"
        ),
        zone=Zones.FRONTIER,
        api_code="023",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YA"],
            three_letter_prefix_ranges=["EEL-EES"]
        )
    )
    CROWLEY = County(
        name="Crowley",
        abbreviations=PlaceAbbreviations(
            three_letter="CWL",
            five_letter="CROWL",
            seven_letter="CROWLEY",
            fourteen_letter="CROWLEY"
        ),
        zone=Zones.FRONTIER,
        api_code="025",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XW-XX"],
            three_letter_prefix_ranges=["EET-EFA"]
        )
    )
    CUSTER = County(
        name="Custer",
        abbreviations=PlaceAbbreviations(
            three_letter="CST",
            five_letter="CUSTR",
            seven_letter="CUSTER",
            fourteen_letter="CUSTER"
        ),
        zone=Zones.FRONTIER,
        api_code="027",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZA"],
            three_letter_prefix_ranges=["EFB-EFG"]
        )
    )
    DELTA = County(
        name="Delta",
        abbreviations=PlaceAbbreviations(
            three_letter="DLT",
            five_letter="DELTA",
            seven_letter="DELTA",
            fourteen_letter="DELTA"
        ),
        zone=Zones.RURAL,
        api_code="029",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["VL-VN"],
            three_letter_prefix_ranges=[]
        )
    )
    DENVER = County(
        name="Denver",
        abbreviations=PlaceAbbreviations(
            three_letter="DEN",
            five_letter="DENVR",
            seven_letter="DENVER",
            fourteen_letter="DENVER"
        ),
        zone=Zones.URBAN,
        api_code="031",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["AA-CV"],
            three_letter_prefix_ranges=["AAA-DZZ"]
        )
    )
    DOLORES = County(
        name="Dolores",
        abbreviations=PlaceAbbreviations(
            three_letter="DLR",
            five_letter="DOLOR",
            seven_letter="DOLORES",
            fourteen_letter="DOLORES"
        ),
        zone=Zones.FRONTIER,
        api_code="033",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZH"],
            three_letter_prefix_ranges=["EHR-EHV"]
        )
    )
    DOUGLAS = County(
        name="Douglass",
        abbreviations=PlaceAbbreviations(
            three_letter="DGL",
            five_letter="DOUGL",
            seven_letter="DOUGLAS",
            fourteen_letter="DOUGLAS"
        ),
        zone=Zones.SUBURBAN,
        api_code="035",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YS-YT"],
            three_letter_prefix_ranges=["EHW-EMA"]
        )
    )
    EAGLE = County(
        name="Eagle",
        abbreviations=PlaceAbbreviations(
            three_letter="EAG",
            five_letter="EAGLE",
            seven_letter="EAGLE",
            fourteen_letter="EAGLE"
        ),
        zone=Zones.RURAL,
        api_code="037",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YM-YN"],
            three_letter_prefix_ranges=["EMB-EPA"]
        )
    )
    ELBERT = County(
        name="Elbert",
        abbreviations=PlaceAbbreviations(
            three_letter="ELB",
            five_letter="ELBRT",
            seven_letter="ELBERT",
            fourteen_letter="ELBERT"
        ),
        zone=Zones.FRONTIER,
        api_code="039",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XS-XT"],
            three_letter_prefix_ranges=["EPB-EPU"]
        )
    )
    EL_PASO = County(
        name="El Paso",
        abbreviations=PlaceAbbreviations(
            three_letter="ELP",
            five_letter="ELPAS",
            seven_letter="ELPASO",
            fourteen_letter="ELPASO"
        ),
        zone=Zones.URBAN,
        api_code="041",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["JX-LL", "FR-FT", "FV"],
            three_letter_prefix_ranges=["KAA-LZZ"]
        )
    )
    FREMONT = County(
        name="Fremont",
        abbreviations=PlaceAbbreviations(
            three_letter="FMT",
            five_letter="FREMT",
            seven_letter="FREMONT",
            fourteen_letter="FREMONT"
        ),
        zone=Zones.RURAL,
        api_code="043",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["UP-UT"],
            three_letter_prefix_ranges=["EPV-ETV"]
        )
    )
    GARFIELD = County(
        name="Garfield",
        abbreviations=PlaceAbbreviations(
            three_letter="GFL",
            five_letter="GARFL",
            seven_letter="GARFLD",
            fourteen_letter="GARFIELD"
        ),
        zone=Zones.RURAL,
        api_code="045",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WM-WR"],
            three_letter_prefix_ranges=["ETM-ETW"]
        )
    )
    GILPIN = County(
        name="Gilpin",
        abbreviations=PlaceAbbreviations(
            three_letter="GLP",
            five_letter="GILPN",
            seven_letter="GILPIN",
            fourteen_letter="GILPIN"
        ),
        zone=Zones.RURAL,
        api_code="047",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZK"],
            three_letter_prefix_ranges=["EWN-EWV"]
        )
    )
    GRAND = County(
        name="Grand",
        abbreviations=PlaceAbbreviations(
            three_letter="GRD",
            five_letter="GRAND",
            seven_letter="GRAND",
            fourteen_letter="GRAND"
        ),
        zone=Zones.FRONTIER,
        api_code="049",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZB-ZC"],
            three_letter_prefix_ranges=["EWZ-EYB"]
        )
    )
    GUNNISON = County(
        name="Gunnison",
        abbreviations=PlaceAbbreviations(
            three_letter="GUN",
            five_letter="GUNN",
            seven_letter="GUNNISN",
            fourteen_letter="GUNNISON"
        ),
        zone=Zones.RURAL,
        api_code="051",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YD-YE"],
            three_letter_prefix_ranges=["EYC-EZC"]
        )
    )
    HINSDALE = County(
        name="Hinsdale",
        abbreviations=PlaceAbbreviations(
            three_letter="HIN",
            five_letter="HINSD",
            seven_letter="HINSDAL",
            fourteen_letter="HINSDALE"
        ),
        zone=Zones.FRONTIER,
        api_code="053",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZN"],
            three_letter_prefix_ranges=["EZD-EZE"]
        )
    )
    HUERFANO = County(
        name="Huerfano",
        abbreviations=PlaceAbbreviations(
            three_letter="HRF",
            five_letter="HUERF",
            seven_letter="HUERFAN",
            fourteen_letter="HUERFANO"
        ),
        zone=Zones.FRONTIER,
        api_code="055",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["VE"],
            three_letter_prefix_ranges=["EZF-EZW"]
        )
    )
    JACKSON = County(
        name="Jackson",
        abbreviations=PlaceAbbreviations(
            three_letter="JKS",
            five_letter="JACKS",
            seven_letter="JACKSON",
            fourteen_letter="JACKSON"
        ),
        zone=Zones.FRONTIER,
        api_code="057",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZJ"],
            three_letter_prefix_ranges=["FGC-FGH"]
        )
    )
    JEFFERSON = County(
        name="Jefferson",
        abbreviations=PlaceAbbreviations(
            three_letter="JFR",
            five_letter="JEFFR",
            seven_letter="JEFFERS",
            fourteen_letter="JEFFERSON"
        ),
        zone=Zones.URBAN,
        api_code="059",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["RS-TD", "HG-HW"],
            three_letter_prefix_ranges=["GAA-JZZ"]
        )
    )
    KIOWA = County(
        name="Kiowa",
        abbreviations=PlaceAbbreviations(
            three_letter="KWA",
            five_letter="KIOWA",
            seven_letter="KIOWA",
            fourteen_letter="KIOWA"
        ),
        zone=Zones.FRONTIER,
        api_code="061",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YP"],
            three_letter_prefix_ranges=["WUS-WUY"]
        )
    )
    KIT_CARSON = County(
        name="Kit Carson",
        abbreviations=PlaceAbbreviations(
            three_letter="KCR",
            five_letter="KITCR",
            seven_letter="KITCRSN",
            fourteen_letter="KITCARSON"
        ),
        zone=Zones.FRONTIER,
        api_code="063",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WU-WV"],
            three_letter_prefix_ranges=["WUZ-WVV"]
        )
    )
    LAKE = County(
        name="Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKE",
            seven_letter="LAKE",
            fourteen_letter="LAKE"
        ),
        zone=Zones.RURAL,
        api_code="065",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YF-YH"],
            three_letter_prefix_ranges=["FCD-FDE"]
        )
    )
    LA_PLATA = County(
        name="La Plata",
        abbreviations=PlaceAbbreviations(
            three_letter="LPT",
            five_letter="LPLAT",
            seven_letter="LAPLATA",
            fourteen_letter="LAPLATA"
        ),
        zone=Zones.RURAL,
        api_code="067",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["VV-VY"],
            three_letter_prefix_ranges=["FDF-FGB"]
        )
    )
    LARIMER = County(
        name="Larimer",
        abbreviations=PlaceAbbreviations(
            three_letter="LAR",
            five_letter="LARIM",
            seven_letter="LARIMER",
            fourteen_letter="LARIMER"
        ),
        zone=Zones.RURAL,
        api_code="069",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["LU-MK", "FX-FY"],
            three_letter_prefix_ranges=["FHA-FZZ"]
        )
    )
    LAS_ANIMAS = County(
        name="Las Animas",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LSANM",
            seven_letter="LSANMAS",
            fourteen_letter="LASANIMAS"
        ),
        zone=Zones.FRONTIER,
        api_code="071",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["LM-LN"],
            three_letter_prefix_ranges=["UAA-UBK"]
        )
    )
    LINCOLN = County(
        name="Lincoln",
        abbreviations=PlaceAbbreviations(
            three_letter="LIN",
            five_letter="LINCL",
            seven_letter="LINCOLN",
            fourteen_letter="LINCOLN"
        ),
        zone=Zones.FRONTIER,
        api_code="073",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XP-XR"],
            three_letter_prefix_ranges=["UBL-UCA"]
        )
    )
    LOGAN = County(
        name="Logan",
        abbreviations=PlaceAbbreviations(
            three_letter="LOG",
            five_letter="LOGAN",
            seven_letter="LOGAN",
            fourteen_letter="LOGAN"
        ),
        zone=Zones.FRONTIER,
        api_code="075",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["UG-UJ"],
            three_letter_prefix_ranges=["UCB-UEH"]
        )
    )
    MESA = County(
        name="Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESA",
            seven_letter="MESA",
            fourteen_letter="MESA"
        ),
        zone=Zones.RURAL,
        api_code="077",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["NG-NT"],
            three_letter_prefix_ranges=["UEJ-UNL"]
        )
    )
    MINERAL = County(
        name="Mineral",
        abbreviations=PlaceAbbreviations(
            three_letter="MIN",
            five_letter="MINRL",
            seven_letter="MINERAL",
            fourteen_letter="MINERAL"
        ),
        zone=Zones.FRONTIER,
        api_code="079",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZM"],
            three_letter_prefix_ranges=["UNM-UNR"]
        )
    )
    MOFFAT = County(
        name="Moffat",
        abbreviations=PlaceAbbreviations(
            three_letter="MFT",
            five_letter="MOFFT",
            seven_letter="MOFFAT",
            fourteen_letter="MOFFAT"
        ),
        zone=Zones.RURAL,
        api_code="081",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YJ-YK"],
            three_letter_prefix_ranges=["UNS-UPX"]
        )
    )
    MONTEZUMA = County(
        name="Montezuma",
        abbreviations=PlaceAbbreviations(
            three_letter="MTZ",
            five_letter="MNTZM",
            seven_letter="MNTZUMA",
            fourteen_letter="MONTEZUMA"
        ),
        zone=Zones.RURAL,
        api_code="083",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XL-XN"],
            three_letter_prefix_ranges=["UPY-USL"]
        )
    )
    MONTROSE = County(
        name="Montrose",
        abbreviations=PlaceAbbreviations(
            three_letter="MTR",
            five_letter="MNTRO",
            seven_letter="MONTRSE",
            fourteen_letter="MONTROSE"
        ),
        zone=Zones.RURAL,
        api_code="085",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WB-WD"],
            three_letter_prefix_ranges=["USM-UUZ"]
        )
    )
    MORGAN = County(
        name="Morgan",
        abbreviations=PlaceAbbreviations(
            three_letter="MGN",
            five_letter="MORGN",
            seven_letter="MORGAN",
            fourteen_letter="MORGAN"
        ),
        zone=Zones.RURAL,
        api_code="087",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["UW-UY"],
            three_letter_prefix_ranges=["UVA-UXR"]
        )
    )
    OTERO = County(
        name="Otero",
        abbreviations=PlaceAbbreviations(
            three_letter="OTR",
            five_letter="OTERO",
            seven_letter="OTERO",
            fourteen_letter="OTERO"
        ),
        zone=Zones.FRONTIER,
        api_code="089",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["PA-PC"],
            three_letter_prefix_ranges=["UXS-UZZ"]
        )
    )
    OURAY = County(
        name="Ouray",
        abbreviations=PlaceAbbreviations(
            three_letter="OUR",
            five_letter="OURAY",
            seven_letter="OURAY",
            fourteen_letter="OURAY"
        ),
        zone=Zones.FRONTIER,
        api_code="091",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZF"],
            three_letter_prefix_ranges=["VAA-VAG"]
        )
    )
    PARK = County(
        name="Park",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK",
            seven_letter="PARK",
            fourteen_letter="PARK"
        ),
        zone=Zones.FRONTIER,
        api_code="093",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZD"],
            three_letter_prefix_ranges=["VAH-VBA"]
        )
    )
    PHILLIPS = County(
        name="Phillips",
        abbreviations=PlaceAbbreviations(
            three_letter="PHI",
            five_letter="PHILL",
            seven_letter="PHILLPS",
            fourteen_letter="PHILLIPS"
        ),
        zone=Zones.FRONTIER,
        api_code="095",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XY-XZ"],
            three_letter_prefix_ranges=["VBB-VBR"]
        )
    )
    PITKIN = County(
        name="Pitkin",
        abbreviations=PlaceAbbreviations(
            three_letter="PIT",
            five_letter="PITKN",
            seven_letter="PITKIN",
            fourteen_letter="PITKIN"
        ),
        zone=Zones.RURAL,
        api_code="097",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZG-ZP"],
            three_letter_prefix_ranges=["VBS-VDM"]
        )
    )
    PROWERS = County(
        name="Prowers",
        abbreviations=PlaceAbbreviations(
            three_letter="PRW",
            five_letter="PROWR",
            seven_letter="PROWERS",
            fourteen_letter="PROWERS"
        ),
        zone=Zones.FRONTIER,
        api_code="099",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["VG-VH"],
            three_letter_prefix_ranges=["VDN-VEY"]
        )
    )
    PUEBLO = County(
        name="Pueblo",
        abbreviations=PlaceAbbreviations(
            three_letter="PUB",
            five_letter="PUEBL",
            seven_letter="PUEBLO",
            fourteen_letter="PUEBLO"
        ),
        zone=Zones.RURAL,
        api_code="101",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["GP-HD"],
            three_letter_prefix_ranges=["VEC-VVC"]
        )
    )
    RIO_BLANCO = County(
        name="Rio Blanco",
        abbreviations=PlaceAbbreviations(
            three_letter="RBL",
            five_letter="RBLNC",
            seven_letter="RBLANCO",
            fourteen_letter="RIOBLANCO"
        ),
        zone=Zones.FRONTIER,
        api_code="103",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YV-YW"],
            three_letter_prefix_ranges=["VVD-VVV"]
        )
    )
    RIO_GRANDE = County(
        name="Rio Grande",
        abbreviations=PlaceAbbreviations(
            three_letter="RGR",
            five_letter="RGRAN",
            seven_letter="RGRANDE",
            fourteen_letter="RIOGRANDE"
        ),
        zone=Zones.FRONTIER,
        api_code="105",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WJ-WL"],
            three_letter_prefix_ranges=["VVW-VWZ"]
        )
    )
    ROUTT = County(
        name="Routt",
        abbreviations=PlaceAbbreviations(
            three_letter="RTT",
            five_letter="ROUTT",
            seven_letter="ROUTT",
            fourteen_letter="ROUTT"
        ),
        zone=Zones.RURAL,
        api_code="107",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WZ-XA"],
            three_letter_prefix_ranges=["VXA-VYN"]
        )
    )
    SAGAUCHE = County(
        name="Saguache",
        abbreviations=PlaceAbbreviations(
            three_letter="SAG",
            five_letter="SAGCH",
            seven_letter="SAGCHE",
            fourteen_letter="SAGAUCHE"
        ),
        zone=Zones.FRONTIER,
        api_code="109",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["XU-XV"],
            three_letter_prefix_ranges=["VYP-VZA"]
        )
    )
    SAN_JUAN = County(
        name="San Juan",
        abbreviations=PlaceAbbreviations(
            three_letter="SJN",
            five_letter="SANJN",
            seven_letter="SANJUAN",
            fourteen_letter="SANJUAN"
        ),
        zone=Zones.FRONTIER,
        api_code="111",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZE"],
            three_letter_prefix_ranges=["VZB-VZE"]
        )
    )
    SAN_MIGUEL = County(
        name="San Miguel",
        abbreviations=PlaceAbbreviations(
            three_letter="SMG",
            five_letter="SANMG",
            seven_letter="SANMIGU",
            fourteen_letter="SANMIGUEL"
        ),
        zone=Zones.RURAL,
        api_code="113",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YX"],
            three_letter_prefix_ranges=["VZF-VZR"]
        )
    )
    SEDGWICK = County(
        name="Sedgwick",
        abbreviations=PlaceAbbreviations(
            three_letter="SDW",
            five_letter="SEDGW",
            seven_letter="SEDGWIC",
            fourteen_letter="SEDGWICK"
        ),
        zone=Zones.FRONTIER,
        api_code="115",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YB-YC"],
            three_letter_prefix_ranges=["WNL-WNY"]
        )
    )
    SUMMIT = County(
        name="Summit",
        abbreviations=PlaceAbbreviations(
            three_letter="SUM",
            five_letter="SUMIT",
            seven_letter="SUMMIT",
            fourteen_letter="SUMMIT"
        ),
        zone=Zones.RURAL,
        api_code="117",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["ZL", "ZR"],
            three_letter_prefix_ranges=["WNZ-WRM"]
        )
    )
    TELLER = County(
        name="Teller",
        abbreviations=PlaceAbbreviations(
            three_letter="TLR",
            five_letter="TELLR",
            seven_letter="TELLER",
            fourteen_letter="TELLER"
        ),
        zone=Zones.RURAL,
        api_code="119",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["YL"],
            three_letter_prefix_ranges=["WRN-WSR"]
        )
    )
    WASHINGTON = County(
        name="Washington",
        abbreviations=PlaceAbbreviations(
            three_letter="WSH",
            five_letter="WSHNG",
            seven_letter="WSHNGT",
            fourteen_letter="WASHINGTON"
        ),
        zone=Zones.FRONTIER,
        api_code="121",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["WW"],
            three_letter_prefix_ranges=["WST-WTK"]
        )
    )
    WELD = County(
        name="Weld",
        abbreviations=PlaceAbbreviations(
            three_letter="WLD",
            five_letter="WELD",
            seven_letter="WELD",
            fourteen_letter="WELD"
        ),
        zone=Zones.RURAL,
        api_code="123",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["HY-JM"],
            three_letter_prefix_ranges=["WAA-WNK"]
        )
    )
    YUMA = County(
        name="Yuma",
        abbreviations=PlaceAbbreviations(
            three_letter="YUM",
            five_letter="YUMA",
            seven_letter="YUMA",
            fourteen_letter="YUMA"
        ),
        zone=Zones.FRONTIER,
        api_code="125",
        license_plate_codes=LicensePlateCodes(
            two_letter_prefix_ranges=["VS-VT"],
            three_letter_prefix_ranges=["WTL-WUR"]
        )
    )
