# py-stock-sl
Prices historical stock lots to determine after-tax valuation of a portfolio based on [short-term and long-term holding period](http://finance.zacks.com/considered-holding-longterm-stocks-1094.html) capital gains impact.

Assumes that the tax rate for a short sale is 28%, and for a long sale is 15%. This can be adjusted by changing

    shortRate = 0.28
    longRate = 0.15

Note:
-----
This is just for fun, please talk to your accountant and verify the numbers before making any assumptions based on the calculations (and if you find ways to improve the accuracy, please share!)

Requires
--------
Developed using: `Python3`

Users need to have an API key from [Alpha Vantage](http://www.alphavantage.co) which is inserted into the `personalParams.py` file

    apikey = "1234"

`personalParams.py` file also needs the stock positions:

    st = [
          ["AMZN",[
           [10,305.17,"01-01-2014"],
           [20,352.50,"01-01-2015"]]
          ],
          ["TMUS",
           [[10, 43.92,"06-13-2016"]]
          ]
         ]

The format of `st` is the ticker, followed by a group listing the number of shares, the purchase price and the purchase date (in the format dd-mm-yyyy)

---

To-Do
-----

- Resiliance: make code more able to handle errors
- Customize: allow user to enter (and store) tax rates and stock lots
  - will this be a web page that stores data in local storage, or server stored (with login requirement)?
  - possibly expose the code as an endpoint to return results based on passing parameters


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