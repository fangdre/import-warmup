from .metrics import calculate_asset_value

def make_asset(ticker: str, price: float, quantity: int) -> dict:
    return {
        "ticker": ticker,
        "price": price,
        "quantity": quantity
    }

def get_asset_value(asset: dict) -> float:
    return calculate_asset_value(asset)