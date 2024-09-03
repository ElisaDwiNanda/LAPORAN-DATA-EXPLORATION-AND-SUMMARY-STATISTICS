import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import Dataset
df = pd.read_csv('heart_disease_uci.csv')

# 2. Eksplorasi Awal
## Menampilkan 5 baris pertama
print("5 Baris Pertama:")
print(df.head())

## Menampilkan 5 baris terakhir
print("\n5 Baris Terakhir:")
print(df.tail())

## Menampilkan informasi dataset
print("\nInformasi Dataset:")
print(df.info())

## Menampilkan statistik deskripsi dasar
print("\nStatistik Deskriptif Dasar:")
print(df.describe())

## Menampilkan jumlah nilai missing per kolom
print("\nJumlah Nilai Missing per Kolom:")
print(df.isnull().sum())

# 3. Identifikasi Outliers menggunakan Box Plot
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

plt.figure(figsize=(15,10))
for i, column in enumerate(numeric_cols, 1):
    plt.subplot(4, 4, i)
    sns.boxplot(y=df[column])
    plt.title(f'Box Plot of {column}')
plt.tight_layout()
plt.show()

# 4. Statistik Deskriptif
## Mean
print("\nMean:")
print(df.mean())

## Median
print("\nMedian:")
print(df.median())

## Mode
print("\nMode:")
print(df.mode().iloc[0])

## Standar Deviasi
print("\nStandard Deviation:")
print(df.std())

## Variansi
print("\nVariance:")
print(df.var())

## Skewness dan Kurtosis
print("\nSkewness:")
print(df.skew())

print("\nKurtosis:")
print(df.kurtosis())

# 5. Korelasi Antar Variabel
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 6. Visualisasi Data


# Membuat histogram untuk setiap variabel numerik
df.hist(bins=15, figsize=(15,10), layout=(4,4))
plt.suptitle('Histogram Variabel Numerik')
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Untuk menghindari overlap judul
plt.show()


## Scatter Plot untuk pasangan variabel dengan korelasi tinggi
threshold = 0.5
high_corr = correlation_matrix.abs() > threshold
high_corr = high_corr.where(np.triu(np.ones(high_corr.shape), k=1).astype(bool))
pairs = high_corr.stack().index.tolist()

for pair in pairs:
    sns.scatterplot(x=pair[0], y=pair[1], data=df, hue='target')
    plt.title(f'Scatter Plot of {pair[0]} vs {pair[1]}')
    plt.show()

# Misalkan 'age' dan 'chol' memiliki korelasi tinggi
sns.scatterplot(x='age', y='chol', data=df, hue='target')
plt.title('Scatter Plot of Age vs Cholesterol')
plt.show()

# Menentukan threshold korelasi
threshold = 0.5

# Mengambil pasangan variabel dengan korelasi tinggi
high_corr = correlation_matrix.abs() > threshold
high_corr = high_corr.where(np.triu(np.ones(high_corr.shape), k=1).astype(bool))
pairs = high_corr.stack().index.tolist()

# Membuat scatter plot untuk setiap pasangan
for pair in pairs:
    sns.scatterplot(x=pair[0], y=pair[1], data=df, hue='target')
    plt.title(f'Scatter Plot of {pair[0]} vs {pair[1]}')
    plt.show()

for column in numeric_cols:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\nOutliers for {column}:")
    print(outliers.shape[0])
