import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt  

data = pd.read_csv('bitcoin_data_preprocessed.csv')

print("Columns in data:", data.columns)

if '7-day MA' not in data.columns:
    data['7-day MA'] = data['Close'].rolling(window=7).mean()

if '30-day MA' not in data.columns:
    data['30-day MA'] = data['Close'].rolling(window=30).mean()

if 'Daily Return' not in data.columns:
    data['Daily Return'] = data['Close'].pct_change()

data = data.dropna(subset=['7-day MA', '30-day MA', 'Daily Return'])


X = data[['7-day MA', '30-day MA', 'Daily Return']]  
y = data['Close'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

predictions_df = pd.DataFrame({
    'Date': data['Date'].iloc[-len(y_test):], 
    'Actual Price': y_test,
    'Predicted Price': y_pred
})

predictions_df['Date'] = pd.to_datetime(predictions_df['Date'])

predictions_df.to_csv('predictions.csv', index=False)

print("Predictions saved to 'predictions.csv'")

plt.figure(figsize=(10, 6))
plt.plot(predictions_df['Date'], predictions_df['Actual Price'], label='Actual Price', color='blue')
plt.plot(predictions_df['Date'], predictions_df['Predicted Price'], label='Predicted Price', color='red')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Price: Actual vs Predicted')
plt.legend()

plt.xticks(rotation=45, ha='right')  

plt.tight_layout()

plt.show()
