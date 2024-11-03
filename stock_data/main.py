import pandas_datareader.data as pdr
import datetime as dt
import mplfinance as mpf


def get_stock_data(code):
  df = pdr.DataReader("{}.JP".format(code), "stooq").sort_index()
  return df

df = pdr.DataReader("9434.JP", "stooq")
print(df)

# 東電9501
df_9501 = get_stock_data(9501)

df_9501["ma5"] = df_9501["Close"].rolling(window=5).mean()
df_9501["ma25"] = df_9501["Close"].rolling(window=25).mean()
df_9501["ma75"] = df_9501["Close"].rolling(window=75).mean()


cdf = df_9501[dt.datetime(2023, 1, 1):dt.datetime(2023, 12, 31)]
apd = [
  mpf.make_addplot(cdf["ma5"], color="blue"),
  mpf.make_addplot(cdf["ma25"], color="green"),
  mpf.make_addplot(cdf["ma75"], color="red")
  ]

mpf.plot(cdf, type="candle", figratio=(16,9), addplot=apd)
# mpf.plot(cdf, type="candle", figratio=(16,9), volume=True, mav=(5, 25, 75), style="nightclouds")

