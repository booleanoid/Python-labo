import pandas_datareader.data as pdr
import datetime as dt
from matplotlib import pyplot as plt
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

# mpf.plot(cdf, type="candle", figratio=(16,9), addplot=apd)

# 描写情報を追加
fig, axes = mpf.plot(cdf, type="candle", figratio=(16, 9), addplot=apd, returnfig=True, volume=True)
axes[0].legend(["MA5", "MA25", "MA75"])
# fig.show()
plt.show()
