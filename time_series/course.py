import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bitcoin = pd.read_csv('./dataset/bitcoin.csv', index_col = 'Date', parse_dates = True) 
ethereum = pd.read_csv('./dataset/eth.csv', index_col = 'Date', parse_dates = True)
bitcoin_eth = pd.merge(bitcoin, ethereum, how = 'inner', left_index = True, right_index = True, suffixes = ('_bitcoin', '_ethereum'))

m = bitcoin_eth['Close_bitcoin'].resample('W').agg(['mean', 'std', 'min', 'max']) # resample('W') pour faire une moyenne hebdomadaire du cours du Bitcoin, agg(['mean', 'std', 'min', 'max']) pour calculer la moyenne, l'écart type, le minimum et le maximum du cours du Bitcoin
# on obtient 4 colonnes : mean, std, min et max
print(m.head())

rolling = bitcoin_eth['Close_bitcoin'].rolling(window = 30).mean() # rolling(window = 30) pour faire une moyenne mobile sur 30 jours du cours du Bitcoin
print(rolling.head())

# moyenne mobile exponentielle
exp_rolling = bitcoin_eth['Close_bitcoin'].ewm(alpha=0.3).mean() # ewm(alpha=0.3) pour faire une moyenne mobile exponentielle sur 30 jours du cours du Bitcoin
print(exp_rolling.head())

plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
bitcoin_eth['Close_bitcoin'].resample('W').mean().plot(label = 'Bitcoin') # resample('W') pour faire une moyenne hebdomadaire du cours du Bitcoin
plt.subplot(2,1,2)
bitcoin_eth['Close_ethereum'].resample('W').mean().plot(label = 'Ethereum')

correlation = bitcoin_eth['Close_bitcoin'].corr(bitcoin_eth['Close_ethereum'])
print(f'La corrélation entre le cours du Bitcoin et de l\'Ethereum est de {correlation:.2f}')

#bitcoin.loc['2017':'2020']['Close'].plot()
#bitcoin.loc['2017':'2020']['Close'].resample('W').mean().plot()
#plt.show() # affichage du graphique