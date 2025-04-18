# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import numpy as np
import pandas as pd
import cProfile

"""I have loaded all the necessary libraries"""

from google.colab import drive
drive.mount('/content/drive')

# Provide the file path in your Google Drive
file_path = '/content/drive/My Drive/clinics.xls'

df = pd.read_excel(file_path, engine='xlrd')
df

"""I have mounted the google drive and uploaded required file"""

print(df.head())

# Define the Haversine distance formula
def haversine(lat1, lon1, lat2, lon2):
    MILES = 3959  # Radius of Earth in miles
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return MILES * c
    return total_miles

"""I have defined Haversine distance formula between latitude and longitude by taking radius of earth in miles as 3959."""

#%% define a function to compute distance, using a for loop
# Define a function to manually loop over all rows and return a series of distances
def haversine_looping(df):
    distance_list = []
    for i in range(0, len(df)):
        d = haversine(40.671, -73.985, df.iloc[i]['locLat'], df.iloc[i]['locLong'])
        distance_list.append(d)
    return distance_list
cProfile.run("df['distance'] = haversine_looping(df)")

"""For loop has been applied and the execution time was found out. For loop generally takes long time because it iterates one by one row."""

haversine_series = []
for index, row in df.iterrows():
    haversine_series.append(haversine(40.671, -73.985, row['locLat'], row['locLong']))
#cProfile.run("df['distance'] = haversine_series")
df['distance'] = haversine_series

df['distance'] = df.apply(lambda row: haversine(40.671, -73.985, row['locLat'], row['locLong']), \
                          axis=1)

# Vectorized implementation of Haversine applied on Pandas series
df['distance'] = haversine(40.671, -73.985, df['locLat'], df['locLong'])

cProfile.run("df['distance'] = haversine(40.671, -73.985, df['locLat'], df['locLong'])")

"""Vectorized(pandas) is applied to compare with for loop. This relatively takes low time when compared to for loop. Vectorized implementation of Haversine is applied on pandas series."""

# Vectorized implementation of Haversine applied on NumPy arrays
df['distance'] = haversine(40.671, -73.985, df['locLat'].values, df['locLong'].values)

cProfile.run("df['distance'] = haversine(40.671, -73.985, df['locLat'].values, df['locLong'].values)")

"""Vectorized implementation of Haversine applied on NumPy arrays which is found to be faster even than vectorized pandas array."""

#Tabulation
results = {
    "Approach": ["For-loop (iterrows)", "Vectorized(Pandas)", "Vectorized (NumPy)"],
    "Execution Time (seconds)": [0.014, 0.004, 0.001]
}

# Create a DataFrame
df_results = pd.DataFrame(results)

# Display the table
print(df_results)

"""The results are tabulated, of which Vectorized(NumPy) found to be faster i.e., having less execution time."""