from collections import OrderedDict
from typing import Optional
from sortedcontainers import SortedDict
from lob.order import Order, Side, OrderType


class LimitOrderBook:

    def __init__(self):
        self.bids = SortedDict()
        self.asks = SortedDict()
        self.order_lookup: dict[int,Order] = {} # flat cancel lookup

    def add_limit_order(self, order: Order) -> None:
        if order.order_id in self.order_lookup:
            return ## this returns and stops dups from happening in the order book

        book = self.bids if order.side == Side.BUY else self.asks

        if order.price not in book:
            book[order.price] = OrderedDict()

        book[order.price][order.order_id] = order

        self.order_lookup[order.order_id] = order## update flat dictioanary


    def get_best_bid(self) -> Optional[float]:
        try:
            # Ascending bids: the highest price is at the very end (-1)
            price, _ = self.bids.peekitem(-1)
            return price
        except IndexError:
            return None

    def get_best_ask(self) -> Optional[float]:
        try:
            # Ascending asks: the lowest price is at the very beginning (0)
            price, _ = self.asks.peekitem(0)
            return price
        except IndexError:
            return None

    def get_spread(self) -> Optional[float]:
        bestBid = self.get_best_bid()
        bestAsk = self.get_best_ask()

        if bestBid is None or bestAsk is None:
            return None

        return bestBid - bestAsk


    def locate_order(self, order_id: int) -> Optional[Order]:
        # Use .get() so cancelling a non-existent order doesn't crash with a KeyError
        return self.order_lookup.get(order_id)

