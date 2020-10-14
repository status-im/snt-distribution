import pandas as pd
import numpy as np

snt_stats = {
    'total_supply': 6804870174.8781,   
}

def lower(string):
    return string.lower()

def label_exp_group(value):
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    for label in labels:
        if value <= 10**float(label):
            return label

# import known Status Addresses
status = pd.read_csv('./data_csv/utility.csv')
status['address'] = status['address'].apply(lower)
status['isStatus'] = True

# import holder accounts
holders = pd.read_csv('./data_csv/holders.csv')
holders['address'] = holders['address'].apply(lower)

# import exchange accounts
exchanges = pd.read_csv('./data_csv/exchanges.csv')
exchanges['address'] = exchanges['address'].apply(lower)
exchanges['isExchange'] = True

# merge into single dataset
holders = holders.merge(status, on="address", how="left")
holders = holders.merge(exchanges, on="address", how="left")

# clean up
holders['name_x'].fillna('', inplace=True)
holders['name_y'].fillna('', inplace=True)
holders['name'] = holders['name_x'] + holders['name_y']

# add additional columns
holders['percent'] = holders['balance'] / snt_stats['total_supply'] * 100
holders['exp_group'] = holders.balance.apply(label_exp_group)

# clean up NaN
holders['isContract'].fillna('False', inplace=True)
holders['isExchange'].fillna('False', inplace=True)
holders['isStatus'].fillna('False', inplace=True)

# filter out what we want
holders = holders[['address', 'balance', 'percent', 'exp_group', 'name', 'isContract', 'isExchange', 'isStatus']]

holders.to_csv('./data_csv/holders_munged.csv')