# Pairs Trading Project
 pip install yfinance
pip install matplotlib

import yfinance as yf
import matplotlib.pyplot as plt

# Download data for MSFT and AAPL
msft = yf.Ticker("MSFT")
aapl = yf.Ticker("AAPL")

msft_data = msft.history(period="max")
aapl_data = aapl.history(period="max")

# Plot the data
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(msft_data.index, msft_data["Close"], label="MSFT")
ax.plot(aapl_data.index, aapl_data["Close"], label="AAPL")

ax.set_xlabel("Year")
ax.set_ylabel("Stock Price ($)")
ax.set_title("Microsoft vs. Apple Stock Price")

ax.legend()

plt.show()
