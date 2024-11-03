import pandas_datareader.data as pdr
import datetime as dt
import mplfinance as mpf


def get_stock_data(code):
  df = pdr.DataReader("{}.JP".format(code), "stooq").sort_index()
  return df

df = pdr.DataReader("9434.JP", "stooq")
print(df)
