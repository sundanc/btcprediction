import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bitcoin_data_preprocessed.csv')

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Close Price', color='b')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Close Price Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.show()

print(data.isnull().sum())  

print(data.describe())  
