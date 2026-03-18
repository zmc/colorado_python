from united_states import UnitedStates, State

from colorado.base.with_abbreviations import WithAbbreviations, Abbreviations
from colorado.base.with_borders import WithBorders
from colorado.base.with_name import WithName


class State(WithName, WithAbbreviations, WithBorders):
    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def coordinates_within_borders(self, latitude: float, longitude: float) -> bool:
        us = UnitedStates()
        states: list[State] = us.from_coords(latitude, longitude)
        for state in states:
            if state.abbr == 'CO':
                return True

        return False


COLORADO = State(
    name="Colorado",
    abbreviations=Abbreviations(
        three_letter="CO",
        five_letter="CO",
        seven_letter="CO",
        fourteen_letter="COLORADO"
    )
)
