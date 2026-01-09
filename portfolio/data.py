def create_portfolio(name: str) -> dict:
    return {
        "name": name,
        "assets": [
            make_asset("AAPL", "262.98", 100),
            make_asset("IBM", 300.06, 500),
            make_asset("CNQ", 31.53, 5000),
            make_asset("HOG", 21.05, 4000),
            make_asset("ZM", 86.32, 300)
        ]
    }