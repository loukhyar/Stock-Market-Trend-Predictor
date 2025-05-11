# 📈 Stock Market Trend Predictor

Stock Market Trend Predictor is a beginner-friendly machine learning project that leverages real-time financial data to forecast future stock prices. By using historical market data from Yahoo Finance, this tool visualizes trends and applies a linear regression model to predict stock prices five days into the future. It's a great starting point for anyone interested in financial analytics, data science, or algorithmic trading.

## 🔧 Features

* Downloads stock data (Tesla: TSLA) from Yahoo Finance using `yfinance`.
* Visualizes closing prices over time.
* Predicts future closing prices (5 days ahead) using a linear regression model.
* Evaluates prediction performance using MAE and RMSE metrics.

## 🛠️ Requirements

Install the necessary Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn yfinance
```

## 📊 Data Source

* Data is fetched from Yahoo Finance for **Tesla (TSLA)** between `2018-01-01` and `2025-01-01`.

## 🚀 How It Works

1. **Fetch Data**
   Uses `yfinance` to download TSLA stock prices.

2. **Visualize**
   Plots the closing prices using `matplotlib`.

3. **Preprocess**
   Creates a new column for the price 5 days into the future and prepares the data.

4. **Model Training**
   Trains a linear regression model on historical closing prices.

5. **Evaluate**
   Outputs:

   * Mean Absolute Error (MAE)
   * Root Mean Squared Error (RMSE)

## 📷 Example Plot

![image](https://github.com/user-attachments/assets/3645c395-a4e4-4abb-a63f-0a849f7efd4d)


## 📁 Project Structure

```
├── predictor.py           # Python script implementing the predictor
├── README.md              # This file
```
