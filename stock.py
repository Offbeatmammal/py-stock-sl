import requests
from urllib.error import URLError, HTTPError
import json, os
from datetime import datetime
import sys

# Note: you will need to create a 'personalParams.py' file
#       and populate it with the 'apikey' variable and 'st' JSON
#       as described in the README.md
from personalParams import *

shortRate = 0.28
longRate = 0.15

# disable SSL warnings. Not really recommended but sometimes AlphaVantage throws them
requests.packages.urllib3.disable_warnings()

def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt 

def getStock(ticker,apikey):
    req = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker + "&outputSize=compact&apikey=" + apikey, verify=False)
    try:
        response = req
    except HTTPError as e:
        # do something
        data = 'Error code: ' + e.code
        sys.exit(data)
    except URLError as e:
        # do something
        data = 'Reason: ' + str(e.reason)
        sys.exit(data)
    else:
        # do the good thing
        data = json.loads(response.text)
    return (data)

for ws in st:
    data = getStock(ws[0], apikey)
    sy = data["Realtime Global Securities Quote"]["01. Symbol"]

    dt = data["Realtime Global Securities Quote"]["11. Last Updated"]
    latest = data["Realtime Global Securities Quote"]
    
    try:
        dthr = dt.split(' ')[1].split(":")[0]
    except Exception:
        dthr = "16"

    open = round(float(latest["04. Open (Current Trading Day)"]) * 100) / 100
    high = round(float(latest["05. High (Current Trading Day)"]) * 100) / 100
    close = round(float(latest["03. Latest Price"]) * 100) / 100

    tot = 0
    costShort = 0
    costLong = 0
    numShort = 0
    numLong = 0

    cdt = subtract_years(datetime.now(),1).date()
    for x in ws[1]:
        tot += x[0]
        if datetime.strptime(x[2], '%m-%d-%Y').date() > cdt:
            costShort += x[0] * x[1]
            numShort += x[0]
        else:
            costLong += x[0] * x[1]
            numLong += x[0]

    vpre =  close * tot

    valShort = ((numShort * close) - costShort) * shortRate
    valLong = ((numLong * close) - costLong) * longRate

    vpost = "$" + str(round((vpre - (valShort + valLong))*100)/100)
    vpre = "$" + str(round(vpre*100)/100)

    print(sy + " (" + str(close) + "): Pre:"+ vpre + ", Post:"+vpost)
  