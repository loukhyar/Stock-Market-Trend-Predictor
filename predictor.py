# predictor.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Download Tesla stock data
print("Downloading TSLA stock data...")
stock = yf.download('TSLA', start='2018-01-01', end='2025-01-01')

# Display first few rows
print("\nSample data:")
print(stock.head())

# Plot closing prices
plt.figure(figsize=(10, 5))
plt.plot(stock['Close'], label="Closing Price")
plt.title("Tesla Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Create a new column for future prices (next 5 days)
stock['Future Price'] = stock['Close'].shift(-5)

# Drop rows with NaN values
stock.dropna(inplace=True)

# Define features (X) and target (y)
X = stock[['Close']]
y = stock['Future Price']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future prices
predicted_prices = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predicted_prices)
rmse = np.sqrt(mean_squared_error(y_test, predicted_prices))

print(f"\nEvaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
