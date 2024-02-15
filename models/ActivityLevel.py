from enum import Enum
from typing import Literal

class ActivityLevel(Enum):
    WEAK = "WEAK"
    GROWING = "GROWING"
    STRONG = "STRONG"
    RESTRICTED = "RESTRICTED"

activity_level = Literal[ActivityLevel]
