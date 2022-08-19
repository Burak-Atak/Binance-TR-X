### Binance-TR-X

* Firstly clone the project after this, you should install the dependencies with this terminal code.

```bash
pip install -r requirements.txt
```


```py
# Get Klines from Binance
datas = GetKlines.get_klines('BTCUSDT', '1d', 300)

# Convert to numpy array for desired price type
close_prices = Helper.prepare_price_for_indicators(datas, 'close')

# Calculate trix
trix = Indicator.trix(np.array(close_prices))

# Print trix
print(trix)
```