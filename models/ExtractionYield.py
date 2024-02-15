from typing import Literal

from . import construction_material_trade_symbol

class ExtractionYield:
    symbol: Literal[construction_material_trade_symbol]
    units: int

extraction_yield = ExtractionYield