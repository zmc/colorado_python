from typing import Optional, Any

from colorado.internal import BaseModel


class LicensePlateCodes(BaseModel):
    """
    Represents the legacy license plate prefix ranges for counties in Colorado.

    In 1958, Colorado began issuing license plates with a specific 2-letter prefix that corresponds to the county of registration.
    By the 1980s, the 2-letter ranges had been exhausted, and the state switched to an 'ABC-123' format with a 3-letter prefix system for counties.
    By the end of 1999, county coding for license plates was discontinued.
    """
    # http://15q.net/coco.html
    two_letter_prefix_ranges: Optional[list[str]] = []
    three_letter_prefix_ranges: Optional[list[str]] = []

    def __init__(self, /, **data: Any):
        super().__init__(**data)
