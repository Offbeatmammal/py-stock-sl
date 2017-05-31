# py-stock-sl
Prices Short/Long stock positions to determine after tax valuation

Requires users to have an API key from [Alpha Vantage](http://www.alphavantage.co) which is inserted into the `personalParams.py` file

    apikey = "1234"

`personalParams.py` file also needs the stock positions:

    st = [["AMZN",[
           [16,305.17,"01-01-2014"],
           [50,352.50,"01-01-2015"]]
          ],
          ["TMUS",
           [[1, 43.92,"06-13-2016"]]]
          ]

The format of `st` is the ticker, followed by a group listing the number of shares, the purchase price and the purchase date (in the format dd-mm-yyyy)

---

If you make use of this and like it and want to give something back... [I wrote a book!](http://amzn.to/1SHjbLI) :)

Contribute
----------
This project can be forked from
[Github](https://github.com/Offbeatmammal/py-stock-sl). Please issue pull
requests from feature branches.

License
-------
See Licence file in repo, or refer to http://unlicense.org