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
cdf = df_9501.tail(100)
mpf.plot(cdf, type="candle", figratio=(16,9), volume=True, style="nightclouds")
