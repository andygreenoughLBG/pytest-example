from pay.order import LineItem, Order


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_one_line_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 100


def test_multi_line_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    order.line_items.append(LineItem(name="Test2", price=200))
    assert order.total == 300
