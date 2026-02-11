import portfolio

if __name__ == "__main__":
    my_portfolio = portfolio.data.create_portfolio("Retirement")
    portfolio.report.print_report(my_portfolio)