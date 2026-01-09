def make_asset(ticker: str, price: float, quantity: int) -> dict:
    return {
        "ticker": ticker,
        "price": price,
        "quantity": quantity
    }