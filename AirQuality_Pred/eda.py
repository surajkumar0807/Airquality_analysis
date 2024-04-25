# eda.py

import pandas as pd

def remove_outliers(data):
    Q1 = data.quantile(0.25)  # First quartile
    Q3 = data.quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range

    scale = 1.4  # Modify this value to adjust outlier detection sensitivity
    lower_lim = Q1 - scale * IQR
    upper_lim = Q3 + scale * IQR

    cols = data.columns[5:]  # Look for outliers in columns starting from index 5

    # Mask to remove rows that have values above/below IQR limits
    condition = ~((data[cols] < lower_lim) | (data[cols] > upper_lim)).any(axis=1)

    # Generate new dataframe that has had its outliers removed
    filtered_data = data[condition]
    
    return filtered_data
