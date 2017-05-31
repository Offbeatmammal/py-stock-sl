# py-stock-sl
Prices Short/Long stock positions to determine after tax valuation

Requires users to have an API key from [Alpha Vantage](http://www.alphavantage.co) which is inserted into the personalParams.py file

    apikey = "1234"

personalParams.py file also needs the stock positions:

    st = [["AMZN",[
           [16,305.17,"01-01-2014"],
           [50,352.50,"01-01-2015"]]
          ],
          ["TMUS",
           [[1, 43.92,"06-13-2016"]]]
          ]
