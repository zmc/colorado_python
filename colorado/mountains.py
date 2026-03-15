from typing import Any

from colorado.base.with_abbreviations import WithAbbreviations, WithAbbreviationsEnum, Abbreviations
from colorado.base.with_coordinates import WithCoordinates, WithCoordinatesEnum
from colorado.base.with_name import WithName, WithNameEnum
from colorado.base.with_nearest_airport import WithNearestAirport, WithNearestAirportEnum, Airports


class Mountain(WithName, WithAbbreviations, WithCoordinates, WithNearestAirport):
    """
    Represents a mountain in the state of Colorado.
    """

    height: float
    """
    The height, in feet, of the mountain.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Mountains(WithNameEnum, WithAbbreviationsEnum, WithCoordinatesEnum, WithNearestAirportEnum):
    """
    An enumeration of mountains in the state of Colorado.
    """
    ANTHRACITE_RANGE_HIGH_POINT = Mountain(
        name="Anthracite Range High Point",
        abbreviations=Abbreviations(
            three_letter="ARH",
            five_letter="ARHP",
            seven_letter="ARNG-HP",
            fourteen_letter="ANTHR-RNG-HP"
        ),
        latitude=38.8145,
        longitude=-107.1445,
        height=12394.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    ANTORA_PEAK = Mountain(
        name="Antora Peak",
        abbreviations=Abbreviations(
            three_letter="ANT",
            five_letter="ANTPK",
            seven_letter="ANTR-PK",
            fourteen_letter="ANTORA-PK"
        ),
        latitude=38.325,
        longitude=-106.218,
        height=13275.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BALD_MOUNTAIN = Mountain(
        name="Bald Mountain",
        abbreviations=Abbreviations(
            three_letter="BLD",
            five_letter="BALD",
            seven_letter="BALD-MT",
            fourteen_letter="BALD-MTN"
        ),
        latitude=39.4448,
        longitude=-105.9705,
        height=13690.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    BARD_PEAK = Mountain(
        name="Bard Peak",
        abbreviations=Abbreviations(
            three_letter="BRD",
            five_letter="BARD",
            seven_letter="BARD-PK",
            fourteen_letter="BARD-PEAK"
        ),
        latitude=39.7204,
        longitude=-105.8044,
        height=13647.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BENNETT_PEAK = Mountain(
        name="Bennett Peak",
        abbreviations=Abbreviations(
            three_letter="BNT",
            five_letter="BNTPK",
            seven_letter="BNNT-PK",
            fourteen_letter="BENNETT-PK"
        ),
        latitude=37.4833,
        longitude=-106.4343,
        height=13209.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BILL_WILLIAMS_PEAK = Mountain(
        name="Bill Williams Peak",
        abbreviations=Abbreviations(
            three_letter="BWP",
            five_letter="BWMS",
            seven_letter="BWMS-PK",
            fourteen_letter="BILLWMS-PK"
        ),
        latitude=39.1806,
        longitude=-106.6102,
        height=13389.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    BISON_MOUNTAIN = Mountain(
        name="Bison Mountain (Bison Peak)",
        abbreviations=Abbreviations(
            three_letter="BSN",
            five_letter="BISON",
            seven_letter="BSON-MT",
            fourteen_letter="BISON-MTN"
        ),
        latitude=39.2384,
        longitude=-105.4978,
        height=12432.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BLACK_MOUNTAIN_MOFFAT_COUNTY = Mountain(
        name="Black Mountain",
        abbreviations=Abbreviations(
            three_letter="BKM",
            five_letter="BKMOF",
            seven_letter="BLK-MOF",
            fourteen_letter="BLKMTN-MOF"
        ),
        latitude=40.7835,
        longitude=-107.3691,
        height=10865.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    BLACK_MOUNTAIN_PARK_COUNTY = Mountain(
        name="Black Mountain",
        abbreviations=Abbreviations(
            three_letter="BKP",
            five_letter="BKPRK",
            seven_letter="BLK-PRK",
            fourteen_letter="BLKMTN-PRK"
        ),
        latitude=38.7185,
        longitude=-105.6874,
        height=11659.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BLAIR_MOUNTAIN = Mountain(
        name="Blair Mountain",
        abbreviations=Abbreviations(
            three_letter="BLR",
            five_letter="BLAIR",
            seven_letter="BLAR-M",
            fourteen_letter="BLAIR-MTN"
        ),
        latitude=39.7943,
        longitude=-107.4176,
        height=11465.0,
        nearest_airport=Airports.EAGLE
    )
    BLANCA_PEAK = Mountain(
        name="Blanca Peak",
        abbreviations=Abbreviations(
            three_letter="BLC",
            five_letter="BLANC",
            seven_letter="BLNC-PK",
            fourteen_letter="BLANCA-PK"
        ),
        latitude=37.5775,
        longitude=-105.4856,
        height=14351.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BUSHNELL_PEAK = Mountain(
        name="Bushnell Peak",
        abbreviations=Abbreviations(
            three_letter="BSH",
            five_letter="BSHNL",
            seven_letter="BUSH-PK",
            fourteen_letter="BUSHNELL-PK"
        ),
        latitude=38.3412,
        longitude=-105.8892,
        height=13110.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CAPITOL_PEAK = Mountain(
        name="Capitol Peak",
        abbreviations=Abbreviations(
            three_letter="CAP",
            five_letter="CAPTL",
            seven_letter="CAPT-PK",
            fourteen_letter="CAPITOL-PK"
        ),
        latitude=39.1503,
        longitude=-107.0829,
        height=14137.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    CARBON_PEAK = Mountain(
        name="Carbon Peak",
        abbreviations=Abbreviations(
            three_letter="CBN",
            five_letter="CARBN",
            seven_letter="CARB-PK",
            fourteen_letter="CARBON-PK"
        ),
        latitude=38.7943,
        longitude=-107.0431,
        height=12088.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CASTLE_PEAK = Mountain(
        name="Castle Peak",
        abbreviations=Abbreviations(
            three_letter="CST",
            five_letter="CSTL",
            seven_letter="CSTL-PK",
            fourteen_letter="CASTLE-PK"
        ),
        latitude=39.0097,
        longitude=-106.8614,
        height=14279.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    CASTLE_PEAK_SAWATCH_RANGE = Mountain(
        name="Castle Peak",
        abbreviations=Abbreviations(
            three_letter="CPW",
            five_letter="CPSAW",
            seven_letter="CSTL-SW",
            fourteen_letter="CASTLE-SAW"
        ),
        latitude=39.7723,
        longitude=-106.8304,
        height=11305.0,
        nearest_airport=Airports.EAGLE
    )
    CHAIR_MOUNTAIN = Mountain(
        name="Chair Mountain",
        abbreviations=Abbreviations(
            three_letter="CHR",
            five_letter="CHAIR",
            seven_letter="CHAR-MT",
            fourteen_letter="CHAIR-MTN"
        ),
        latitude=39.0581,
        longitude=-107.2822,
        height=12727.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    CHALK_BENCHMARK = Mountain(
        name="Chalk Benchmark",
        abbreviations=Abbreviations(
            three_letter="CHK",
            five_letter="CHALK",
            seven_letter="CHLK-BM",
            fourteen_letter="CHALK-BNCHMK"
        ),
        latitude=37.1418,
        longitude=-106.75,
        height=12038.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CLARK_PEAK = Mountain(
        name="Clark Peak",
        abbreviations=Abbreviations(
            three_letter="CLK",
            five_letter="CLARK",
            seven_letter="CLRK-PK",
            fourteen_letter="CLARK-PK"
        ),
        latitude=40.6068,
        longitude=-105.93,
        height=12954.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    COAL_MOUNTAIN = Mountain(
        name="Coal Mountain",
        abbreviations=Abbreviations(
            three_letter="COL",
            five_letter="COAL",
            seven_letter="COAL-MT",
            fourteen_letter="COAL-MTN"
        ),
        latitude=38.787,
        longitude=-107.4837,
        height=11710.0,
        nearest_airport=Airports.MONTROSE
    )
    COCHETOPA_DOME = Mountain(
        name="Cochetopa Dome",
        abbreviations=Abbreviations(
            three_letter="CCH",
            five_letter="CCHTP",
            seven_letter="CHTP-DM",
            fourteen_letter="COCHETOPA-DM"
        ),
        latitude=38.2267,
        longitude=-106.7147,
        height=11138.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    COLUMBUS_MOUNTAIN = Mountain(
        name="Columbus Mountain",
        abbreviations=Abbreviations(
            three_letter="CLB",
            five_letter="CLMBS",
            seven_letter="CLMB-MT",
            fourteen_letter="COLUMBUS-MT"
        ),
        latitude=40.8799,
        longitude=-107.1921,
        height=10258.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CONEJOS_PEAK = Mountain(
        name="Conejos Peak",
        abbreviations=Abbreviations(
            three_letter="CNJ",
            five_letter="CONJS",
            seven_letter="CNJS-PK",
            fourteen_letter="CONEJOS-PK"
        ),
        latitude=37.2887,
        longitude=-106.5709,
        height=13179.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CORNWALL_MOUNTAIN = Mountain(
        name="Cornwall Mountain",
        abbreviations=Abbreviations(
            three_letter="CNW",
            five_letter="CRNWL",
            seven_letter="CWAL-MT",
            fourteen_letter="CORNWALL-MT"
        ),
        latitude=37.3811,
        longitude=-106.492,
        height=12291.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CRATER_PEAK = Mountain(
        name="Crater Peak",
        abbreviations=Abbreviations(
            three_letter="CRT",
            five_letter="CRATR",
            seven_letter="CRTR-PK",
            fourteen_letter="CRATER-PK"
        ),
        latitude=39.0396,
        longitude=-107.6628,
        height=11333.0,
        nearest_airport=Airports.MONTROSE
    )
    CRESTED_BUTTE = Mountain(
        name="Crested Butte",
        abbreviations=Abbreviations(
            three_letter="CRB",
            five_letter="CSTBT",
            seven_letter="CRST-BT",
            fourteen_letter="CRESTED-BTT"
        ),
        latitude=38.8835,
        longitude=-106.9436,
        height=12168.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    CRESTONE_PEAK = Mountain(
        name="Crestone Peak",
        abbreviations=Abbreviations(
            three_letter="CRS",
            five_letter="CRSTN",
            seven_letter="CRST-PK",
            fourteen_letter="CRESTONE-PK"
        ),
        latitude=37.9669,
        longitude=-105.5855,
        height=14300.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CULEBRA_PEAK = Mountain(
        name="Culebra Peak",
        abbreviations=Abbreviations(
            three_letter="CUL",
            five_letter="CULBR",
            seven_letter="CULB-PK",
            fourteen_letter="CULEBRA-PK"
        ),
        latitude=37.1224,
        longitude=-105.1858,
        height=14053.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    EAST_BECKWITH_MOUNTAIN = Mountain(
        name="East Beckwith Mountain",
        abbreviations=Abbreviations(
            three_letter="EBK",
            five_letter="EBECK",
            seven_letter="EBK-MTN",
            fourteen_letter="E-BECKWITH"
        ),
        latitude=38.8464,
        longitude=-107.2233,
        height=12441.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    EAST_SPANISH_PEAK = Mountain(
        name="East Spanish Peak",
        abbreviations=Abbreviations(
            three_letter="ESP",
            five_letter="ESPAN",
            seven_letter="ESP-PK",
            fourteen_letter="E-SPANISH-PK"
        ),
        latitude=37.3934,
        longitude=-104.9201,
        height=12688.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ELK_MOUNTAIN = Mountain(
        name="Elk Mountain",
        abbreviations=Abbreviations(
            three_letter="ELK",
            five_letter="ELKMT",
            seven_letter="ELK-MTN",
            fourteen_letter="ELK-MTN"
        ),
        latitude=40.1619,
        longitude=-106.1285,
        height=11424.0,
        nearest_airport=Airports.EAGLE
    )
    ELLIOTT_MOUNTAIN = Mountain(
        name="Elliott Mountain",
        abbreviations=Abbreviations(
            three_letter="ELL",
            five_letter="ELLIT",
            seven_letter="ELLT-MT",
            fourteen_letter="ELLIOTT-MTN"
        ),
        latitude=37.7344,
        longitude=-108.058,
        height=12346.0,
        nearest_airport=Airports.TELLURIDE
    )
    FLAT_TOP_MOUNTAIN = Mountain(
        name="Flat Top Mountain",
        abbreviations=Abbreviations(
            three_letter="FLT",
            five_letter="FLTTP",
            seven_letter="FLATTOP",
            fourteen_letter="FLATTOP-MTN"
        ),
        latitude=40.0147,
        longitude=-107.0833,
        height=12361.0,
        nearest_airport=Airports.EAGLE
    )
    GOTHIC_MOUNTAIN = Mountain(
        name="Gothic Mountain",
        abbreviations=Abbreviations(
            three_letter="GTH",
            five_letter="GOTH",
            seven_letter="GOTH-MT",
            fourteen_letter="GOTHIC-MTN"
        ),
        latitude=38.9562,
        longitude=-107.0107,
        height=12631.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    GRAHAM_PEAK = Mountain(
        name="Graham Peak",
        abbreviations=Abbreviations(
            three_letter="GRH",
            five_letter="GRHAM",
            seven_letter="GRHM-PK",
            fourteen_letter="GRAHAM-PK"
        ),
        latitude=37.4972,
        longitude=-107.3761,
        height=12536.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    GRAYS_PEAK = Mountain(
        name="Grays Peak",
        abbreviations=Abbreviations(
            three_letter="GRY",
            five_letter="GRAYS",
            seven_letter="GRYS-PK",
            fourteen_letter="GRAYS-PK"
        ),
        latitude=39.6339,
        longitude=-105.8176,
        height=14278.0,
        nearest_airport=Airports.EAGLE
    )
    GREEN_MOUNTAIN = Mountain(
        name="Green Mountain",
        abbreviations=Abbreviations(
            three_letter="GRN",
            five_letter="GREEN",
            seven_letter="GREN-MT",
            fourteen_letter="GREEN-MTN"
        ),
        latitude=39.3053,
        longitude=-105.3001,
        height=10427.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREENHORN_MOUNTAIN = Mountain(
        name="Greenhorn Mountain",
        abbreviations=Abbreviations(
            three_letter="GHN",
            five_letter="GRNHN",
            seven_letter="GRNH-MT",
            fourteen_letter="GREENHORN-MT"
        ),
        latitude=37.8815,
        longitude=-105.0133,
        height=12352.0,
        nearest_airport=Airports.PUEBLO
    )
    GRIZZLY_PEAK = Mountain(
        name="Grizzly Peak",
        abbreviations=Abbreviations(
            three_letter="GRZ",
            five_letter="GRZLY",
            seven_letter="GRZL-PK",
            fourteen_letter="GRIZZLY-PK"
        ),
        latitude=39.0425,
        longitude=-106.5976,
        height=13995.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    HAGUES_PEAK = Mountain(
        name="Hagues Peak",
        abbreviations=Abbreviations(
            three_letter="HAG",
            five_letter="HAGUE",
            seven_letter="HAGS-PK",
            fourteen_letter="HAGUES-PK"
        ),
        latitude=40.4845,
        longitude=-105.6464,
        height=13573.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HANDIES_PEAK = Mountain(
        name="Handies Peak",
        abbreviations=Abbreviations(
            three_letter="HND",
            five_letter="HANDS",
            seven_letter="HNDS-PK",
            fourteen_letter="HANDIES-PK"
        ),
        latitude=37.913,
        longitude=-107.5044,
        height=14058.0,
        nearest_airport=Airports.TELLURIDE
    )
    HARDSCRABBLE_MOUNTAIN = Mountain(
        name="Hardscrabble Mountain",
        abbreviations=Abbreviations(
            three_letter="HDS",
            five_letter="HDSCB",
            seven_letter="HDSC-MT",
            fourteen_letter="HARDSCRAB-MT"
        ),
        latitude=39.5171,
        longitude=-106.8021,
        height=11171.0,
        nearest_airport=Airports.EAGLE
    )
    HENRY_MOUNTAIN = Mountain(
        name="Henry Mountain",
        abbreviations=Abbreviations(
            three_letter="HNR",
            five_letter="HENRY",
            seven_letter="HNRY-MT",
            fourteen_letter="HENRY-MTN"
        ),
        latitude=38.6856,
        longitude=-106.6211,
        height=13261.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    HESPERUS_MOUNTAIN = Mountain(
        name="Hesperus Mountain",
        abbreviations=Abbreviations(
            three_letter="HSP",
            five_letter="HSPRS",
            seven_letter="HSPR-MT",
            fourteen_letter="HESPERUS-MT"
        ),
        latitude=37.4451,
        longitude=-108.089,
        height=13237.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HORSE_MOUNTAIN = Mountain(
        name="Horse Mountain",
        abbreviations=Abbreviations(
            three_letter="HRS",
            five_letter="HORSE",
            seven_letter="HORS-MT",
            fourteen_letter="HORSE-MTN"
        ),
        latitude=37.308,
        longitude=-107.2864,
        height=9952.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HUNTSMAN_RIDGE_PEAK_DUTCH_PEAK = Mountain(
        name="Huntsman Ridge Peak (Dutch Peak)",
        abbreviations=Abbreviations(
            three_letter="HNT",
            five_letter="HNTRG",
            seven_letter="HTMR-PK",
            fourteen_letter="HUNTSMAN-PK"
        ),
        latitude=39.192,
        longitude=-107.3668,
        height=11858.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    IRON_MOUNTAIN = Mountain(
        name="Iron Mountain",
        abbreviations=Abbreviations(
            three_letter="IRN",
            five_letter="IRON",
            seven_letter="IRON-MT",
            fourteen_letter="IRON-MTN"
        ),
        latitude=37.6375,
        longitude=-105.2538,
        height=11416.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    JACQUE_PEAK = Mountain(
        name="Jacque Peak",
        abbreviations=Abbreviations(
            three_letter="JAC",
            five_letter="JACQ",
            seven_letter="JACQ-PK",
            fourteen_letter="JACQUE-PK"
        ),
        latitude=39.4549,
        longitude=-106.197,
        height=13211.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    KNOBBY_CREST = Mountain(
        name="Knobby Crest",
        abbreviations=Abbreviations(
            three_letter="KNB",
            five_letter="KNOBY",
            seven_letter="KNBY-CR",
            fourteen_letter="KNOBBY-CRST"
        ),
        latitude=39.3681,
        longitude=-105.605,
        height=12434.0,
        nearest_airport=Airports.DENVER
    )
    LA_PLATA_PEAK = Mountain(
        name="La Plata Peak",
        abbreviations=Abbreviations(
            three_letter="LPL",
            five_letter="LPLAT",
            seven_letter="LAPL-PK",
            fourteen_letter="LA-PLATA-PK"
        ),
        latitude=39.0294,
        longitude=-106.4729,
        height=14343.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    LARAMIE_MOUNTAINS_HP = Mountain(
        name="Laramie Mountains HP",
        abbreviations=Abbreviations(
            three_letter="LAR",
            five_letter="LARMI",
            seven_letter="LARM-HP",
            fourteen_letter="LARAMIE-HP"
        ),
        latitude=40.7704,
        longitude=-105.7162,
        height=11025.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LITTLE_CONE = Mountain(
        name="Little Cone",
        abbreviations=Abbreviations(
            three_letter="LTC",
            five_letter="LTCON",
            seven_letter="LTL-CNE",
            fourteen_letter="LITTLE-CONE"
        ),
        latitude=37.9275,
        longitude=-108.0908,
        height=11988.0,
        nearest_airport=Airports.TELLURIDE
    )
    LONE_CONE = Mountain(
        name="Lone Cone",
        abbreviations=Abbreviations(
            three_letter="LON",
            five_letter="LOCON",
            seven_letter="LNE-CNE",
            fourteen_letter="LONE-CONE"
        ),
        latitude=37.888,
        longitude=-108.2556,
        height=12618.0,
        nearest_airport=Airports.TELLURIDE
    )
    LONGS_PEAK = Mountain(
        name="Longs Peak",
        abbreviations=Abbreviations(
            three_letter="LNG",
            five_letter="LONGS",
            seven_letter="LNGS-PK",
            fourteen_letter="LONGS-PK"
        ),
        latitude=40.255,
        longitude=-105.6151,
        height=14259.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MARCELLINA_MOUNTAIN = Mountain(
        name="Marcellina Mountain",
        abbreviations=Abbreviations(
            three_letter="MRC",
            five_letter="MRCEL",
            seven_letter="MRCL-MT",
            fourteen_letter="MARCELLINA"
        ),
        latitude=38.9299,
        longitude=-107.2438,
        height=11353.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MAROON_PEAK = Mountain(
        name="Maroon Peak",
        abbreviations=Abbreviations(
            three_letter="MRN",
            five_letter="MROON",
            seven_letter="MRON-PK",
            fourteen_letter="MAROON-PK"
        ),
        latitude=39.0708,
        longitude=-106.989,
        height=14163.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MATCHLESS_MOUNTAIN = Mountain(
        name="Matchless Mountain",
        abbreviations=Abbreviations(
            three_letter="MCH",
            five_letter="MTLES",
            seven_letter="MTCL-MT",
            fourteen_letter="MATCHLESS-MT"
        ),
        latitude=38.834,
        longitude=-106.6451,
        height=12389.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MIDDLE_PEAK = Mountain(
        name="Middle Peak",
        abbreviations=Abbreviations(
            three_letter="MID",
            five_letter="MIDDL",
            seven_letter="MID-PK",
            fourteen_letter="MIDDLE-PK"
        ),
        latitude=37.8536,
        longitude=-108.1082,
        height=13306.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_ANTERO = Mountain(
        name="Mount Antero",
        abbreviations=Abbreviations(
            three_letter="ATR",
            five_letter="ANTRO",
            seven_letter="MT-ANTR",
            fourteen_letter="MT-ANTERO"
        ),
        latitude=38.6741,
        longitude=-106.2462,
        height=14276.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_BLUE_SKY = Mountain(
        name="Mount Blue Sky",
        abbreviations=Abbreviations(
            three_letter="BLS",
            five_letter="BLSKY",
            seven_letter="MT-BLSK",
            fourteen_letter="MT-BLUE-SKY"
        ),
        latitude=39.5883,
        longitude=-105.6438,
        height=14271.0,
        nearest_airport=Airports.DENVER
    )
    MOUNT_CENTENNIAL = Mountain(
        name="Mount Centennial (Peak 13010)",
        abbreviations=Abbreviations(
            three_letter="CTL",
            five_letter="CENTL",
            seven_letter="MT-CNTL",
            fourteen_letter="MT-CENTNNL"
        ),
        latitude=37.6062,
        longitude=-107.2446,
        height=13016.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MOUNT_ELBERT = Mountain(
        name="Mount Elbert",
        abbreviations=Abbreviations(
            three_letter="LBT",
            five_letter="ELBRT",
            seven_letter="MT-ELBT",
            fourteen_letter="MT-ELBERT"
        ),
        latitude=39.1178,
        longitude=-106.4454,
        height=14440.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_GUERO = Mountain(
        name="Mount Guero",
        abbreviations=Abbreviations(
            three_letter="GRO",
            five_letter="GUERO",
            seven_letter="MT-GURO",
            fourteen_letter="MT-GUERO"
        ),
        latitude=38.7196,
        longitude=-107.3861,
        height=12058.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_GUNNISON = Mountain(
        name="Mount Gunnison",
        abbreviations=Abbreviations(
            three_letter="GUN",
            five_letter="GUNN",
            seven_letter="MT-GUNN",
            fourteen_letter="MT-GUNNISON"
        ),
        latitude=38.8121,
        longitude=-107.3826,
        height=12725.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_HARVARD = Mountain(
        name="Mount Harvard",
        abbreviations=Abbreviations(
            three_letter="HRV",
            five_letter="HARVD",
            seven_letter="MT-HVRD",
            fourteen_letter="MT-HARVARD"
        ),
        latitude=38.9244,
        longitude=-106.3207,
        height=14421.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_HERARD = Mountain(
        name="Mount Herard",
        abbreviations=Abbreviations(
            three_letter="HRD",
            five_letter="HERAD",
            seven_letter="MT-HERD",
            fourteen_letter="MT-HERARD"
        ),
        latitude=37.8492,
        longitude=-105.4949,
        height=13345.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_JACKSON = Mountain(
        name="Mount Jackson",
        abbreviations=Abbreviations(
            three_letter="JKS",
            five_letter="JKSON",
            seven_letter="MT-JKSN",
            fourteen_letter="MT-JACKSON"
        ),
        latitude=39.4853,
        longitude=-106.5367,
        height=13676.0,
        nearest_airport=Airports.EAGLE
    )
    MOUNT_LINCOLN = Mountain(
        name="Mount Lincoln",
        abbreviations=Abbreviations(
            three_letter="LCN",
            five_letter="LNCLN",
            seven_letter="MT-LNCN",
            fourteen_letter="MT-LINCOLN"
        ),
        latitude=39.3515,
        longitude=-106.1116,
        height=14293.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_MASSIVE = Mountain(
        name="Mount Massive",
        abbreviations=Abbreviations(
            three_letter="MSV",
            five_letter="MSSIV",
            seven_letter="MT-MSVE",
            fourteen_letter="MT-MASSIVE"
        ),
        latitude=39.1875,
        longitude=-106.4757,
        height=14428.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_MESTAS = Mountain(
        name="Mount Mestas",
        abbreviations=Abbreviations(
            three_letter="MST",
            five_letter="MSTAS",
            seven_letter="MT-MSTS",
            fourteen_letter="MT-MESTAS"
        ),
        latitude=37.583,
        longitude=-105.1474,
        height=11574.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_OSO = Mountain(
        name="Mount Oso",
        abbreviations=Abbreviations(
            three_letter="OSO",
            five_letter="OSO",
            seven_letter="MT-OSO",
            fourteen_letter="MT-OSO"
        ),
        latitude=37.607,
        longitude=-107.4936,
        height=13690.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MOUNT_OURAY = Mountain(
        name="Mount Ouray",
        abbreviations=Abbreviations(
            three_letter="OUR",
            five_letter="OURAY",
            seven_letter="MT-OURY",
            fourteen_letter="MT-OURAY"
        ),
        latitude=38.4227,
        longitude=-106.2247,
        height=13961.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_POWELL = Mountain(
        name="Mount Powell",
        abbreviations=Abbreviations(
            three_letter="PWL",
            five_letter="POWLL",
            seven_letter="MT-PWLL",
            fourteen_letter="MT-POWELL"
        ),
        latitude=39.7601,
        longitude=-106.3407,
        height=13586.0,
        nearest_airport=Airports.EAGLE
    )
    MOUNT_PRINCETON = Mountain(
        name="Mount Princeton",
        abbreviations=Abbreviations(
            three_letter="PRC",
            five_letter="PRINC",
            seven_letter="MT-PRCN",
            fourteen_letter="MT-PRINCTN"
        ),
        latitude=38.7492,
        longitude=-106.2424,
        height=14204.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_RICHTHOFEN = Mountain(
        name="Mount Richthofen",
        abbreviations=Abbreviations(
            three_letter="RTF",
            five_letter="RCTFN",
            seven_letter="MT-RCHT",
            fourteen_letter="MT-RICHTHFN"
        ),
        latitude=40.4695,
        longitude=-105.8945,
        height=12945.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MOUNT_SILVERHEELS = Mountain(
        name="Mount Silverheels",
        abbreviations=Abbreviations(
            three_letter="SVH",
            five_letter="SLVHL",
            seven_letter="MT-SLVH",
            fourteen_letter="MT-SILVRHLS"
        ),
        latitude=39.3394,
        longitude=-106.0054,
        height=13829.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_SNEFFELS = Mountain(
        name="Mount Sneffels",
        abbreviations=Abbreviations(
            three_letter="SNF",
            five_letter="SNFLS",
            seven_letter="MT-SNFF",
            fourteen_letter="MT-SNEFFELS"
        ),
        latitude=38.0038,
        longitude=-107.7923,
        height=14158.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_WILSON = Mountain(
        name="Mount Wilson",
        abbreviations=Abbreviations(
            three_letter="WIL",
            five_letter="WILSN",
            seven_letter="MT-WLSN",
            fourteen_letter="MT-WILSON"
        ),
        latitude=37.8391,
        longitude=-107.9916,
        height=14252.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_YALE = Mountain(
        name="Mount Yale",
        abbreviations=Abbreviations(
            three_letter="YAL",
            five_letter="YALE",
            seven_letter="MT-YALE",
            fourteen_letter="MT-YALE"
        ),
        latitude=38.8442,
        longitude=-106.3138,
        height=14200.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    MOUNT_ZIRKEL = Mountain(
        name="Mount Zirkel",
        abbreviations=Abbreviations(
            three_letter="ZRK",
            five_letter="ZIRKL",
            seven_letter="MT-ZRKL",
            fourteen_letter="MT-ZIRKEL"
        ),
        latitude=40.8313,
        longitude=-106.6631,
        height=12185.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MOUNT_ZWISCHEN = Mountain(
        name="Mount Zwischen",
        abbreviations=Abbreviations(
            three_letter="ZWC",
            five_letter="ZWISC",
            seven_letter="MT-ZWSN",
            fourteen_letter="MT-ZWISCHEN"
        ),
        latitude=37.7913,
        longitude=-105.4554,
        height=12011.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_OF_THE_HOLY_CROSS = Mountain(
        name="Mount of the Holy Cross",
        abbreviations=Abbreviations(
            three_letter="HCR",
            five_letter="HLYCR",
            seven_letter="MT-HLCR",
            fourteen_letter="MT-HOLY-CRS"
        ),
        latitude=39.4668,
        longitude=-106.4817,
        height=14011.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    NORTH_ARAPAHO_PEAK = Mountain(
        name="North Arapaho Peak",
        abbreviations=Abbreviations(
            three_letter="NAP",
            five_letter="NAPPK",
            seven_letter="NARP-PK",
            fourteen_letter="N-ARAPAHO-PK"
        ),
        latitude=40.0265,
        longitude=-105.6504,
        height=13508.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NORTH_MAMM_PEAK = Mountain(
        name="North Mamm Peak",
        abbreviations=Abbreviations(
            three_letter="NMP",
            five_letter="NMMPK",
            seven_letter="NMAM-PK",
            fourteen_letter="N-MAMM-PK"
        ),
        latitude=39.3865,
        longitude=-107.866,
        height=11126.0,
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PARK_CONE = Mountain(
        name="Park Cone",
        abbreviations=Abbreviations(
            three_letter="PKC",
            five_letter="PKCON",
            seven_letter="PRK-CNE",
            fourteen_letter="PARK-CONE"
        ),
        latitude=38.7967,
        longitude=-106.6028,
        height=12106.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PARKVIEW_MOUNTAIN = Mountain(
        name="Parkview Mountain",
        abbreviations=Abbreviations(
            three_letter="PKV",
            five_letter="PARKV",
            seven_letter="PKVIEW",
            fourteen_letter="PARKVIEW-MT"
        ),
        latitude=40.3303,
        longitude=-106.1363,
        height=12301.0,
        nearest_airport=Airports.EAGLE
    )
    PARRY_PEAK = Mountain(
        name="Parry Peak",
        abbreviations=Abbreviations(
            three_letter="PRY",
            five_letter="PARRY",
            seven_letter="PRRY-PK",
            fourteen_letter="PARRY-PK"
        ),
        latitude=39.8381,
        longitude=-105.7132,
        height=13397.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PIKES_PEAK = Mountain(
        name="Pikes Peak",
        abbreviations=Abbreviations(
            three_letter="PIK",
            five_letter="PIKES",
            seven_letter="PIKE-PK",
            fourteen_letter="PIKES-PK"
        ),
        latitude=38.8405,
        longitude=-105.0442,
        height=14115.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PUMA_PEAK = Mountain(
        name="Puma Peak",
        abbreviations=Abbreviations(
            three_letter="PUM",
            five_letter="PUMA",
            seven_letter="PUMA-PK",
            fourteen_letter="PUMA-PK"
        ),
        latitude=39.1572,
        longitude=-105.5815,
        height=11575.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    RED_TABLE_MOUNTAIN = Mountain(
        name="Red Table Mountain",
        abbreviations=Abbreviations(
            three_letter="RTB",
            five_letter="REDTB",
            seven_letter="RTBL-MT",
            fourteen_letter="REDTABLE-MT"
        ),
        latitude=39.4181,
        longitude=-106.7712,
        height=12043.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    RIO_GRANDE_PYRAMID = Mountain(
        name="Rio Grande Pyramid",
        abbreviations=Abbreviations(
            three_letter="RGP",
            five_letter="RGPYR",
            seven_letter="RIOG-PY",
            fourteen_letter="RIOGRND-PYR"
        ),
        latitude=37.6797,
        longitude=-107.3924,
        height=13827.0,
        nearest_airport=Airports.TELLURIDE
    )
    SAN_LUIS_PEAK = Mountain(
        name="San Luis Peak",
        abbreviations=Abbreviations(
            three_letter="SLP",
            five_letter="SLUIS",
            seven_letter="SANL-PK",
            fourteen_letter="SAN-LUIS-PK"
        ),
        latitude=37.9868,
        longitude=-106.9313,
        height=14022.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SAND_MOUNTAIN_NORTH = Mountain(
        name="Sand Mountain North",
        abbreviations=Abbreviations(
            three_letter="SDN",
            five_letter="SANDN",
            seven_letter="SNDMT-N",
            fourteen_letter="SANDMTN-N"
        ),
        latitude=40.7636,
        longitude=-107.0575,
        height=10884.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SAWTOOTH_MOUNTAIN = Mountain(
        name="Sawtooth Mountain",
        abbreviations=Abbreviations(
            three_letter="SWT",
            five_letter="SAWTH",
            seven_letter="SAWT-MT",
            fourteen_letter="SAWTOOTH-MT"
        ),
        latitude=38.274,
        longitude=-106.867,
        height=12153.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SHEEP_MOUNTAIN = Mountain(
        name="Sheep Mountain",
        abbreviations=Abbreviations(
            three_letter="SHP",
            five_letter="SHEEP",
            seven_letter="SHEP-MT",
            fourteen_letter="SHEEP-MTN"
        ),
        latitude=40.361,
        longitude=-106.2658,
        height=11825.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SLEEPY_CAT_PEAK = Mountain(
        name="Sleepy Cat Peak",
        abbreviations=Abbreviations(
            three_letter="SCP",
            five_letter="SLPCT",
            seven_letter="SLPY-PK",
            fourteen_letter="SLEEPY-CAT"
        ),
        latitude=40.1275,
        longitude=-107.5338,
        height=10853.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SOUTH_RIVER_PEAK = Mountain(
        name="South River Peak",
        abbreviations=Abbreviations(
            three_letter="SRP",
            five_letter="STHRV",
            seven_letter="SRIV-PK",
            fourteen_letter="S-RIVER-PK"
        ),
        latitude=37.5741,
        longitude=-106.9815,
        height=13154.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    SPECIMEN_MOUNTAIN = Mountain(
        name="Specimen Mountain",
        abbreviations=Abbreviations(
            three_letter="SPC",
            five_letter="SPECM",
            seven_letter="SPCM-MT",
            fourteen_letter="SPECIMEN-MT"
        ),
        latitude=40.4449,
        longitude=-105.8081,
        height=12494.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SPRUCE_MOUNTAIN = Mountain(
        name="Spruce Mountain",
        abbreviations=Abbreviations(
            three_letter="SPR",
            five_letter="SPRUC",
            seven_letter="SPRC-MT",
            fourteen_letter="SPRUCE-MTN"
        ),
        latitude=39.1973,
        longitude=-107.522,
        height=10838.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    SULTAN_MOUNTAIN = Mountain(
        name="Sultan Mountain",
        abbreviations=Abbreviations(
            three_letter="SLT",
            five_letter="SULTN",
            seven_letter="SLTN-MT",
            fourteen_letter="SULTAN-MTN"
        ),
        latitude=37.7859,
        longitude=-107.7038,
        height=13373.0,
        nearest_airport=Airports.TELLURIDE
    )
    SUMMIT_PEAK = Mountain(
        name="Summit Peak",
        abbreviations=Abbreviations(
            three_letter="SMT",
            five_letter="SUMMT",
            seven_letter="SUMT-PK",
            fourteen_letter="SUMMIT-PK"
        ),
        latitude=37.3506,
        longitude=-106.6968,
        height=13308.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    THIRTYNINE_MILE_MOUNTAIN = Mountain(
        name="Thirtynine Mile Mountain",
        abbreviations=Abbreviations(
            three_letter="39M",
            five_letter="39MIL",
            seven_letter="39MI-MT",
            fourteen_letter="39MILE-MTN"
        ),
        latitude=38.8324,
        longitude=-105.5553,
        height=11553.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TOMICHI_DOME = Mountain(
        name="Tomichi Dome",
        abbreviations=Abbreviations(
            three_letter="TMC",
            five_letter="TOMCH",
            seven_letter="TMCH-DM",
            fourteen_letter="TOMICHI-DM"
        ),
        latitude=38.4849,
        longitude=-106.5291,
        height=11471.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    TOWER_MOUNTAIN = Mountain(
        name="Tower Mountain",
        abbreviations=Abbreviations(
            three_letter="TWR",
            five_letter="TOWER",
            seven_letter="TOWR-MT",
            fourteen_letter="TOWER-MTN"
        ),
        latitude=37.8573,
        longitude=-107.623,
        height=13558.0,
        nearest_airport=Airports.TELLURIDE
    )
    TREASURE_MOUNTAIN = Mountain(
        name="Treasure Mountain",
        abbreviations=Abbreviations(
            three_letter="TRS",
            five_letter="TREAS",
            seven_letter="TRSR-MT",
            fourteen_letter="TREASURE-MT"
        ),
        latitude=39.0244,
        longitude=-107.1228,
        height=13535.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    TWILIGHT_PEAK = Mountain(
        name="Twilight Peak",
        abbreviations=Abbreviations(
            three_letter="TWL",
            five_letter="TWLIT",
            seven_letter="TWLT-PK",
            fourteen_letter="TWILIGHT-PK"
        ),
        latitude=37.663,
        longitude=-107.727,
        height=13163.0,
        nearest_airport=Airports.TELLURIDE
    )
    TWIN_SISTERS_PEAKS = Mountain(
        name="Twin Sisters Peaks",
        abbreviations=Abbreviations(
            three_letter="TSP",
            five_letter="TWSIS",
            seven_letter="TWIN-PK",
            fourteen_letter="TWNSISTRS"
        ),
        latitude=40.2886,
        longitude=-105.5175,
        height=11433.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    UNCOMPAHGRE_PEAK = Mountain(
        name="Uncompahgre Peak",
        abbreviations=Abbreviations(
            three_letter="UNC",
            five_letter="UNCPG",
            seven_letter="UNCP-PK",
            fourteen_letter="UNCOMPAHGRE"
        ),
        latitude=38.0717,
        longitude=-107.4621,
        height=14321.0,
        nearest_airport=Airports.TELLURIDE
    )
    UTE_PEAK = Mountain(
        name="Ute Peak",
        abbreviations=Abbreviations(
            three_letter="UTE",
            five_letter="UTE",
            seven_letter="UTE-PK",
            fourteen_letter="UTE-PEAK"
        ),
        latitude=37.2841,
        longitude=-108.7787,
        height=9984.0,
        nearest_airport=Airports.CORTEZ
    )
    VERMILION_PEAK = Mountain(
        name="Vermilion Peak",
        abbreviations=Abbreviations(
            three_letter="VRM",
            five_letter="VERML",
            seven_letter="VRML-PK",
            fourteen_letter="VERMILION-PK"
        ),
        latitude=37.7993,
        longitude=-107.8285,
        height=13900.0,
        nearest_airport=Airports.TELLURIDE
    )
    WAUGH_MOUNTAIN = Mountain(
        name="Waugh Mountain",
        abbreviations=Abbreviations(
            three_letter="WAU",
            five_letter="WAUGH",
            seven_letter="WAUG-MT",
            fourteen_letter="WAUGH-MTN"
        ),
        latitude=38.6022,
        longitude=-105.6955,
        height=11716.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WEST_BUFFALO_PEAK = Mountain(
        name="West Buffalo Peak",
        abbreviations=Abbreviations(
            three_letter="WBF",
            five_letter="WBUFF",
            seven_letter="WBUF-PK",
            fourteen_letter="W-BUFFALO-PK"
        ),
        latitude=38.9917,
        longitude=-106.1249,
        height=13332.0,
        nearest_airport=Airports.ASPEN_PITKIN
    )
    WEST_ELK_PEAK = Mountain(
        name="West Elk Peak",
        abbreviations=Abbreviations(
            three_letter="WEP",
            five_letter="WELK",
            seven_letter="WELK-PK",
            fourteen_letter="W-ELK-PK"
        ),
        latitude=38.7179,
        longitude=-107.1994,
        height=13042.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WEST_SPANISH_PEAK = Mountain(
        name="West Spanish Peak",
        abbreviations=Abbreviations(
            three_letter="WSP",
            five_letter="WSPAN",
            seven_letter="WSPA-PK",
            fourteen_letter="W-SPANISH-PK"
        ),
        latitude=37.3756,
        longitude=-104.9934,
        height=13631.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    WHETSTONE_MOUNTAIN = Mountain(
        name="Whetstone Mountain",
        abbreviations=Abbreviations(
            three_letter="WHT",
            five_letter="WHETS",
            seven_letter="WHTS-MT",
            fourteen_letter="WHETSTONE-MT"
        ),
        latitude=38.8223,
        longitude=-106.9799,
        height=12527.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WILLIAMS_PEAK = Mountain(
        name="Williams Peak",
        abbreviations=Abbreviations(
            three_letter="WLL",
            five_letter="WLLMS",
            seven_letter="WLMS-PK",
            fourteen_letter="WILLIAMS-PK"
        ),
        latitude=39.8552,
        longitude=-106.1854,
        height=11620.0,
        nearest_airport=Airports.EAGLE
    )
    WINDOM_PEAK = Mountain(
        name="Windom Peak",
        abbreviations=Abbreviations(
            three_letter="WND",
            five_letter="WNDOM",
            seven_letter="WNDM-PK",
            fourteen_letter="WINDOM-PK"
        ),
        latitude=37.6212,
        longitude=-107.5919,
        height=14093.0,
        nearest_airport=Airports.TELLURIDE
    )

    @property
    def height(self) -> str:
        """
        Get the height, in feet, of the mountain.
        :return: The height, in feet, of the mountain.
        :rtype: float
        """
        return self._location.height  # type: ignore
