# Just for testing purposes!
# My second change.
#print("hello project")

import yfinance as yf
import matplotlib.pyplot as plt
# Get the data for the stock AAPL



def get_info_on_stock(ticker):
    stock = yf.Ticker(ticker)

    # Get overview of company
    print(stock.info)

    # Get historical closing price data
    hist = stock.history(period="max")["Close"]
    print(hist.head())

    # Get financial data
    print(stock.financials)

    # Get major share holders
    print(stock.major_holders)

    # Get institutional holders
    print(stock.institutional_holders)

    # Get balance sheet
    print(stock.balance_sheet)

    # Show cashflow
    print(stock.cashflow)

    # Show earnings
    print(stock.earnings)

    # Show analysts recommendations
    print(stock.recommendations)

data = yf.download('TRY=X','2021-01-01','2021-12-01')
# Import the plotting library

# Plot the close price of the AAPL
data['Adj Close'].plot()

plt.show()

get_info_on_stock("GARAN.IS")






