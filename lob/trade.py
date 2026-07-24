from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Trade:
    """
    This is a complete match between a buy and a sell

    It is frozen as a trade should not be mutable after it has been filled
    """
    trade_id:int
    buy_order_id:int
    sell_order_id:int
    price:float
    quantity:int
    timestamp: datetime