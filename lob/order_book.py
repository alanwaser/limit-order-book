from collections import OrderedDict
from typing import Optional
from sortedcontainers import SortedDict
from lob.order import Order, Side, OrderType
from lob.trade import Trade


class LimitOrderBook:

    def __init__(self):
        self.bids = SortedDict()
        self.asks = SortedDict()
        self.order_lookup: dict[int,Order] = {} # flat cancel lookup

    def add_limit_order(self, order: Order) -> None:

        if order.order_id in self.order_lookup:
            return ## this returns and stops dups from happening in the order book

        book = self.bids if order.side == Side.BID else self.asks ## picks buy or sell side

        if order.price not in book:
            book[order.price] = OrderedDict() ##if there is no price level exist, adds ordered dict

        book[order.price][order.order_id] = order ## adds order to price level

        self.order_lookup[order.order_id] = order## update flat dictioanary for 0(1)

    def _match(self, order: Order) -> list[Trade]:
        trades: list[Trade] = []

        match_book = self.asks if order.side == Side.BID else self.bids

        while order.remaining_quantity > 0 and len(match_book) > 0:

            if order.side == Side.BID:
                best_price, price_level = match_book.peekitem(0)
                if order.price < best_price:
                    break
            else:
                best_price, price_level = match_book.peekitem(-1)
                if order.price < best_price:
                    break










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
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()

        if best_bid is None or best_ask is None:
            return None

        return best_ask - best_bid

    def locate_order(self, order_id: int) -> Optional[Order]:
        # Use .get() so cancelling a non-existent order doesn't crash with a KeyError
        return self.order_lookup.get(order_id)

