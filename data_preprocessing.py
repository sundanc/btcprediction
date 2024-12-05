import pandas as pd

data = pd.read_csv('bitcoin_data.csv', skiprows=2) 

data.columns = ['Date', 'Open', 'Adj Close', 'Close', 'High', 'Low', 'Volume']

data['Date'] = pd.to_datetime(data['Date'])

data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

print(data.head())

data.to_csv('bitcoin_data_preprocessed.csv', index=False)

print("Preprocessed data has been saved to 'bitcoin_data_preprocessed.csv'")
