import pandas as pd

df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
print(df_csv.dtypes)

df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq.dtypes)

import os

csv_size = os.path.getsize('example-data/2025-01-01.taxi-rides.csv')
pq_size  = os.path.getsize('example-data/2025-01-01.taxi-rides.parquet')

print(f'CSV:     {csv_size / 1024 / 1024:.1f} MB')
print(f'Parquet: {pq_size  / 1024 / 1024:.1f} MB')
print(f'Parquet is {csv_size / pq_size:.1f}x smaller')

import time

t = time.time()
pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.3f}s')
print(f'Parquet: {pq_time:.3f}s')