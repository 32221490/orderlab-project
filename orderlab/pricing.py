def subtotal(unit_price: int, quantitiy: int) -> int:
    if unit_price < 0 or quantitiy < 0:
        raise ValueError("negative input")
    return unit_price * quantitiy