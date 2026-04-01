# mettre en place la stratégie de la tortue pour savoir si on doit acheter ou vendre une action
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bitcoin = pd.read_csv('./dataset/bitcoin.csv', index_col = 'Date', parse_dates = True)
print(bitcoin['Close'].shape)
print(bitcoin.head())

bitcoin['Max'] = bitcoin['Close'].rolling(window = 28).max()
bitcoin['Min'] = bitcoin['Close'].rolling(window = 28).min()

bitcoin['Buy'] = np.zeros(bitcoin.shape[0])
bitcoin['Sell'] = np.zeros(bitcoin.shape[0])

bitcoin.loc[bitcoin['Close'] > bitcoin['Max'].shift(1), 'Buy'] = 1
bitcoin.loc[bitcoin['Close'] < bitcoin['Min'].shift(1), 'Sell'] = -1

#on supprime les lignes où il n'y a pas de signal d'achat ou de vente
bitcoin = bitcoin[(bitcoin['Buy'] != 0) | (bitcoin['Sell'] != 0)]

print(bitcoin.head(30))

plt.figure(figsize=(12,6))
bitcoin['Close'].plot(label = 'Bitcoin')
plt.plot(bitcoin.index, bitcoin['Buy']*bitcoin['Close'], color = 'green', label = 'Buy')
plt.plot(bitcoin.index, -bitcoin['Sell']*bitcoin['Close'], color = 'red', label = 'Sell')

plt.show()