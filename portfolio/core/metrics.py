def calculate_portfolio_value(portfolio: dict) -> float:
    total = 0
    for asset in portfolio["assets"]:
        total += calculate_asset_value(asset)
    return total

def calculate_asset_value(asset: dict) -> float:
    return asset["price"] * asset["quantity"]