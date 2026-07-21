from dataclasses import dataclass
from typing import Optional
from enum import Enum
from datetime import datetime


class Side(Enum):
    BID = 'bid'
    ASK = 'ask' 

class OrderType(Enum):
    MARKET = 'market'
    LIMIT = 'limit'

@dataclass
class Order:
    order_id: int
    side: Side
    order_type: OrderType
    price: Optional[float] # None for market orders — they execute at the best available price, not a fixed price
    quantity: int
    timestamp: datetime
    remaining_quantity: int

