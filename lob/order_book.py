from collections import OrderedDict
from sortedcontainers import SortedDict
from lob.order import Order, Side, OrderType


class LimitOrderBook:

    def __init__(self):
        self.bids = SortedDict()
        self.asks = SortedDict()
        self.order_lookup = {} # flat cancel lookup

    def get_bestBid(self):
        maxBid = self.bids.peekitem(-1)
        return maxBid

    def get_bestAsk(self):
        maxAsk = self.asks.peekitem(-1)
        return maxAsk
    
    def get_order_book(self, order_id):
        return self.order_lookup[order_id]

    def get_bid(self, order_id):
        return self.bids[order_id]


