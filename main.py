import numpy as np
from helper import Helper

from get_data import GetKlines
from indikator import Indicator

# Get Klines from Binance
datas = GetKlines.get_klines('BTCUSDT', '1d', 300)

# Convert to numpy array for desired price type
close_prices = Helper.prepare_price_for_indicators(datas, 'close')

# Calculate trix
trix = Indicator.trix(np.array(close_prices))

# Print trix
print(trix)
