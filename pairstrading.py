import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download historical data for MSFT and AAPL
msft = yf.download("MSFT", start="2021-01-01", end="2023-02-27")
aapl = yf.download("AAPL", start="2021-01-01", end="2023-02-27")

# Calculate the difference between the closing prices of MSFT and AAPL
msft_appl_diff = msft['Close'] - aapl['Close']

# Calculate the Bollinger Bands for MSFT_APPL_DIFF
window_size = 20
num_std = 2
rolling_mean = msft_appl_diff.rolling(window=window_size).mean()
rolling_std = msft_appl_diff.rolling(window=window_size).std()
upper_band = rolling_mean + (rolling_std * num_std)
lower_band = rolling_mean - (rolling_std * num_std)

# Create a new dataframe to hold the trade signals
signals = pd.DataFrame(index=msft_appl_diff.index)
signals['signal'] = 0.0

# Set the buy signal to 1 when MSFT_APPL_DIFF crosses below the lower Bollinger Band
signals['signal'][window_size:] = \
    ((msft_appl_diff[window_size:] < lower_band[window_size:]) * 1.0)

# Set the sell signal to -1 when MSFT_APPL_DIFF crosses above the upper Bollinger Band
signals['signal'][window_size:] = \
    ((msft_appl_diff[window_size:] > upper_band[window_size:]) * -1.0)

# Take the cumulative sum of the trade signals to get the position (long or short)
signals['position'] = signals['signal'].cumsum()

# Plot the closing prices of MSFT, AAPL, and MSFT_APPL_DIFF with Bollinger Bands and trade signals
fig, ax = plt.subplots(figsize=(12,8))

ax.plot(msft.index, msft['Close'], label='MSFT')
ax.plot(aapl.index, aapl['Close'], label='AAPL')
ax.plot(msft_appl_diff.index, msft_appl_diff, label='MSFT_APPL_DIFF')
ax.plot(rolling_mean.index, rolling_mean, label='Rolling Mean')
ax.fill_between(rolling_mean.index, upper_band, lower_band, color='gray', alpha=0.2)
ax.plot(signals.loc[signals['signal'] == 1.0].index,
        msft_appl_diff[signals['signal'] == 1.0],
        marker='^', markersize=10, color='green', label='Buy')
ax.plot(signals.loc[signals['signal'] == -1.0].index,
        msft_appl_diff[signals['signal'] == -1.0],
        marker='v', markersize=10, color='red', label='Sell')

# Customize the plot
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('Historical Stock Prices for MSFT and AAPL with Bollinger Bands and Trade Signals')
ax.legend()

# Display the plot
plt.show()
