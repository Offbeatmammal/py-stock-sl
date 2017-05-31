import urllib.request, json, os
from datetime import datetime

from personalParams import *

shortRate = 0.28
longRate = 0.15

def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt 

def getStock(ticker,apikey):
    with urllib.request.urlopen("http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputSize=compact&apikey=" + apikey) as url:
        data = json.load(url)
    return (data)

for ws in st:
    data = getStock(ws[0], apikey)
    sy = data["Meta Data"]["2. Symbol"]

    dt = data["Meta Data"]["3. Last Refreshed"]
    latest = data["Time Series (Daily)"][dt]
    
    try:
        dthr = dt.split(' ')[1].split(":")[0]
    except Exception:
        dthr = "16"

    open = round(float(latest["1. open"]) * 100) / 100
    high = round(float(latest["2. high"]) * 100) / 100
    close = round(float(latest["4. close"]) * 100) / 100

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
  