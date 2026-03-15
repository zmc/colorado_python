from typing import Any

from colorado.airports import Airports
from colorado.base.populated_place import PopulatedPlace, PopulatedPlaceEnum, Abbreviations
from colorado.counties import Counties


class Municipality(PopulatedPlace):
    """
    Represents a municipality in the state of Colorado.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Municipalities(PopulatedPlaceEnum):
    """
    An enumeration of all municipalities in the state of Colorado.
    """
    AGUILAR = Municipality(
        name="Aguilar",
        abbreviations=Abbreviations(
            three_letter="AGU",
            five_letter="AGULR",
            seven_letter="AGUILAR",
            fourteen_letter="AGUILAR"
        ),
        latitude=37.40279920713442,
        longitude=-104.65332858227504,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    AKRON = Municipality(
        name="Akron",
        abbreviations=Abbreviations(
            three_letter="AKR",
            five_letter="AKRON",
            seven_letter="AKRON",
            fourteen_letter="AKRON"
        ),
        latitude=40.16054390057366,
        longitude=-103.21439404027768,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    ALAMOSA = Municipality(
        name="Alamosa",
        abbreviations=Abbreviations(
            three_letter="AMS",
            five_letter="ALMSA",
            seven_letter="ALAMOSA",
            fourteen_letter="ALAMOSA"
        ),
        latitude=37.46945514128652,
        longitude=-105.87003156514731,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ALMA = Municipality(
        name="Alma",
        abbreviations=Abbreviations(
            three_letter="ALM",
            five_letter="ALMA",
            seven_letter="ALMA",
            fourteen_letter="ALMA"
        ),
        latitude=39.283884582644646,
        longitude=-106.06280700139007,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    ANTONITO = Municipality(
        name="Antonito",
        abbreviations=Abbreviations(
            three_letter="ANT",
            five_letter="ANTNO",
            seven_letter="ANTNTO",
            fourteen_letter="ANTONITO"
        ),
        latitude=37.07918497659148,
        longitude=-106.00864295826494,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ARRIBA = Municipality(
        name="Arriba",
        abbreviations=Abbreviations(
            three_letter="ARB",
            five_letter="ARRBA",
            seven_letter="ARRIBA",
            fourteen_letter="ARRIBA"
        ),
        latitude=39.286106171651454,
        longitude=-103.2755051561436,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ARVADA = Municipality(
        name="Arvada",
        abbreviations=Abbreviations(
            three_letter="ARV",
            five_letter="ARVDA",
            seven_letter="ARVADA",
            fourteen_letter="ARVADA"
        ),
        latitude=39.802770821209435,
        longitude=-105.08749433847447,
        counties=[Counties.JEFFERSON, Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    ASPEN = Municipality(
        name="Aspen",
        abbreviations=Abbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN",
            fourteen_letter="ASPEN"
        ),
        latitude=39.19110451823167,
        longitude=-106.81754916020952,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    AULT = Municipality(
        name="Ault",
        abbreviations=Abbreviations(
            three_letter="ALT",
            five_letter="AULT",
            seven_letter="AULT",
            fourteen_letter="AULT"
        ),
        latitude=40.58248695250995,
        longitude=-104.73192134925284,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    AURORA = Municipality(
        name="Aurora",
        abbreviations=Abbreviations(
            three_letter="AUR",
            five_letter="AURRA",
            seven_letter="AURORA",
            fourteen_letter="AURORA"
        ),
        latitude=39.72943832854605,
        longitude=-104.83192957081997,
        counties=[Counties.ARAPAHOE, Counties.ADAMS, Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    AVON = Municipality(
        name="Avon",
        abbreviations=Abbreviations(
            three_letter="AVN",
            five_letter="AVON",
            seven_letter="AVON",
            fourteen_letter="AVON"
        ),
        latitude=39.63138119770201,
        longitude=-106.5222645450379,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BASALT = Municipality(
        name="Basalt",
        abbreviations=Abbreviations(
            three_letter="BST",
            five_letter="BSALT",
            seven_letter="BASALT",
            fourteen_letter="BASALT"
        ),
        latitude=39.36887932690354,
        longitude=-107.0328347281656,
        counties=[Counties.EAGLE, Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    BAYFIELD = Municipality(
        name="Bayfield",
        abbreviations=Abbreviations(
            three_letter="BYF",
            five_letter="BYFLD",
            seven_letter="BAYFLD",
            fourteen_letter="BAYFIELD"
        ),
        latitude=37.22556519746513,
        longitude=-107.59812272267197,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    BENNETT = Municipality(
        name="Bennett",
        abbreviations=Abbreviations(
            three_letter="BNT",
            five_letter="BENNT",
            seven_letter="BENNETT",
            fourteen_letter="BENNETT"
        ),
        latitude=39.758880060492515,
        longitude=-104.42747097979384,
        counties=[Counties.ADAMS, Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    BERTHOUD = Municipality(
        name="Berthoud",
        abbreviations=Abbreviations(
            three_letter="BRT",
            five_letter="BRTHD",
            seven_letter="BERTHD",
            fourteen_letter="BERTHOUD"
        ),
        latitude=40.308323890381644,
        longitude=-105.08110259705586,
        counties=[Counties.LARIMER, Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BETHUNE = Municipality(
        name="Bethune",
        abbreviations=Abbreviations(
            three_letter="BTH",
            five_letter="BTHNE",
            seven_letter="BETHUNE",
            fourteen_letter="BETHUNE"
        ),
        latitude=39.30416893007231,
        longitude=-102.42464895454725,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    BLACK_HAWK = Municipality(
        name="Black Hawk",
        abbreviations=Abbreviations(
            three_letter="BLH",
            five_letter="BLKHK",
            seven_letter="BLKHAWK",
            fourteen_letter="BLACKHAWK"
        ),
        latitude=39.796938591671164,
        longitude=-105.49389553091271,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BLANCA = Municipality(
        name="Blanca",
        abbreviations=Abbreviations(
            three_letter="BLA",
            five_letter="BLNCA",
            seven_letter="BLANCA",
            fourteen_letter="BLANCA"
        ),
        latitude=37.43806935871913,
        longitude=-105.51585598170686,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BLUE_RIVER = Municipality(
        name="Blue River",
        abbreviations=Abbreviations(
            three_letter="BLR",
            five_letter="BLRVR",
            seven_letter="BLRIVER",
            fourteen_letter="BLUERIVER"
        ),
        latitude=39.42971610358546,
        longitude=-106.04391771358416,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    BONANZA = Municipality(
        name="Bonanza",
        abbreviations=Abbreviations(
            three_letter="BNZ",
            five_letter="BNANZ",
            seven_letter="BONANZA",
            fourteen_letter="BONANZA"
        ),
        latitude=38.294727740533574,
        longitude=-106.14225271064538,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BOONE = Municipality(
        name="Boone",
        abbreviations=Abbreviations(
            three_letter="BNE",
            five_letter="BOONE",
            seven_letter="BOONE",
            fourteen_letter="BOONE"
        ),
        latitude=38.24861925662066,
        longitude=-104.25692017539552,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BOULDER = Municipality(
        name="Boulder",
        abbreviations=Abbreviations(
            three_letter="BDL",
            five_letter="BOULR",
            seven_letter="BOULDER",
            fourteen_letter="BOULDER"
        ),
        latitude=40.014992037079196,
        longitude=-105.27055580556157,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BOW_MAR = Municipality(
        name="Bow Mar",
        abbreviations=Abbreviations(
            three_letter="BWM",
            five_letter="BOWMR",
            seven_letter="BOWMAR",
            fourteen_letter="BOWMAR"
        ),
        latitude=39.628327399445595,
        longitude=-105.0499942109563,
        counties=[Counties.ARAPAHOE, Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BRANSON = Municipality(
        name="Branson",
        abbreviations=Abbreviations(
            three_letter="BRS",
            five_letter="BRNSN",
            seven_letter="BRANSON",
            fourteen_letter="BRANSON"
        ),
        latitude=37.017528796882175,
        longitude=-103.8844178678076,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    BRECKENRIDGE = Municipality(
        name="Breckenridge",
        abbreviations=Abbreviations(
            three_letter="BCK",
            five_letter="BRECK",
            seven_letter="BRKNRDG",
            fourteen_letter="BRECKENRIDGE"
        ),
        latitude=39.481660010867984,
        longitude=-106.03836211864223,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    BRIGHTON = Municipality(
        name="Brighton",
        abbreviations=Abbreviations(
            three_letter="BRT",
            five_letter="BRGHT",
            seven_letter="BRIGHTN",
            fourteen_letter="BRIGHTON"
        ),
        latitude=39.98526816452795,
        longitude=-104.82053839851977,
        counties=[Counties.ADAMS, Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    BROOKSIDE = Municipality(
        name="Brookside",
        abbreviations=Abbreviations(
            three_letter="BKS",
            five_letter="BRKSD",
            seven_letter="BROOKSD",
            fourteen_letter="BROOKSIDE"
        ),
        latitude=38.41528271983117,
        longitude=-105.19194360802419,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BROOMFIELD = Municipality(
        name="Broomfield",
        abbreviations=Abbreviations(
            three_letter="BRM",
            five_letter="BROOM",
            seven_letter="BROOMFD",
            fourteen_letter="BROOMFIELD"
        ),
        latitude=39.92054753645141,
        longitude=-105.08666055187217,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BRUSH = Municipality(
        name="Brush",
        abbreviations=Abbreviations(
            three_letter="BSH",
            five_letter="BRUSH",
            seven_letter="BRUSH",
            fourteen_letter="BRUSH"
        ),
        latitude=40.25887518606942,
        longitude=-103.6238465492246,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    BUENA_VISTA = Municipality(
        name="Buena Vista",
        abbreviations=Abbreviations(
            three_letter="BVT",
            five_letter="BNVST",
            seven_letter="BNVISTA",
            fourteen_letter="BUENAVISTA"
        ),
        latitude=38.842224017267654,
        longitude=-106.13113906746224,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    BURLINGTON = Municipality(
        name="Burlington",
        abbreviations=Abbreviations(
            three_letter="BRL",
            five_letter="BRLNG",
            seven_letter="BURLNGT",
            fourteen_letter="BURLINGTON"
        ),
        latitude=39.306114740695364,
        longitude=-102.2693657172918,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    CALHAN = Municipality(
        name="Calhan",
        abbreviations=Abbreviations(
            three_letter="CLH",
            five_letter="CLHAN",
            seven_letter="CALHAN",
            fourteen_letter="CALHAN"
        ),
        latitude=39.03555226719334,
        longitude=-104.29719586807113,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CAMPO = Municipality(
        name="Campo",
        abbreviations=Abbreviations(
            three_letter="CMP",
            five_letter="CAMPO",
            seven_letter="CAMPO",
            fourteen_letter="CAMPO"
        ),
        latitude=37.105025187708804,
        longitude=-102.57964697041172,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    CANON_CITY = Municipality(
        name="Cañon City",
        abbreviations=Abbreviations(
            three_letter="CNC",
            five_letter="CANON",
            seven_letter="CANCITY",
            fourteen_letter="CANONCITY"
        ),
        latitude=38.44099122033896,
        longitude=-105.24245702270053,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CARBONATE = Municipality(
        name="Carbonate",
        abbreviations=Abbreviations(
            three_letter="CRB",
            five_letter="CBNTE",
            seven_letter="CRBNATE",
            fourteen_letter="CARBONATE"
        ),
        latitude=39.7442926,
        longitude=-107.3494183,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    CARBONDALE = Municipality(
        name="Carbondale",
        abbreviations=Abbreviations(
            three_letter="CRD",
            five_letter="CBNDL",
            seven_letter="CRBDALE",
            fourteen_letter="CARBONDALE"
        ),
        latitude=39.402211618604326,
        longitude=-107.21117337181659,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    CASTLE_PINES = Municipality(
        name="Castle Pines",
        abbreviations=Abbreviations(
            three_letter="CSP",
            five_letter="CSTLP",
            seven_letter="CSTLPNS",
            fourteen_letter="CASTLEPINES"
        ),
        latitude=39.458051186501905,
        longitude=-104.89610115433231,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLE_ROCK = Municipality(
        name="Castle Rock",
        abbreviations=Abbreviations(
            three_letter="CSR",
            five_letter="CSTLR",
            seven_letter="CSTLRCK",
            fourteen_letter="CASTLEROCK"
        ),
        latitude=39.37221847758906,
        longitude=-104.8561002356409,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CEDAREDGE = Municipality(
        name="Cedaredge",
        abbreviations=Abbreviations(
            three_letter="CDG",
            five_letter="CREDG",
            seven_letter="CDREDGE",
            fourteen_letter="CEDAREDGE"
        ),
        latitude=38.90165480315932,
        longitude=-107.9264646710543,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CENTENNIAL = Municipality(
        name="Centennial",
        abbreviations=Abbreviations(
            three_letter="CEN",
            five_letter="CENTL",
            seven_letter="CENTNNL",
            fourteen_letter="CENTENNIAL"
        ),
        latitude=39.57916140479068,
        longitude=-104.87693276356094,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CENTER = Municipality(
        name="Center",
        abbreviations=Abbreviations(
            three_letter="CTR",
            five_letter="CENTR",
            seven_letter="CENTER",
            fourteen_letter="CENTER"
        ),
        latitude=37.75306236660913,
        longitude=-106.10864804650834,
        counties=[Counties.SAGUACHE, Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CENTRAL_CITY = Municipality(
        name="Central City",
        abbreviations=Abbreviations(
            three_letter="CCT",
            five_letter="CNTCY",
            seven_letter="CENCITY",
            fourteen_letter="CENTRALCITY"
        ),
        latitude=39.801938590971986,
        longitude=-105.51417413606902,
        counties=[Counties.GILPIN, Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CHERAW = Municipality(
        name="Cheraw",
        abbreviations=Abbreviations(
            three_letter="CRW",
            five_letter="CHRAW",
            seven_letter="CHERAW",
            fourteen_letter="CHERAW"
        ),
        latitude=38.10695778309707,
        longitude=-103.51022798692372,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    CHERRY_HILLS_VILLAGE = Municipality(
        name="Cherry Hills Village",
        abbreviations=Abbreviations(
            three_letter="CHV",
            five_letter="CHRVL",
            seven_letter="CHRVHLL",
            fourteen_letter="CHERRYHILLS"
        ),
        latitude=39.64166080743007,
        longitude=-104.95943539032072,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHEYENNE_WELLS = Municipality(
        name="Cheyenne Wells",
        abbreviations=Abbreviations(
            three_letter="CHW",
            five_letter="CHYWL",
            seven_letter="CHYWLLS",
            fourteen_letter="CHEYENNEWELLS"
        ),
        latitude=38.82140156342473,
        longitude=-102.35325288416135,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    COAL_CREEK = Municipality(
        name="Coal Creek",
        abbreviations=Abbreviations(
            three_letter="CLC",
            five_letter="COALC",
            seven_letter="COALCRK",
            fourteen_letter="COALCREEK"
        ),
        latitude=38.361117415151966,
        longitude=-105.14833219222083,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    COKEDALE = Municipality(
        name="Cokedale",
        abbreviations=Abbreviations(
            three_letter="CKD",
            five_letter="COKDL",
            seven_letter="COKEDAL",
            fourteen_letter="COKEDALE"
        ),
        latitude=37.14530357142036,
        longitude=-104.62110914995054,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    COLLBRAN = Municipality(
        name="Collbran",
        abbreviations=Abbreviations(
            three_letter="CLB",
            five_letter="COLLB",
            seven_letter="COLLBRN",
            fourteen_letter="COLLBRAN"
        ),
        latitude=39.24054044452362,
        longitude=-107.96119151783063,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    COLORADO_SPRINGS = Municipality(
        name="Colorado Springs",
        abbreviations=Abbreviations(
            three_letter="COS",
            five_letter="CSPRG",
            seven_letter="COSPRGS",
            fourteen_letter="COSPRINGS"
        ),
        latitude=38.83388790377501,
        longitude=-104.8213733682033,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    COLUMBINE_VALLEY = Municipality(
        name="Columbine Valley",
        abbreviations=Abbreviations(
            three_letter="CLV",
            five_letter="CLBVY",
            seven_letter="CLBNVLY",
            fourteen_letter="CLMBINE VALLEY"
        ),
        latitude=39.601105297271715,
        longitude=-105.03221610142771,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COMMERCE_CITY = Municipality(
        name="Commerce City",
        abbreviations=Abbreviations(
            three_letter="CMC",
            five_letter="CMRCE",
            seven_letter="COMCITY",
            fourteen_letter="COMMERCECITY"
        ),
        latitude=39.80832603235723,
        longitude=-104.93387760363186,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    CORTEZ = Municipality(
        name="Cortez",
        abbreviations=Abbreviations(
            three_letter="CRZ",
            five_letter="CRTEZ",
            seven_letter="CORTEZ",
            fourteen_letter="CORTEZ"
        ),
        latitude=37.34888855197022,
        longitude=-108.5859371477685,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    CRAIG = Municipality(
        name="Craig",
        abbreviations=Abbreviations(
            three_letter="CRG",
            five_letter="CRAIG",
            seven_letter="CRAIG",
            fourteen_letter="CRAIG"
        ),
        latitude=40.515255438601514,
        longitude=-107.5464648812731,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CRAWFORD = Municipality(
        name="Crawford",
        abbreviations=Abbreviations(
            three_letter="CRF",
            five_letter="CRWFD",
            seven_letter="CRWFORD",
            fourteen_letter="CRAWFORD"
        ),
        latitude=38.703882798126415,
        longitude=-107.60895718024449,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CREEDE = Municipality(
        name="Creede",
        abbreviations=Abbreviations(
            three_letter="CRD",
            five_letter="CREED",
            seven_letter="CREEDE",
            fourteen_letter="CREEDE"
        ),
        latitude=37.84917222718855,
        longitude=-106.92644483888739,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CRESTED_BUTTE = Municipality(
        name="Crested Butte",
        abbreviations=Abbreviations(
            three_letter="CRB",
            five_letter="CRSTB",
            seven_letter="CRSTBT",
            fourteen_letter="CRESTEDBUTTE"
        ),
        latitude=38.869720762929205,
        longitude=-106.98783366173689,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CRESTONE = Municipality(
        name="Crestone",
        abbreviations=Abbreviations(
            three_letter="CRS",
            five_letter="CRSTN",
            seven_letter="CRSTONE",
            fourteen_letter="CRESTONE"
        ),
        latitude=37.99639422771361,
        longitude=-105.6997432790177,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CRIPPLE_CREEK = Municipality(
        name="Cripple Creek",
        abbreviations=Abbreviations(
            three_letter="CRP",
            five_letter="CRPLC",
            seven_letter="CRPLCRK",
            fourteen_letter="CRIPPLECREEK"
        ),
        latitude=38.74666176812747,
        longitude=-105.17832494080608,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CROOK = Municipality(
        name="Crook",
        abbreviations=Abbreviations(
            three_letter="CRK",
            five_letter="CROOK",
            seven_letter="CROOK",
            fourteen_letter="CROOK"
        ),
        latitude=40.85888662779365,
        longitude=-102.80103612539585,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    CROWLEY = Municipality(
        name="Crowley",
        abbreviations=Abbreviations(
            three_letter="CRW",
            five_letter="CRWLY",
            seven_letter="CROWLEY",
            fourteen_letter="CROWLEY"
        ),
        latitude=38.19306697390681,
        longitude=-103.85607427606533,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    DACONO = Municipality(
        name="Dacono",
        abbreviations=Abbreviations(
            three_letter="DAC",
            five_letter="DACNO",
            seven_letter="DACONO",
            fourteen_letter="DACONO"
        ),
        latitude=40.08471266990625,
        longitude=-104.93943173791331,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    DE_BEQUE = Municipality(
        name="De Beque",
        abbreviations=Abbreviations(
            three_letter="DBQ",
            five_letter="DEBEQ",
            seven_letter="DEBEQUE",
            fourteen_letter="DEBEQUE"
        ),
        latitude=39.33442943909051,
        longitude=-108.21509238369515,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DEER_TRAIL = Municipality(
        name="Deer Trail",
        abbreviations=Abbreviations(
            three_letter="DRT",
            five_letter="DRTRL",
            seven_letter="DRTRAIL",
            fourteen_letter="DEERTRAIL"
        ),
        latitude=39.61498856692867,
        longitude=-104.0444131738684,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DEL_NORTE = Municipality(
        name="Del Norte",
        abbreviations=Abbreviations(
            three_letter="DLN",
            five_letter="DELNT",
            seven_letter="DELNORT",
            fourteen_letter="DELNORTE"
        ),
        latitude=37.678897940199704,
        longitude=-106.3533785937455,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    DELTA = Municipality(
        name="Delta",
        abbreviations=Abbreviations(
            three_letter="DLT",
            five_letter="DELTA",
            seven_letter="DELTA",
            fourteen_letter="DELTA"
        ),
        latitude=38.74221227221676,
        longitude=-108.06896888470965,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    DENVER = Municipality(
        name="Denver",
        abbreviations=Abbreviations(
            three_letter="DEN",
            five_letter="DENVR",
            seven_letter="DENVER",
            fourteen_letter="DENVER"
        ),
        latitude=39.73916001934174,
        longitude=-104.98471350720706,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    DILLON = Municipality(
        name="Dillon",
        abbreviations=Abbreviations(
            three_letter="DLN",
            five_letter="DLLN",
            seven_letter="DILLON",
            fourteen_letter="DILLON"
        ),
        latitude=39.630270631010035,
        longitude=-106.04336213702209,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    DINOSAUR = Municipality(
        name="Dinosaur",
        abbreviations=Abbreviations(
            three_letter="DNS",
            five_letter="DINOS",
            seven_letter="DINOSR",
            fourteen_letter="DINOSAUR"
        ),
        latitude=40.24358419608177,
        longitude=-109.01457236753077,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DOLORES = Municipality(
        name="Dolores",
        abbreviations=Abbreviations(
            three_letter="DLS",
            five_letter="DOLOS",
            seven_letter="DOLORES",
            fourteen_letter="DOLORES"
        ),
        latitude=37.47388767410109,
        longitude=-108.50454624276676,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    DOVE_CREEK = Municipality(
        name="Dove Creek",
        abbreviations=Abbreviations(
            three_letter="DVC",
            five_letter="DOVEC",
            seven_letter="DVCREEK",
            fourteen_letter="DOVECREEK"
        ),
        latitude=37.76610588633355,
        longitude=-108.90595005877037,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.CORTEZ
    )
    DURANGO = Municipality(
        name="Durango",
        abbreviations=Abbreviations(
            three_letter="DUR",
            five_letter="DURAN",
            seven_letter="DURANGO",
            fourteen_letter="DURANGO"
        ),
        latitude=37.275285887032624,
        longitude=-107.88007718883347,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    EADS = Municipality(
        name="Eads",
        abbreviations=Abbreviations(
            three_letter="EAD",
            five_letter="EADS",
            seven_letter="EADS",
            fourteen_letter="EADS"
        ),
        latitude=38.4805678851622,
        longitude=-102.78187235286333,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    EAGLE = Municipality(
        name="Eagle",
        abbreviations=Abbreviations(
            three_letter="EAG",
            five_letter="EAGLE",
            seven_letter="EAGLE",
            fourteen_letter="EAGLE"
        ),
        latitude=39.655269779267655,
        longitude=-106.82866121606952,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    EATON = Municipality(
        name="Eaton",
        abbreviations=Abbreviations(
            three_letter="EAT",
            five_letter="EATON",
            seven_letter="EATON",
            fourteen_letter="EATON"
        ),
        latitude=40.53026474664489,
        longitude=-104.71136433822358,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ECKLEY = Municipality(
        name="Eckley",
        abbreviations=Abbreviations(
            three_letter="ECK",
            five_letter="ECKLY",
            seven_letter="ECKLEY",
            fourteen_letter="ECKLEY"
        ),
        latitude=40.113883843500105,
        longitude=-102.4907671612292,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    EDGEWATER = Municipality(
        name="Edgewater",
        abbreviations=Abbreviations(
            three_letter="EDW",
            five_letter="EDGWT",
            seven_letter="EDGWATR",
            fourteen_letter="EDGEWATER"
        ),
        latitude=39.7530489155871,
        longitude=-105.06416042739124,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ELIZABETH = Municipality(
        name="Elizabeth",
        abbreviations=Abbreviations(
            three_letter="ELI",
            five_letter="ELIZB",
            seven_letter="ELZBETH",
            fourteen_letter="ELIZABETH"
        ),
        latitude=39.36027259311544,
        longitude=-104.5969249744677,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    EMPIRE = Municipality(
        name="Empire",
        abbreviations=Abbreviations(
            three_letter="EMP",
            five_letter="EMPR",
            seven_letter="EMPIRE",
            fourteen_letter="EMPIRE"
        ),
        latitude=39.761382673497906,
        longitude=-105.68445817047234,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ENGLEWOOD = Municipality(
        name="Englewood",
        abbreviations=Abbreviations(
            three_letter="ENL",
            five_letter="ENGLW",
            seven_letter="ENGLWD",
            fourteen_letter="ENGLEWOOD"
        ),
        latitude=39.647771706177764,
        longitude=-104.98776979768752,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    ERIE = Municipality(
        name="Erie",
        abbreviations=Abbreviations(
            three_letter="ERI",
            five_letter="ERIE",
            seven_letter="ERIE",
            fourteen_letter="ERIE"
        ),
        latitude=40.050268757471486,
        longitude=-105.04999186006529,
        counties=[Counties.WELD, Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ESTES_PARK = Municipality(
        name="Estes Park",
        abbreviations=Abbreviations(
            three_letter="ESP",
            five_letter="ESTPK",
            seven_letter="ESTPARK",
            fourteen_letter="ESTESPARK"
        ),
        latitude=40.37721236799962,
        longitude=-105.52167540735627,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EVANS = Municipality(
        name="Evans",
        abbreviations=Abbreviations(
            three_letter="EVA",
            five_letter="EVANS",
            seven_letter="EVANS",
            fourteen_letter="EVANS"
        ),
        latitude=40.37637662729253,
        longitude=-104.69219751501237,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FAIRPLAY = Municipality(
        name="Fairplay",
        abbreviations=Abbreviations(
            three_letter="FPL",
            five_letter="FAIRP",
            seven_letter="FAIRPLY",
            fourteen_letter="FAIRPLAY"
        ),
        latitude=39.22471887862463,
        longitude=-106.00197208064321,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    FEDERAL_HEIGHTS = Municipality(
        name="Federal Heights",
        abbreviations=Abbreviations(
            three_letter="FHE",
            five_letter="FEDHG",
            seven_letter="FEDHGTS",
            fourteen_letter="FEDHEIGHTS"
        ),
        latitude=39.85138113351388,
        longitude=-104.99860232388221,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    FIRESTONE = Municipality(
        name="Firestone",
        abbreviations=Abbreviations(
            three_letter="FST",
            five_letter="FIRES",
            seven_letter="FIRESTN",
            fourteen_letter="FIRESTONE"
        ),
        latitude=40.1124903740415,
        longitude=-104.93665374011795,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FLAGLER = Municipality(
        name="Flagler",
        abbreviations=Abbreviations(
            three_letter="FLG",
            five_letter="FLAGL",
            seven_letter="FLAGLER",
            fourteen_letter="FLAGLER"
        ),
        latitude=39.29305278608126,
        longitude=-103.06716780717863,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    FLEMING = Municipality(
        name="Fleming",
        abbreviations=Abbreviations(
            three_letter="FLM",
            five_letter="FLEMG",
            seven_letter="FLEMING",
            fourteen_letter="FLEMING"
        ),
        latitude=40.679998099875206,
        longitude=-102.83937241286526,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    FLORENCE = Municipality(
        name="Florence",
        abbreviations=Abbreviations(
            three_letter="FLR",
            five_letter="FLRNC",
            seven_letter="FLOREN",
            fourteen_letter="FLORENCE"
        ),
        latitude=38.39028392110623,
        longitude=-105.11860878820221,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FORT_COLLINS = Municipality(
        name="Fort Collins",
        abbreviations=Abbreviations(
            three_letter="FCL",
            five_letter="FOCO",
            seven_letter="FORTCLL",
            fourteen_letter="FORTCOLLINS"
        ),
        latitude=40.58526672731159,
        longitude=-105.08443323212572,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FORT_LUPTON = Municipality(
        name="Fort Lupton",
        abbreviations=Abbreviations(
            three_letter="FLP",
            five_letter="FLUPT",
            seven_letter="FORTLUP",
            fourteen_letter="FORTLUPTON"
        ),
        latitude=40.084711978487576,
        longitude=-104.81303760783112,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    FORT_MORGAN = Municipality(
        name="Fort Morgan",
        abbreviations=Abbreviations(
            three_letter="FMG",
            five_letter="FMORG",
            seven_letter="FORTMOR",
            fourteen_letter="FORTMORGAN"
        ),
        latitude=40.25026477242511,
        longitude=-103.79996089057028,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    FOUNTAIN = Municipality(
        name="Fountain",
        abbreviations=Abbreviations(
            three_letter="FTN",
            five_letter="FOUNT",
            seven_letter="FOUNTN",
            fourteen_letter="FOUNTAIN"
        ),
        latitude=38.68222529017055,
        longitude=-104.70081552335176,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FOWLER = Municipality(
        name="Fowler",
        abbreviations=Abbreviations(
            three_letter="FOW",
            five_letter="FOWLR",
            seven_letter="FOWLER",
            fourteen_letter="FOWLER"
        ),
        latitude=38.12917835433535,
        longitude=-104.0233031087464,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    FOXFIELD = Municipality(
        name="Foxfield",
        abbreviations=Abbreviations(
            three_letter="FXF",
            five_letter="FXFLD",
            seven_letter="FOXFLD",
            fourteen_letter="FOXFIELD"
        ),
        latitude=39.591661612488224,
        longitude=-104.79248494554628,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    FRASER = Municipality(
        name="Fraser",
        abbreviations=Abbreviations(
            three_letter="FRS",
            five_letter="FRASR",
            seven_letter="FRASER",
            fourteen_letter="FRASER"
        ),
        latitude=39.94499318934146,
        longitude=-105.8172419228473,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FREDERICK = Municipality(
        name="Frederick",
        abbreviations=Abbreviations(
            three_letter="FRD",
            five_letter="FREDK",
            seven_letter="FREDRCK",
            fourteen_letter="FREDERICK"
        ),
        latitude=40.09915707212315,
        longitude=-104.93720943885103,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    FRISCO = Municipality(
        name="Frisco",
        abbreviations=Abbreviations(
            three_letter="FRI",
            five_letter="FRSCO",
            seven_letter="FRISCO",
            fourteen_letter="FRISCO"
        ),
        latitude=39.57443721917679,
        longitude=-106.09753074269054,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    FRUITA = Municipality(
        name="Fruita",
        abbreviations=Abbreviations(
            three_letter="FRU",
            five_letter="FRUIT",
            seven_letter="FRUITA",
            fourteen_letter="FRUITA"
        ),
        latitude=39.15887568050579,
        longitude=-108.72899907417974,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GARDEN_CITY = Municipality(
        name="Garden City",
        abbreviations=Abbreviations(
            three_letter="GDC",
            five_letter="GRDNC",
            seven_letter="GARDEN",
            fourteen_letter="GARDENCITY"
        ),
        latitude=40.393876529410534,
        longitude=-104.68941941660574,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GENOA = Municipality(
        name="Genoa",
        abbreviations=Abbreviations(
            three_letter="GNO",
            five_letter="GENOA",
            seven_letter="GENOA",
            fourteen_letter="GENOA"
        ),
        latitude=39.27832725508563,
        longitude=-103.50023360775361,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GEORGETOWN = Municipality(
        name="Georgetown",
        abbreviations=Abbreviations(
            three_letter="GEO",
            five_letter="GEORT",
            seven_letter="GEORGTN",
            fourteen_letter="GEORGETOWN"
        ),
        latitude=39.706104765436294,
        longitude=-105.69751436745668,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GILCREST = Municipality(
        name="Gilcrest",
        abbreviations=Abbreviations(
            three_letter="GLC",
            five_letter="GLCST",
            seven_letter="GILCRST",
            fourteen_letter="GILCREST"
        ),
        latitude=40.28193310830176,
        longitude=-104.77775732338125,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GLENDALE = Municipality(
        name="Glendale",
        abbreviations=Abbreviations(
            three_letter="GLN",
            five_letter="GLNDL",
            seven_letter="GLENDA",
            fourteen_letter="GLENDALE"
        ),
        latitude=39.70499371841959,
        longitude=-104.9336005919443,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GLENWOOD_SPRINGS = Municipality(
        name="Glenwood Springs",
        abbreviations=Abbreviations(
            three_letter="GLW",
            five_letter="GLWDS",
            seven_letter="GWSPRGS",
            fourteen_letter="GLNWOODSPRINGS"
        ),
        latitude=39.55054383038498,
        longitude=-107.32478681461873,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    GOLDEN = Municipality(
        name="Golden",
        abbreviations=Abbreviations(
            three_letter="GLD",
            five_letter="GLDN",
            seven_letter="GOLDEN",
            fourteen_letter="GOLDEN"
        ),
        latitude=39.75554940484966,
        longitude=-105.22110986342881,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GRANADA = Municipality(
        name="Granada",
        abbreviations=Abbreviations(
            three_letter="GRN",
            five_letter="GRNDA",
            seven_letter="GRANADA",
            fourteen_letter="GRANADA"
        ),
        latitude=38.06390455206366,
        longitude=-102.31047669765462,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    GRANBY = Municipality(
        name="Granby",
        abbreviations=Abbreviations(
            three_letter="GRB",
            five_letter="GRNBY",
            seven_letter="GRANBY",
            fourteen_letter="GRANBY"
        ),
        latitude=40.086103399087506,
        longitude=-105.93947006729013,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GRAND_JUNCTION = Municipality(
        name="Grand Junction",
        abbreviations=Abbreviations(
            three_letter="GJT",
            five_letter="GRJCT",
            seven_letter="GRNDJCT",
            fourteen_letter="GRANDJUNCTION"
        ),
        latitude=39.06387658040359,
        longitude=-108.55065942531371,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GRAND_LAKE = Municipality(
        name="Grand Lake",
        abbreviations=Abbreviations(
            three_letter="GDL",
            five_letter="GRDLK",
            seven_letter="GRANDLK",
            fourteen_letter="GRANDLAKE"
        ),
        latitude=40.25221372956071,
        longitude=-105.82307746067949,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GREELEY = Municipality(
        name="Greeley",
        abbreviations=Abbreviations(
            three_letter="GRL",
            five_letter="GRELY",
            seven_letter="GREELY",
            fourteen_letter="GREELEY"
        ),
        latitude=40.423320732340756,
        longitude=-104.70914232482562,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GREEN_MOUNTAIN_FALLS = Municipality(
        name="Green Mountain Falls",
        abbreviations=Abbreviations(
            three_letter="GMF",
            five_letter="GRMNT",
            seven_letter="GRMTFLS",
            fourteen_letter="GREENMTNFALLS"
        ),
        latitude=38.934996805106266,
        longitude=-105.01693632348514,
        counties=[Counties.EL_PASO, Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREENWOOD_VILLAGE = Municipality(
        name="Greenwood Village",
        abbreviations=Abbreviations(
            three_letter="GRV",
            five_letter="GRWDV",
            seven_letter="GRWDVL",
            fourteen_letter="GREENWOODVLG"
        ),
        latitude=39.617216504763064,
        longitude=-104.95082418492291,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GROVER = Municipality(
        name="Grover",
        abbreviations=Abbreviations(
            three_letter="GVR",
            five_letter="GROVR",
            seven_letter="GROVER",
            fourteen_letter="GROVER"
        ),
        latitude=40.87137952792369,
        longitude=-104.22523756640345,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GUNNISON = Municipality(
        name="Gunnison",
        abbreviations=Abbreviations(
            three_letter="GUN",
            five_letter="GUNN",
            seven_letter="GUNNISN",
            fourteen_letter="GUNNISON"
        ),
        latitude=38.54583072305218,
        longitude=-106.92533111208968,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    GYPSUM = Municipality(
        name="Gypsum",
        abbreviations=Abbreviations(
            three_letter="GYP",
            five_letter="GYPSM",
            seven_letter="GYPSUM",
            fourteen_letter="GYPSUM"
        ),
        latitude=39.64693576935315,
        longitude=-106.9517214430108,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    HARTMAN = Municipality(
        name="Hartman",
        abbreviations=Abbreviations(
            three_letter="HRT",
            five_letter="HRTMN",
            seven_letter="HARTMAN",
            fourteen_letter="HARTMAN"
        ),
        latitude=38.12029426615311,
        longitude=-102.21991968173444,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    HAXTUN = Municipality(
        name="Haxtun",
        abbreviations=Abbreviations(
            three_letter="HAX",
            five_letter="HAXTN",
            seven_letter="HAXTUN",
            fourteen_letter="HAXTUN"
        ),
        latitude=40.641108909376555,
        longitude=-102.62686805687667,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    HAYDEN = Municipality(
        name="Hayden",
        abbreviations=Abbreviations(
            three_letter="HAY",
            five_letter="HAYDN",
            seven_letter="HAYDEN",
            fourteen_letter="HAYDEN"
        ),
        latitude=40.49529335752396,
        longitude=-107.25729871485771,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HILLROSE = Municipality(
        name="Hillrose",
        abbreviations=Abbreviations(
            three_letter="HRS",
            five_letter="HILRS",
            seven_letter="HILLRS",
            fourteen_letter="HILLROSE"
        ),
        latitude=40.325819502574404,
        longitude=-103.52189883351787,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    HOLLY = Municipality(
        name="Holly",
        abbreviations=Abbreviations(
            three_letter="HOL",
            five_letter="HOLLY",
            seven_letter="HOLLY",
            fourteen_letter="HOLLY"
        ),
        latitude=38.05224006183107,
        longitude=-102.12269425137288,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    HOLYOKE = Municipality(
        name="Holyoke",
        abbreviations=Abbreviations(
            three_letter="HLY",
            five_letter="HOLYK",
            seven_letter="HOLYOKE",
            fourteen_letter="HOLYOKE"
        ),
        latitude=40.584443624000585,
        longitude=-102.30241987136469,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    HOOPER = Municipality(
        name="Hooper",
        abbreviations=Abbreviations(
            three_letter="HPR",
            five_letter="HOOPR",
            seven_letter="HOOPER",
            fourteen_letter="HOOPER"
        ),
        latitude=37.74278368036585,
        longitude=-105.8753087937423,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HOT_SULPHER_SPRINGS = Municipality(
        name="Hot Sulphur Springs",
        abbreviations=Abbreviations(
            three_letter="HSS",
            five_letter="HTSUL",
            seven_letter="HTSULP",
            fourteen_letter="HOTSLPSPRINGS"
        ),
        latitude=40.07304748573205,
        longitude=-106.10280950291315,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    HOTCHKISS = Municipality(
        name="Hotchkiss",
        abbreviations=Abbreviations(
            three_letter="HCK",
            five_letter="HOTCK",
            seven_letter="HOTCHKS",
            fourteen_letter="HOTCHKISS"
        ),
        latitude=38.79971310347622,
        longitude=-107.71951381423827,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    HUDSON = Municipality(
        name="Hudson",
        abbreviations=Abbreviations(
            three_letter="HDS",
            five_letter="HUDSN",
            seven_letter="HUDSON",
            fourteen_letter="HUDSON"
        ),
        latitude=40.07360058949382,
        longitude=-104.64302996707443,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    HUGO = Municipality(
        name="Hugo",
        abbreviations=Abbreviations(
            three_letter="HUG",
            five_letter="HUGO",
            seven_letter="HUGO",
            fourteen_letter="HUGO"
        ),
        latitude=39.136106837064915,
        longitude=-103.46995438552602,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    IDAHO_SPRINGS = Municipality(
        name="Idaho Springs",
        abbreviations=Abbreviations(
            three_letter="IDS",
            five_letter="IDSPR",
            seven_letter="IDSPRGS",
            fourteen_letter="IDAHOSPRINGS"
        ),
        latitude=39.74249448316948,
        longitude=-105.5136184292511,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    IGNACIO = Municipality(
        name="Ignacio",
        abbreviations=Abbreviations(
            three_letter="IGN",
            five_letter="IGNAC",
            seven_letter="IGNACIO",
            fourteen_letter="IGNACIO"
        ),
        latitude=37.115009580496064,
        longitude=-107.63312341906595,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ILIFF = Municipality(
        name="Iliff",
        abbreviations=Abbreviations(
            three_letter="ILF",
            five_letter="ILIFF",
            seven_letter="ILIFF",
            fourteen_letter="ILIFF"
        ),
        latitude=40.75916269480257,
        longitude=-103.06659917719702,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    JAMESTOWN = Municipality(
        name="Jamestown",
        abbreviations=Abbreviations(
            three_letter="JAM",
            five_letter="JAMST",
            seven_letter="JAMESTN",
            fourteen_letter="JAMESTOWN"
        ),
        latitude=40.11554764251014,
        longitude=-105.38861534487802,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JOHNSTOWN = Municipality(
        name="Johnstown",
        abbreviations=Abbreviations(
            three_letter="JHN",
            five_letter="JOHNS",
            seven_letter="JOHNSTN",
            fourteen_letter="JOHNSTOWN"
        ),
        latitude=40.336933706200284,
        longitude=-104.91220686131345,
        counties=[Counties.WELD, Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JULESBURG = Municipality(
        name="Julesburg",
        abbreviations=Abbreviations(
            three_letter="JUL",
            five_letter="JULSB",
            seven_letter="JULSBRG",
            fourteen_letter="JULESBURG"
        ),
        latitude=40.98833258373469,
        longitude=-102.26436151096613,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    KEENESBURG = Municipality(
        name="Keenesburg",
        abbreviations=Abbreviations(
            three_letter="KNS",
            five_letter="KEENS",
            seven_letter="KEENSBG",
            fourteen_letter="KEENESBURG"
        ),
        latitude=40.108322302224224,
        longitude=-104.51996854267901,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    KERSEY = Municipality(
        name="Kersey",
        abbreviations=Abbreviations(
            three_letter="KRS",
            five_letter="KERSY",
            seven_letter="KERSEY",
            fourteen_letter="KERSEY"
        ),
        latitude=40.38748753767152,
        longitude=-104.56163568620377,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KEYSTONE = Municipality(
        name="Keystone",
        abbreviations=Abbreviations(
            three_letter="KYS",
            five_letter="KEYST",
            seven_letter="KEYSTN",
            fourteen_letter="KEYSTONE"
        ),
        latitude=39.59943743055959,
        longitude=-105.98724892041025,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    KIM = Municipality(
        name="Kim",
        abbreviations=Abbreviations(
            three_letter="KIM",
            five_letter="KIM",
            seven_letter="KIM",
            fourteen_letter="KIM"
        ),
        latitude=37.246691664210175,
        longitude=-103.35217056522134,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    KIOWA = Municipality(
        name="Kiowa",
        abbreviations=Abbreviations(
            three_letter="KIW",
            five_letter="KIOWA",
            seven_letter="KIOWA",
            fourteen_letter="KIOWA"
        ),
        latitude=39.34721590041636,
        longitude=-104.46442114162693,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    KIT_CARSON = Municipality(
        name="Kit Carson",
        abbreviations=Abbreviations(
            three_letter="KIT",
            five_letter="KITCR",
            seven_letter="KITCRSN",
            fourteen_letter="KITCARSON"
        ),
        latitude=38.76111932616783,
        longitude=-102.78937618345088,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    KREMMLING = Municipality(
        name="Kremmling",
        abbreviations=Abbreviations(
            three_letter="KRM",
            five_letter="KRMML",
            seven_letter="KRMMLNG",
            fourteen_letter="KREMMLING"
        ),
        latitude=40.05888076379165,
        longitude=-106.38893036704059,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    LA_JARA = Municipality(
        name="La Jara",
        abbreviations=Abbreviations(
            three_letter="LJR",
            five_letter="LAJRA",
            seven_letter="LAJARA",
            fourteen_letter="LAJARA"
        ),
        latitude=37.27501440763774,
        longitude=-105.96031106632341,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_JUNTA = Municipality(
        name="La Junta",
        abbreviations=Abbreviations(
            three_letter="LJT",
            five_letter="LAJUN",
            seven_letter="LAJUNTA",
            fourteen_letter="LAJUNTA"
        ),
        latitude=37.9850153627396,
        longitude=-103.54384168182412,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    LA_VETA = Municipality(
        name="La Veta",
        abbreviations=Abbreviations(
            three_letter="LVT",
            five_letter="LAVTA",
            seven_letter="LAVETA",
            fourteen_letter="LAVETA"
        ),
        latitude=37.50501790061219,
        longitude=-105.00778457303471,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LAFAYETTE = Municipality(
        name="Lafayette",
        abbreviations=Abbreviations(
            three_letter="LAF",
            five_letter="LFYTE",
            seven_letter="LFAYTE",
            fourteen_letter="LAFAYETTE"
        ),
        latitude=39.99360234663493,
        longitude=-105.08971596110536,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    LAKE_CITY = Municipality(
        name="Lake City",
        abbreviations=Abbreviations(
            three_letter="LKC",
            five_letter="LKCTY",
            seven_letter="LKCITY",
            fourteen_letter="LAKECITY"
        ),
        latitude=38.03000272716531,
        longitude=-107.31534394264264,
        counties=[Counties.HINSDALE],
        nearest_airport=Airports.TELLURIDE
    )
    LAKESIDE = Municipality(
        name="Lakeside",
        abbreviations=Abbreviations(
            three_letter="LKS",
            five_letter="LAKSD",
            seven_letter="LAKSIDE",
            fourteen_letter="LAKESIDE"
        ),
        latitude=39.77721531946281,
        longitude=-105.05582672775438,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAKEWOOD = Municipality(
        name="Lakewood",
        abbreviations=Abbreviations(
            three_letter="LKW",
            five_letter="LAKWD",
            seven_letter="LKWOOD",
            fourteen_letter="LAKEWOOD"
        ),
        latitude=39.70471590756529,
        longitude=-105.08138352539805,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAMAR = Municipality(
        name="Lamar",
        abbreviations=Abbreviations(
            three_letter="LMR",
            five_letter="LAMAR",
            seven_letter="LAMAR",
            fourteen_letter="LAMAR"
        ),
        latitude=38.08723703638498,
        longitude=-102.62075897395562,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    LARKSPUR = Municipality(
        name="Larkspur",
        abbreviations=Abbreviations(
            three_letter="LRK",
            five_letter="LRKSP",
            seven_letter="LRKSPR",
            fourteen_letter="LARKSPUR"
        ),
        latitude=39.228608454987125,
        longitude=-104.88721312679161,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LAS_ANIMAS = Municipality(
        name="Las Animas",
        abbreviations=Abbreviations(
            three_letter="LAS",
            five_letter="LSANM",
            seven_letter="LSANMAS",
            fourteen_letter="LASANIMAS"
        ),
        latitude=38.066679795239736,
        longitude=-103.2227175152899,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    LASALLE = Municipality(
        name="LaSalle",
        abbreviations=Abbreviations(
            three_letter="LSL",
            five_letter="LASLL",
            seven_letter="LASALLE",
            fourteen_letter="LASALLE"
        ),
        latitude=40.3489,
        longitude=-104.7019,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LEADVILLE = Municipality(
        name="Leadville",
        abbreviations=Abbreviations(
            three_letter="LDV",
            five_letter="LEADV",
            seven_letter="LEADVLL",
            fourteen_letter="LEADVILLE"
        ),
        latitude=39.250829161129275,
        longitude=-106.29253414905992,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    LIMON = Municipality(
        name="Limon",
        abbreviations=Abbreviations(
            three_letter="LMN",
            five_letter="LIMON",
            seven_letter="LIMON",
            fourteen_letter="LIMON"
        ),
        latitude=39.26388264136767,
        longitude=-103.69218345092781,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LITTLETON = Municipality(
        name="Littleton",
        abbreviations=Abbreviations(
            three_letter="LIT",
            five_letter="LTTN",
            seven_letter="LTTN",
            fourteen_letter="LITTLETON"
        ),
        latitude=39.6133273999032,
        longitude=-105.01665990019404,
        counties=[Counties.ARAPAHOE, Counties.JEFFERSON, Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    LOCHBUIE = Municipality(
        name="Lochbuie",
        abbreviations=Abbreviations(
            three_letter="LCB",
            five_letter="LOCHB",
            seven_letter="LOCHBUI",
            fourteen_letter="LOCHBUIE"
        ),
        latitude=40.007212074714175,
        longitude=-104.71608927629381,
        counties=[Counties.WELD, Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    LOG_LANE_VILLAGE = Municipality(
        name="Log Lane Village",
        abbreviations=Abbreviations(
            three_letter="LLV",
            five_letter="LOGLV",
            seven_letter="LOGLNVL",
            fourteen_letter="LOGLANEVLG"
        ),
        latitude=40.27054297349616,
        longitude=-103.8296830998296,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    LONE_TREE = Municipality(
        name="Lone Tree",
        abbreviations=Abbreviations(
            three_letter="LNT",
            five_letter="LNTRE",
            seven_letter="LNTREE",
            fourteen_letter="LONETREE"
        ),
        latitude=39.5313873989478,
        longitude=-104.86197205463094,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    LONGMONT = Municipality(
        name="Longmont",
        abbreviations=Abbreviations(
            three_letter="LGM",
            five_letter="LONGM",
            seven_letter="LONGMT",
            fourteen_letter="LONGMONT"
        ),
        latitude=40.167213369566355,
        longitude=-105.10193768517456,
        counties=[Counties.BOULDER, Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LOUISVILLE = Municipality(
        name="Louisville",
        abbreviations=Abbreviations(
            three_letter="LOU",
            five_letter="LSVL",
            seven_letter="LSVL",
            fourteen_letter="LOUISVILLE"
        ),
        latitude=39.977769441487794,
        longitude=-105.13193976905217,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    LOVELAND = Municipality(
        name="Loveland",
        abbreviations=Abbreviations(
            three_letter="LOV",
            five_letter="LOVE",
            seven_letter="LOVELD",
            fourteen_letter="LOVELAND"
        ),
        latitude=40.39776770281662,
        longitude=-105.07499030714911,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LYONS = Municipality(
        name="Lyons",
        abbreviations=Abbreviations(
            three_letter="LYO",
            five_letter="LYONS",
            seven_letter="LYONS",
            fourteen_letter="LYONS"
        ),
        latitude=40.2247139651152,
        longitude=-105.27138823121618,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MANASSA = Municipality(
        name="Manassa",
        abbreviations=Abbreviations(
            three_letter="MNS",
            five_letter="MANSS",
            seven_letter="MANASSA",
            fourteen_letter="MANASSA"
        ),
        latitude=37.1741837945965,
        longitude=-105.93753155141616,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MANCOS = Municipality(
        name="Mancos",
        abbreviations=Abbreviations(
            three_letter="MNC",
            five_letter="MANC",
            seven_letter="MANCOS",
            fourteen_letter="MANCOS"
        ),
        latitude=37.34500187012043,
        longitude=-108.2892592833204,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    MANITOU_SPRINGS = Municipality(
        name="Manitou Springs",
        abbreviations=Abbreviations(
            three_letter="MNS",
            five_letter="MSPRG",
            seven_letter="MNSPRGS",
            fourteen_letter="MANITOUSPRINGS"
        ),
        latitude=38.859719000843654,
        longitude=-104.91720889281783,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MANZANOLA = Municipality(
        name="Manzanola",
        abbreviations=Abbreviations(
            three_letter="MZL",
            five_letter="MZLNA",
            seven_letter="MANZANL",
            fourteen_letter="MANZANOLA"
        ),
        latitude=38.1094571613765,
        longitude=-103.8660754698551,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    MARBLE = Municipality(
        name="Marble",
        abbreviations=Abbreviations(
            three_letter="MRB",
            five_letter="MARBL",
            seven_letter="MARBLE",
            fourteen_letter="MARBLE"
        ),
        latitude=39.07221677633197,
        longitude=-107.18894822883067,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    MEAD = Municipality(
        name="Mead",
        abbreviations=Abbreviations(
            three_letter="MED",
            five_letter="MEAD",
            seven_letter="MEAD",
            fourteen_letter="MEAD"
        ),
        latitude=40.23332388577927,
        longitude=-104.99860016882377,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MEEKER = Municipality(
        name="Meeker",
        abbreviations=Abbreviations(
            three_letter="MKR",
            five_letter="MEEKR",
            seven_letter="MEEKER",
            fourteen_letter="MEEKER"
        ),
        latitude=40.03747955105064,
        longitude=-107.91314070245346,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MERINO = Municipality(
        name="Merino",
        abbreviations=Abbreviations(
            three_letter="MRN",
            five_letter="MRINO",
            seven_letter="MERINO",
            fourteen_letter="MERINO"
        ),
        latitude=40.48248903652103,
        longitude=-103.3513377110703,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    MILLIKEN = Municipality(
        name="Milliken",
        abbreviations=Abbreviations(
            three_letter="MLK",
            five_letter="MILKN",
            seven_letter="MLLIKEN",
            fourteen_letter="MILLIKEN"
        ),
        latitude=40.329433308848195,
        longitude=-104.85526014735689,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MINTURN = Municipality(
        name="Minturn",
        abbreviations=Abbreviations(
            three_letter="MTR",
            five_letter="MNTUR",
            seven_letter="MINTURN",
            fourteen_letter="MINTURN"
        ),
        latitude=39.586381197849164,
        longitude=-106.4308735188348,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    MOFFAT = Municipality(
        name="Moffat",
        abbreviations=Abbreviations(
            three_letter="MOF",
            five_letter="MFFT",
            seven_letter="MOFFAT",
            fourteen_letter="MOFFAT"
        ),
        latitude=37.998894314008396,
        longitude=-105.91002572760954,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MONTE_VISTA = Municipality(
        name="Monte Vista",
        abbreviations=Abbreviations(
            three_letter="MTV",
            five_letter="MNVST",
            seven_letter="MNVISTA",
            fourteen_letter="MONTEVISTA"
        ),
        latitude=37.57917563945995,
        longitude=-106.14809443786993,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MONTEZUMA = Municipality(
        name="Montezuma",
        abbreviations=Abbreviations(
            three_letter="MTZ",
            five_letter="MNZMA",
            seven_letter="MNTZUMA",
            fourteen_letter="MONTEZUMA"
        ),
        latitude=39.58110433619612,
        longitude=-105.86724409102396,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    MONTROSE = Municipality(
        name="Montrose",
        abbreviations=Abbreviations(
            three_letter="MTR",
            five_letter="MNTRO",
            seven_letter="MONTRSE",
            fourteen_letter="MONTROSE"
        ),
        latitude=38.478325850516626,
        longitude=-107.87618441321172,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    MONUMENT = Municipality(
        name="Monument",
        abbreviations=Abbreviations(
            three_letter="MNM",
            five_letter="MNMT",
            seven_letter="MONUMT",
            fourteen_letter="MONUMENT"
        ),
        latitude=39.091664937058795,
        longitude=-104.87276800771542,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MORRISON = Municipality(
        name="Morrison",
        abbreviations=Abbreviations(
            three_letter="MRN",
            five_letter="MORRN",
            seven_letter="MORRSON",
            fourteen_letter="MORRISON"
        ),
        latitude=39.65360519299031,
        longitude=-105.19110974506509,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNT_CRESTED_BUTTE = Municipality(
        name="Mount Crested Butte",
        abbreviations=Abbreviations(
            three_letter="MCB",
            five_letter="MTCB",
            seven_letter="MTCSTBT",
            fourteen_letter="MTCRESTEDBUTTE"
        ),
        latitude=38.90862516936443,
        longitude=-106.96947846189317,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    MOUNTAIN_VIEW = Municipality(
        name="Mountain View",
        abbreviations=Abbreviations(
            three_letter="MVW",
            five_letter="MTNVW",
            seven_letter="MTNVIEW",
            fourteen_letter="MOUNTAINVIEW"
        ),
        latitude=39.77443751945077,
        longitude=-105.05554902795734,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNTAIN_VILLAGE = Municipality(
        name="Mountain Village",
        abbreviations=Abbreviations(
            three_letter="MVL",
            five_letter="MTNVL",
            seven_letter="MTNVILL",
            fourteen_letter="MOUNTAINVLGE"
        ),
        latitude=37.93138867787246,
        longitude=-107.85646365016862,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    NATURITA = Municipality(
        name="Naturita",
        abbreviations=Abbreviations(
            three_letter="NAT",
            five_letter="NATUR",
            seven_letter="NATURT",
            fourteen_letter="NATURITA"
        ),
        latitude=38.21832986920998,
        longitude=-108.56871403449037,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    NEDERLAND = Municipality(
        name="Nederland",
        abbreviations=Abbreviations(
            three_letter="NED",
            five_letter="NEDER",
            seven_letter="NEDERL",
            fourteen_letter="NEDERLAND"
        ),
        latitude=39.96138231263194,
        longitude=-105.51084145463687,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NEW_CASTLE = Municipality(
        name="New Castle",
        abbreviations=Abbreviations(
            three_letter="NWC",
            five_letter="NEWCL",
            seven_letter="NEWCSTL",
            fourteen_letter="NEWCASTLE"
        ),
        latitude=39.57276471783331,
        longitude=-107.53645496394358,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    NORTHGLENN = Municipality(
        name="Northglenn",
        abbreviations=Abbreviations(
            three_letter="NGL",
            five_letter="NGLEN",
            seven_letter="NGLENN",
            fourteen_letter="NORTHGLENN"
        ),
        latitude=39.885547439134484,
        longitude=-104.98721272543037,
        counties=[Counties.ADAMS, Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    NORWOOD = Municipality(
        name="Norwood",
        abbreviations=Abbreviations(
            three_letter="NRW",
            five_letter="NORWD",
            seven_letter="NORWOOD",
            fourteen_letter="NORWOOD"
        ),
        latitude=38.130552075579885,
        longitude=-108.29231436556671,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    NUCLA = Municipality(
        name="Nucla",
        abbreviations=Abbreviations(
            three_letter="NUC",
            five_letter="NUCLA",
            seven_letter="NUCLA",
            fourteen_letter="NUCLA"
        ),
        latitude=38.26944067707865,
        longitude=-108.54787983570384,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    NUNN = Municipality(
        name="Nunn",
        abbreviations=Abbreviations(
            three_letter="NUN",
            five_letter="NUNN",
            seven_letter="NUNN",
            fourteen_letter="NUNN"
        ),
        latitude=40.703598265179835,
        longitude=-104.78081257630754,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    OAK_CREEK = Municipality(
        name="Oak Creek",
        abbreviations=Abbreviations(
            three_letter="OKC",
            five_letter="OAKCR",
            seven_letter="OAKCRK",
            fourteen_letter="OAKCREEK"
        ),
        latitude=40.27498695093249,
        longitude=-106.95839352078178,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    OLATHE = Municipality(
        name="Olathe",
        abbreviations=Abbreviations(
            three_letter="OLT",
            five_letter="OLATH",
            seven_letter="OLATHE",
            fourteen_letter="OLATHE"
        ),
        latitude=38.60499145983238,
        longitude=-107.98229905060197,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    OLNEY_SPRINGS = Municipality(
        name="Olney Springs",
        abbreviations=Abbreviations(
            three_letter="OLS",
            five_letter="OLNSP",
            seven_letter="OLNSPRG",
            fourteen_letter="OLNEYSPRINGS"
        ),
        latitude=38.1661224647267,
        longitude=-103.94468889449121,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    OPHIR = Municipality(
        name="Ophir",
        abbreviations=Abbreviations(
            three_letter="OPH",
            five_letter="OPHIR",
            seven_letter="OPHIR",
            fourteen_letter="OPHIR"
        ),
        latitude=37.85694516957318,
        longitude=-107.83257493776938,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    ORCHARD_CITY = Municipality(
        name="Orchard City",
        abbreviations=Abbreviations(
            three_letter="ORC",
            five_letter="ORCHD",
            seven_letter="ORCHCTY",
            fourteen_letter="ORCHARDCITY"
        ),
        latitude=38.82832219044815,
        longitude=-107.97091017259896,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    ORDWAY = Municipality(
        name="Ordway",
        abbreviations=Abbreviations(
            three_letter="ORD",
            five_letter="ORDWY",
            seven_letter="ORDWAY",
            fourteen_letter="ORDWAY"
        ),
        latitude=38.21806708393126,
        longitude=-103.7560702559187,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    OTIS = Municipality(
        name="Otis",
        abbreviations=Abbreviations(
            three_letter="OTI",
            five_letter="OTIS",
            seven_letter="OTIS",
            fourteen_letter="OTIS"
        ),
        latitude=40.148878816009756,
        longitude=-102.96300237920752,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    OURAY = Municipality(
        name="Ouray",
        abbreviations=Abbreviations(
            three_letter="OUR",
            five_letter="OURAY",
            seven_letter="OURAY",
            fourteen_letter="OURAY"
        ),
        latitude=38.02277760272227,
        longitude=-107.67145921964857,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    OVID = Municipality(
        name="Ovid",
        abbreviations=Abbreviations(
            three_letter="OVI",
            five_letter="OVID",
            seven_letter="OVID",
            fourteen_letter="OVID"
        ),
        latitude=40.9605541713928,
        longitude=-102.38797433745265,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    PAGOSA_SPRINGS = Municipality(
        name="Pagosa Springs",
        abbreviations=Abbreviations(
            three_letter="PGS",
            five_letter="PGSAS",
            seven_letter="PAGOSAS",
            fourteen_letter="PAGOSASPRINGS"
        ),
        latitude=37.269455940850605,
        longitude=-107.00977199870368,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    PALISADE = Municipality(
        name="Palisade",
        abbreviations=Abbreviations(
            three_letter="PLS",
            five_letter="PALIS",
            seven_letter="PALISD",
            fourteen_letter="PALISADE"
        ),
        latitude=39.11026490084913,
        longitude=-108.35093008733753,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PALMER_LAKE = Municipality(
        name="Palmer Lake",
        abbreviations=Abbreviations(
            three_letter="PML",
            five_letter="PALML",
            seven_letter="PALMLK",
            fourteen_letter="PALMERLAKE"
        ),
        latitude=39.12222013829518,
        longitude=-104.9172140212998,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PAOLI = Municipality(
        name="Paoli",
        abbreviations=Abbreviations(
            three_letter="PLI",
            five_letter="PAOLI",
            seven_letter="PAOLI",
            fourteen_letter="PAOLI"
        ),
        latitude=40.612220016848596,
        longitude=-102.47269891562667,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    PAONIA = Municipality(
        name="Paonia",
        abbreviations=Abbreviations(
            three_letter="PAN",
            five_letter="PAONI",
            seven_letter="PAONIA",
            fourteen_letter="PAONIA"
        ),
        latitude=38.86832652169471,
        longitude=-107.59201229497279,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    PARACHUTE = Municipality(
        name="Parachute",
        abbreviations=Abbreviations(
            three_letter="PRC",
            five_letter="PRCHT",
            seven_letter="PRCHUTE",
            fourteen_letter="PARACHUTE"
        ),
        latitude=39.45192866577594,
        longitude=-108.05286366281877,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PARKER = Municipality(
        name="Parker",
        abbreviations=Abbreviations(
            three_letter="PRK",
            five_letter="PARKR",
            seven_letter="PARKER",
            fourteen_letter="PARKER"
        ),
        latitude=39.51860660437933,
        longitude=-104.76137343061458,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PEETZ = Municipality(
        name="Peetz",
        abbreviations=Abbreviations(
            three_letter="PTZ",
            five_letter="PEETZ",
            seven_letter="PEETZ",
            fourteen_letter="PEETZ"
        ),
        latitude=40.96277091990271,
        longitude=-103.11243391254868,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    PIERCE = Municipality(
        name="Pierce",
        abbreviations=Abbreviations(
            three_letter="PIR",
            five_letter="PIERC",
            seven_letter="PIERCE",
            fourteen_letter="PIERCE"
        ),
        latitude=40.635542557952135,
        longitude=-104.75525596192023,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PITKIN = Municipality(
        name="Pitkin",
        abbreviations=Abbreviations(
            three_letter="PIT",
            five_letter="PITKN",
            seven_letter="PITKIN",
            fourteen_letter="PITKIN"
        ),
        latitude=38.60916735946631,
        longitude=-106.51670612848756,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PLATTEVILLE = Municipality(
        name="Platteville",
        abbreviations=Abbreviations(
            three_letter="PLV",
            five_letter="PLTVL",
            seven_letter="PLTVLE",
            fourteen_letter="PLATTEVILLE"
        ),
        latitude=40.21498939606772,
        longitude=-104.8227595261788,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PONCHA_SPRINGS = Municipality(
        name="Poncha Springs",
        abbreviations=Abbreviations(
            three_letter="PCS",
            five_letter="PCHAS",
            seven_letter="PONCHAS",
            fourteen_letter="PONCHASPRINGS"
        ),
        latitude=38.51278137505858,
        longitude=-106.07724861883315,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PRITCHETT = Municipality(
        name="Pritchett",
        abbreviations=Abbreviations(
            three_letter="PRT",
            five_letter="PRTCH",
            seven_letter="PRITCTT",
            fourteen_letter="PRITCHETT"
        ),
        latitude=37.370299612091685,
        longitude=-102.8596556614134,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    PUEBLO = Municipality(
        name="Pueblo",
        abbreviations=Abbreviations(
            three_letter="PUB",
            five_letter="PUEBL",
            seven_letter="PUEBLO",
            fourteen_letter="PUEBLO"
        ),
        latitude=38.25445343479271,
        longitude=-104.60915085773684,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    RAMAH = Municipality(
        name="Ramah",
        abbreviations=Abbreviations(
            three_letter="RMA",
            five_letter="RAMAH",
            seven_letter="RAMAH",
            fourteen_letter="RAMAH"
        ),
        latitude=39.12166178833019,
        longitude=-104.16580384681976,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    RANGELY = Municipality(
        name="Rangely",
        abbreviations=Abbreviations(
            three_letter="RAN",
            five_letter="RANGL",
            seven_letter="RANGLY",
            fourteen_letter="RANGELY"
        ),
        latitude=40.08748209192953,
        longitude=-108.80484020262759,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RAYMER = Municipality(
        name="Raymer",
        abbreviations=Abbreviations(
            three_letter="RYM",
            five_letter="RAYMR",
            seven_letter="RAYMER",
            fourteen_letter="RAYMER"
        ),
        latitude=40.60804842018672,
        longitude=-103.84246004382982,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    RED_CLIFF = Municipality(
        name="Red Cliff",
        abbreviations=Abbreviations(
            three_letter="RCL",
            five_letter="RCLIF",
            seven_letter="REDCLFF",
            fourteen_letter="REDCLIFF"
        ),
        latitude=39.51221459248302,
        longitude=-106.36809409673907,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    RICO = Municipality(
        name="Rico",
        abbreviations=Abbreviations(
            three_letter="RIC",
            five_letter="RICO",
            seven_letter="RICO",
            fourteen_letter="RICO"
        ),
        latitude=37.69277883455203,
        longitude=-108.03036076344199,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.TELLURIDE
    )
    RIDGWAY = Municipality(
        name="Ridgway",
        abbreviations=Abbreviations(
            three_letter="RDG",
            five_letter="RIDGW",
            seven_letter="RIDGWAY",
            fourteen_letter="RIDGWAY"
        ),
        latitude=38.152774514179725,
        longitude=-107.76173685322726,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    RIFLE = Municipality(
        name="Rifle",
        abbreviations=Abbreviations(
            three_letter="RIF",
            five_letter="RIFLE",
            seven_letter="RIFLE",
            fourteen_letter="RIFLE"
        ),
        latitude=39.53470849550695,
        longitude=-107.7831305137895,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ROCKVALE = Municipality(
        name="Rockvale",
        abbreviations=Abbreviations(
            three_letter="RKV",
            five_letter="ROCKV",
            seven_letter="ROCKVL",
            fourteen_letter="ROCKVALE"
        ),
        latitude=38.369728415553936,
        longitude=-105.16389889655676,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ROCKY_FORD = Municipality(
        name="Rocky Ford",
        abbreviations=Abbreviations(
            three_letter="RKF",
            five_letter="ROCKF",
            seven_letter="ROCKYFD",
            fourteen_letter="ROCKYFORD"
        ),
        latitude=38.05251426207832,
        longitude=-103.72023703056374,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ROMEO = Municipality(
        name="Romeo",
        abbreviations=Abbreviations(
            three_letter="RMO",
            five_letter="ROMEO",
            seven_letter="ROMEO",
            fourteen_letter="ROMEO"
        ),
        latitude=37.172238691342045,
        longitude=-105.98531046202828,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    RYE = Municipality(
        name="Rye",
        abbreviations=Abbreviations(
            three_letter="RYE",
            five_letter="RYE",
            seven_letter="RYE",
            fourteen_letter="RYE"
        ),
        latitude=37.923625567579904,
        longitude=-104.93027609685947,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SAGUACHE = Municipality(
        name="Saguache",
        abbreviations=Abbreviations(
            three_letter="SGC",
            five_letter="SAGCH",
            seven_letter="SAGCHE",
            fourteen_letter="SAGUACHE"
        ),
        latitude=38.08750611168176,
        longitude=-106.14197728897585,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SALIDA = Municipality(
        name="Salida",
        abbreviations=Abbreviations(
            three_letter="SLD",
            five_letter="SALID",
            seven_letter="SALIDA",
            fourteen_letter="SALIDA"
        ),
        latitude=38.53472548350504,
        longitude=-105.99891240351411,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SAN_LUIS = Municipality(
        name="San Luis",
        abbreviations=Abbreviations(
            three_letter="SLS",
            five_letter="SLUIS",
            seven_letter="SANLUIS",
            fourteen_letter="SANLUIS"
        ),
        latitude=37.20085433015964,
        longitude=-105.42391113784294,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SANFORD = Municipality(
        name="Sanford",
        abbreviations=Abbreviations(
            three_letter="SFD",
            five_letter="SFORD",
            seven_letter="SANFORD",
            fourteen_letter="SANFORD"
        ),
        latitude=37.258348609583265,
        longitude=-105.90475425182558,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SAWPIT = Municipality(
        name="Sawpit",
        abbreviations=Abbreviations(
            three_letter="SAW",
            five_letter="SAWPT",
            seven_letter="SAWPIT",
            fourteen_letter="SAWPIT"
        ),
        latitude=37.995276176994764,
        longitude=-108.00174448899344,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    SEDGWICK = Municipality(
        name="Sedgwick",
        abbreviations=Abbreviations(
            three_letter="SDW",
            five_letter="SEDGW",
            seven_letter="SEDGWCK",
            fourteen_letter="SEDGWICK"
        ),
        latitude=40.936386657985054,
        longitude=-102.52547616746403,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    SEIBERT = Municipality(
        name="Seibert",
        abbreviations=Abbreviations(
            three_letter="SBT",
            five_letter="SBERT",
            seven_letter="SEIBERT",
            fourteen_letter="SEIBERT"
        ),
        latitude=39.299165600236734,
        longitude=-102.86910726052236,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    SEVERANCE = Municipality(
        name="Severance",
        abbreviations=Abbreviations(
            three_letter="SVR",
            five_letter="SEVRN",
            seven_letter="SEVRNC",
            fourteen_letter="SEVERANCE"
        ),
        latitude=40.52415443575012,
        longitude=-104.85109207043973,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SHERIDAN = Municipality(
        name="Sheridan",
        abbreviations=Abbreviations(
            three_letter="SHR",
            five_letter="SHERD",
            seven_letter="SHERID",
            fourteen_letter="SHERIDAN"
        ),
        latitude=39.646938303721754,
        longitude=-105.02527110559186,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SHERIDAN_LAKE = Municipality(
        name="Sheridan Lake",
        abbreviations=Abbreviations(
            three_letter="SHL",
            five_letter="SHERL",
            seven_letter="SHERLK",
            fourteen_letter="SHERIDLAKE"
        ),
        latitude=38.46668741401601,
        longitude=-102.29214023397287,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    SILT = Municipality(
        name="Silt",
        abbreviations=Abbreviations(
            three_letter="SLT",
            five_letter="SILT",
            seven_letter="SILT",
            fourteen_letter="SILT"
        ),
        latitude=39.548597906311045,
        longitude=-107.65618138745685,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    SILVER_CLIFF = Municipality(
        name="Silver Cliff",
        abbreviations=Abbreviations(
            three_letter="SVC",
            five_letter="SVCLF",
            seven_letter="SVCLFF",
            fourteen_letter="SILVERCLIFF"
        ),
        latitude=38.13528406364776,
        longitude=-105.44640023640204,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SILVER_PLUME = Municipality(
        name="Silver Plume",
        abbreviations=Abbreviations(
            three_letter="SVP",
            five_letter="SVPLM",
            seven_letter="SVPLME",
            fourteen_letter="SILVERPLUME"
        ),
        latitude=39.69610466161322,
        longitude=-105.7258488727399,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SILVERTHORNE = Municipality(
        name="Silverthorne",
        abbreviations=Abbreviations(
            three_letter="SVT",
            five_letter="SVTHR",
            seven_letter="SVTHRN",
            fourteen_letter="SILVERTHORNE"
        ),
        latitude=39.632145328770605,
        longitude=-106.07429134425666,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    SILVERTON = Municipality(
        name="Silverton",
        abbreviations=Abbreviations(
            three_letter="SVN",
            five_letter="SVLVT",
            seven_letter="SVLTON",
            fourteen_letter="SILVERTON"
        ),
        latitude=37.81194697461086,
        longitude=-107.66451619651315,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    SILMA = Municipality(
        name="Simla",
        abbreviations=Abbreviations(
            three_letter="SIL",
            five_letter="SILMA",
            seven_letter="SILMA",
            fourteen_letter="SIMLA"
        ),
        latitude=39.141661497053235,
        longitude=-104.0838577299719,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SNOWMASS_VILLAGE = Municipality(
        name="Snowmass Village",
        abbreviations=Abbreviations(
            three_letter="SMV",
            five_letter="SNMVS",
            seven_letter="SNMVLLG",
            fourteen_letter="SNOWMASSVLG"
        ),
        latitude=39.21304801267007,
        longitude=-106.93783118903116,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    SOUTH_FORK = Municipality(
        name="South Fork",
        abbreviations=Abbreviations(
            three_letter="SFK",
            five_letter="SFORK",
            seven_letter="SOUTHFK",
            fourteen_letter="SOUTHFORK"
        ),
        latitude=37.67001012062855,
        longitude=-106.63977405668572,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SPRINGFIELD = Municipality(
        name="Springfield",
        abbreviations=Abbreviations(
            three_letter="SPF",
            five_letter="SPRGF",
            seven_letter="SPRGFD",
            fourteen_letter="SPRINGFIELD"
        ),
        latitude=37.408354833005376,
        longitude=-102.61437090664646,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    STARKVILLE = Municipality(
        name="Starkville",
        abbreviations=Abbreviations(
            three_letter="SKV",
            five_letter="STARK",
            seven_letter="STARKVL",
            fourteen_letter="STARKVILLE"
        ),
        latitude=37.11530407296931,
        longitude=-104.52416302467543,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    STEAMBOAT_SPRINGS = Municipality(
        name="Steamboat Springs",
        abbreviations=Abbreviations(
            three_letter="STB",
            five_letter="STEAM",
            seven_letter="STMBOAT",
            fourteen_letter="STEAMBOATSPRGS"
        ),
        latitude=40.484983287346495,
        longitude=-106.83172641783767,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    STERLING = Municipality(
        name="Sterling",
        abbreviations=Abbreviations(
            three_letter="STL",
            five_letter="STERL",
            seven_letter="STERLN",
            fourteen_letter="STERLING"
        ),
        latitude=40.625548166277156,
        longitude=-103.20771879414866,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    STRATTON = Municipality(
        name="Stratton",
        abbreviations=Abbreviations(
            three_letter="STT",
            five_letter="STRAT",
            seven_letter="STRATN",
            fourteen_letter="STRATTON"
        ),
        latitude=39.30333411822744,
        longitude=-102.60465489741682,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SUGAR_CITY = Municipality(
        name="Sugar City",
        abbreviations=Abbreviations(
            three_letter="SGC",
            five_letter="SUGAR",
            seven_letter="SGRCITY",
            fourteen_letter="SUGARCITY"
        ),
        latitude=38.23195569224055,
        longitude=-103.66301073483965,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    SUPERIOR = Municipality(
        name="Superior",
        abbreviations=Abbreviations(
            three_letter="SUP",
            five_letter="SUPER",
            seven_letter="SUPRIOR",
            fourteen_letter="SUPERIOR"
        ),
        latitude=39.95276983553691,
        longitude=-105.16860787515753,
        counties=[Counties.BOULDER, Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SWINK = Municipality(
        name="Swink",
        abbreviations=Abbreviations(
            three_letter="SWK",
            five_letter="SWINK",
            seven_letter="SWINK",
            fourteen_letter="SWINK"
        ),
        latitude=38.01445926225392,
        longitude=-103.62828940461742,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    TELLURIDE = Municipality(
        name="Telluride",
        abbreviations=Abbreviations(
            three_letter="TEL",
            five_letter="TELLR",
            seven_letter="TELLUR",
            fourteen_letter="TELLURIDE"
        ),
        latitude=37.937499881928375,
        longitude=-107.81229574152144,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    THORNTON = Municipality(
        name="Thornton",
        abbreviations=Abbreviations(
            three_letter="THO",
            five_letter="THRTN",
            seven_letter="THRTON",
            fourteen_letter="THORNTON"
        ),
        latitude=39.8680476377578,
        longitude=-104.97193441982654,
        counties=[Counties.ADAMS, Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    TIMNATH = Municipality(
        name="Timnath",
        abbreviations=Abbreviations(
            three_letter="TIM",
            five_letter="TIMNT",
            seven_letter="TIMNATH",
            fourteen_letter="TIMNATH"
        ),
        latitude=40.52915562719477,
        longitude=-104.98526350163803,
        counties=[Counties.LARIMER, Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TRINIDAD = Municipality(
        name="Trinidad",
        abbreviations=Abbreviations(
            three_letter="TRI",
            five_letter="TRIND",
            seven_letter="TRINDD",
            fourteen_letter="TRINIDAD"
        ),
        latitude=37.16946928227463,
        longitude=-104.5005504247502,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    TWO_BUTTES = Municipality(
        name="Two Buttes",
        abbreviations=Abbreviations(
            three_letter="TWB",
            five_letter="TWOBT",
            seven_letter="TWOBTTE",
            fourteen_letter="TWOBUTTES"
        ),
        latitude=37.56113066965287,
        longitude=-102.39769796978601,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    VAIL = Municipality(
        name="Vail",
        abbreviations=Abbreviations(
            three_letter="VAI",
            five_letter="VAIL",
            seven_letter="VAIL",
            fourteen_letter="VAIL"
        ),
        latitude=39.640270108853656,
        longitude=-106.374205911437,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    VICTOR = Municipality(
        name="Victor",
        abbreviations=Abbreviations(
            three_letter="VIC",
            five_letter="VICTR",
            seven_letter="VICTOR",
            fourteen_letter="VICTOR"
        ),
        latitude=38.70999586538289,
        longitude=-105.13999072754666,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    VILAS = Municipality(
        name="Vilas",
        abbreviations=Abbreviations(
            three_letter="VLS",
            five_letter="VILAS",
            seven_letter="VILAS",
            fourteen_letter="VILAS"
        ),
        latitude=37.37363343792504,
        longitude=-102.44631026365687,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    VONA = Municipality(
        name="Vona",
        abbreviations=Abbreviations(
            three_letter="VON",
            five_letter="VONA",
            seven_letter="VONA",
            fourteen_letter="VONA"
        ),
        latitude=39.303610909350255,
        longitude=-102.74299263046106,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    WALDEN = Municipality(
        name="Walden",
        abbreviations=Abbreviations(
            three_letter="WLD",
            five_letter="WALDN",
            seven_letter="WALDEN",
            fourteen_letter="WALDEN"
        ),
        latitude=40.7316497593207,
        longitude=-106.28364782562318,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    WALSENBURG = Municipality(
        name="Walsenburg",
        abbreviations=Abbreviations(
            three_letter="WLB",
            five_letter="WALSN",
            seven_letter="WALSNB",
            fourteen_letter="WALSENBURG"
        ),
        latitude=37.62418543204245,
        longitude=-104.78027433273883,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    WALSH = Municipality(
        name="Walsh",
        abbreviations=Abbreviations(
            three_letter="WLS",
            five_letter="WALSH",
            seven_letter="WALSH",
            fourteen_letter="WALSH"
        ),
        latitude=37.38613334973962,
        longitude=-102.27824862443555,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    WARD = Municipality(
        name="Ward",
        abbreviations=Abbreviations(
            three_letter="WRD",
            five_letter="WARD",
            seven_letter="WARD",
            fourteen_letter="WARD"
        ),
        latitude=40.072214728272456,
        longitude=-105.50834186720596,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WELLINGTON = Municipality(
        name="Wellington",
        abbreviations=Abbreviations(
            three_letter="WEL",
            five_letter="WELLN",
            seven_letter="WELLGTN",
            fourteen_letter="WELLINGTON"
        ),
        latitude=40.70387774845142,
        longitude=-105.00859582899142,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WESTCLIFFE = Municipality(
        name="Westcliffe",
        abbreviations=Abbreviations(
            three_letter="WCL",
            five_letter="WCLFF",
            seven_letter="WESTCLF",
            fourteen_letter="WESTCLIFFE"
        ),
        latitude=38.13472816209804,
        longitude=-105.46584534062032,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    WESTMINSTER = Municipality(
        name="Westminster",
        abbreviations=Abbreviations(
            three_letter="WMS",
            five_letter="WSTMR",
            seven_letter="WSTMNR",
            fourteen_letter="WESTMINSTER"
        ),
        latitude=39.83665922908642,
        longitude=-105.0372147301137,
        counties=[Counties.ADAMS, Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WHEAT_RIDGE = Municipality(
        name="Wheat Ridge",
        abbreviations=Abbreviations(
            three_letter="WHR",
            five_letter="WHTRG",
            seven_letter="WHTRDGE",
            fourteen_letter="WHEATRIDGE"
        ),
        latitude=39.766104416930204,
        longitude=-105.0772164321362,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WIGGINS = Municipality(
        name="Wiggins",
        abbreviations=Abbreviations(
            three_letter="WIG",
            five_letter="WGGNS",
            seven_letter="WIGGINS",
            fourteen_letter="WIGGINS"
        ),
        latitude=40.230542851072016,
        longitude=-104.0727377527677,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    WILEY = Municipality(
        name="Wiley",
        abbreviations=Abbreviations(
            three_letter="WLY",
            five_letter="WILEY",
            seven_letter="WILEY",
            fourteen_letter="WILEY"
        ),
        latitude=38.154181139978334,
        longitude=-102.7196497047841,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    WILLIAMSBURG = Municipality(
        name="Williamsburg",
        abbreviations=Abbreviations(
            three_letter="WSB",
            five_letter="WMSBG",
            seven_letter="WILLMBG",
            fourteen_letter="WILLIAMSBURG"
        ),
        latitude=38.38195031786478,
        longitude=-105.15194309537117,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WINDSOR = Municipality(
        name="Windsor",
        abbreviations=Abbreviations(
            three_letter="WIN",
            five_letter="WINDS",
            seven_letter="WINDSR",
            fourteen_letter="WINDSOR"
        ),
        latitude=40.4774883261677,
        longitude=-104.90137187642983,
        counties=[Counties.WELD, Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WINTER_PARK = Municipality(
        name="Winter Park",
        abbreviations=Abbreviations(
            three_letter="WPK",
            five_letter="WINTP",
            seven_letter="WINTPK",
            fourteen_letter="WINTERPARK"
        ),
        latitude=39.8916600853978,
        longitude=-105.7630727036294,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WOODLAND_PARK = Municipality(
        name="Woodland Park",
        abbreviations=Abbreviations(
            three_letter="WLP",
            five_letter="WDLPK",
            seven_letter="WDLNDPK",
            fourteen_letter="WOODLANDPARK"
        ),
        latitude=38.993887110981234,
        longitude=-105.05694013924335,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WRAY = Municipality(
        name="Wray",
        abbreviations=Abbreviations(
            three_letter="WRA",
            five_letter="WRAY",
            seven_letter="WRAY",
            fourteen_letter="WRAY"
        ),
        latitude=40.075829756553446,
        longitude=-102.22325899183505,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    YAMPA = Municipality(
        name="Yampa",
        abbreviations=Abbreviations(
            three_letter="YMP",
            five_letter="YAMPA",
            seven_letter="YAMPA",
            fourteen_letter="YAMPA"
        ),
        latitude=40.152490038823714,
        longitude=-106.90866879458554,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    YUMA = Municipality(
        name="Yuma",
        abbreviations=Abbreviations(
            three_letter="YUM",
            five_letter="YUMA",
            seven_letter="YUMA",
            fourteen_letter="YUMA"
        ),
        latitude=40.12221502884205,
        longitude=-102.72521921912147,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
