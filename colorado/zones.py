import enum


class Zones(enum.Enum):
    """
    Represents the different zones for counties in Colorado, as defined by the Colorado Consortium for Prescription Drug Abuse Prevention.
    """
    # https://corxconsortium.org/wp-content/uploads/County-list.pdf
    URBAN = 0
    SUBURBAN = 1
    RURAL = 2
    FRONTIER = 3
