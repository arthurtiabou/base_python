import pandas as pd


bitcoin = pd.read_csv('./dataset/bitcoin.csv', index_col = 'Date', parse_dates = True) # lecture d'un fichier CSV contenant des données sur le prix du bitcoin
print(bitcoin.head()) # affichage des 5 premières lignes du DataFrame