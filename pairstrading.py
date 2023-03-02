import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for MSFT and AAPL
msft = yf.download("MSFT", start="2021-01-01", end="2023-02-27")
aapl = yf.download("AAPL", start="2021-01-01", end="2023-02-27")

# Calculate the difference between the closing prices of MSFT and AAPL
msft_appl_diff = msft['Close'] - aapl['Close']

# Plot the closing prices of MSFT, AAPL, and MSFT_APPL_DIFF
plt.plot(msft.index, msft['Close'], label='MSFT')
plt.plot(aapl.index, aapl['Close'], label='AAPL')
plt.plot(msft_appl_diff.index, msft_appl_diff, label='MSFT_APPL_DIFF')

# Customize the plot
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Historical Stock Prices for MSFT and AAPL')
plt.legend()

# Display the plot
plt.show()
