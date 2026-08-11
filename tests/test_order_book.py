from lob.order import Order, Side
from lob.order_book import LimitOrderBook


def test_spread_is_never_negative():
    book = LimitOrderBook()
    book.add_limit_order(Order(order_id=1, side=Side.BUY, price=101.0, quantity=10, ...))
    book.add_limit_order(Order(order_id=2, side=Side.SELL, price=100.0, quantity=10, ...))

    # assert the spread is not negative