# data_preprocessing.py

import pandas as pd
import numpy as np
import datetime

def load_data(file_path):
    return pd.read_csv(file_path, sep=";", decimal=",")

def drop_columns(data):
    return data.drop(['Unnamed: 15', 'Unnamed: 16'], axis=1, inplace=True, errors='ignore')

def replace_missing_values(data):
    return data.replace(to_replace=-200, value=np.nan, inplace=True)

def convert_datetime(data):
    data['DateTime'] = (data['Date']) + ' ' + (data['Time'])
    data['DateTime'] = data['DateTime'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H.%M.%S'))
    data['Weekday'] = data['DateTime'].dt.day_name()
    data['Month'] = data['DateTime'].dt.month_name()
    data['Hour'] = data['DateTime'].dt.hour
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    data.drop('Time', axis=1, inplace=True, errors='ignore')
    return data[['Date', 'Month', 'Weekday', 'DateTime', 'Hour', 'CO(GT)', 'PT08.S1(CO)', 'C6H6(GT)', 'PT08.S2(NMHC)',
                 'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)', 'T', 'RH', 'AH']]
