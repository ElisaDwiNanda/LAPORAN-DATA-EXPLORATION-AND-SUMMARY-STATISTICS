# LAPORAN-DATA-EXPLORATION-AND-SUMMARY-STATISTICS
## Pendahuluan
### 1. Latar Belakang
Penyakit jantung koroner (PJK) adalah salah satu penyebab utama kematian di seluruh dunia. Dengan meningkatnya prevalensi dan dampak serius dari penyakit ini, penting untuk memiliki pemahaman yang mendalam tentang faktor-faktor yang mempengaruhi risiko terkena penyakit jantung. Data kesehatan yang tersedia dapat menyediakan wawasan berharga yang dapat membantu dalam pencegahan dan pengelolaan penyakit ini. Analisis data kesehatan menggunakan teknik statistik dan visualisasi data dapat mengungkapkan pola dan hubungan yang mungkin tidak terlihat secara langsung.
Pada tugas ini, kami melakukan eksplorasi data dan menghitung berbagai statistik deskriptif untuk dataset Heart Disease UCI. Tujuan dari analisis ini adalah untuk memahami karakteristik dataset, mengidentifikasi pola, outliers, missing values, dan hubungan antar variabel. Analisis dilakukan menggunakan Python dengan library Pandas, NumPy, dan Matplotlib/Seaborn.
### 2. Deskripsi Dataset
Dataset yang digunakan dalam laporan ini adalah Heart Disease UCI Dataset, yang diperoleh dari Kaggle. Dataset ini berisi informasi medis tentang pasien yang telah didiagnosis dengan penyakit jantung, termasuk berbagai variabel yang dapat mempengaruhi risiko penyakit. Variabel-variabel ini meliputi:
- Usia (age): Usia pasien.
- Jenis Kelamin (sex): Jenis kelamin pasien (1 = pria, 0 = wanita).
- Jenis Nyeri Dada (cp): Klasifikasi nyeri dada berdasarkan karakteristik (0-3).
- Tekanan Darah (trestbps): Tekanan darah sistolik pada saat istirahat.
- Kolesterol (chol): Level kolesterol serum.
- Gula Darah (fbs): Status gula darah puasa (1 = lebih dari 120 mg/dl, 0 = kurang dari 120 mg/dl).
- Hasil Elektrokardiografi (restecg): Hasil elektrokardiogram pada saat istirahat (0-2).
- Detak Jantung Maksimum (thalach): Detak jantung maksimum selama uji stres.
- Eksersais Angina (exang): Apakah terjadi angina selama latihan (1 = ya, 0 = tidak).
- Depresi ST Segment (oldpeak): Depresi ST segment selama uji stres dibandingkan dengan saat istirahat.
- Kemiringan ST Segment (slope): Kemiringan ST segment pada puncak uji stres (0-2).
- Jumlah Vaskularisasi (ca): Jumlah pembuluh darah yang terlihat pada fluoroskopi (0-3).
- Thalassemia (thal): Status thalassemia (0-3).
- Target: Apakah pasien menderita penyakit jantung (1 = ya, 0 = tidak).
### 3. Tujuan Analisis
Tujuan dari analisis ini adalah untuk mengeksplorasi dan memahami dataset Heart Disease UCI secara mendalam dengan menggunakan berbagai teknik statistik dan visualisasi data. Analisis ini mencakup:
- Pemahaman Struktur Dataset: Mengimpor dan memeriksa struktur dataset untuk menentukan tipe data, jumlah entri, serta identifikasi nilai yang hilang.
- Statistik Deskriptif: Menghitung statistik deskriptif seperti mean, median, mode, standar deviasi, variansi, skewness, dan kurtosis untuk setiap kolom numerik. Statistik ini penting untuk memahami distribusi dan variasi data.
- Eksplorasi Data Awal: Mengidentifikasi pola, outliers, dan missing values. Eksplorasi ini meliputi analisis distribusi data dan penanganan outliers serta nilai yang hilang.
- Visualisasi Data: Membuat visualisasi seperti histogram, box plot, dan scatter plot untuk menggambarkan distribusi dan hubungan antar variabel. Visualisasi ini membantu dalam mengidentifikasi pola dan korelasi antar variabel.
- Penyusunan Laporan: Menyusun laporan yang menjelaskan temuan dari eksplorasi data, termasuk analisis distribusi, identifikasi korelasi kuat antar variabel, dan penanganan outliers serta missing values.
### 4. Metodologi
Analisis ini dilakukan menggunakan Python, dengan memanfaatkan library analisis data seperti Pandas untuk manipulasi data, NumPy untuk perhitungan statistik, dan Matplotlib serta Seaborn untuk visualisasi data. Proses analisis dimulai dengan memuat dataset dan melakukan eksplorasi awal, diikuti dengan perhitungan statistik deskriptif dan identifikasi outliers. Visualisasi data kemudian digunakan untuk memperjelas pola dan hubungan antar variabel. Laporan akhir akan merangkum temuan utama dari analisis ini, memberikan wawasan yang berguna untuk penelitian lebih lanjut dan pengambilan keputusan terkait penyakit jantung.
## Pembahasan
#### Eksplorasi Awal
Eksplorasi awal adalah langkah penting dalam analisis data yang bertujuan untuk memahami struktur dan kualitas data sebelum melakukan analisis lebih lanjut. Dalam bagian ini, kami akan melakukan beberapa langkah utama untuk mengeksplorasi dataset Heart Disease UCI, termasuk menampilkan baris pertama dan terakhir dari dataset, memeriksa informasi dataset, dan mengevaluasi statistik deskriptif dasar serta nilai yang hilang.
##### 1. Import Library
import pandas as pd<br/>
import numpy as np<br/>
import matplotlib.pyplot as plt<br/>
import seaborn as sns<br/>

- Pandas (pd): Untuk manipulasi dan analisis data dalam bentuk tabel (DataFrames).
- NumPy (np): Untuk operasi matematika dan array numerik.
- Matplotlib (plt): Untuk membuat visualisasi data seperti grafik dan plot.
- Seaborn (sns): Untuk visualisasi statistik yang lebih estetis dan informatif, dibangun di atas Matplotlib.
##### 2. Import Dataset
fileLocation = r"C:\Data Mining\heart_disease_uci.csv" <br/>
df = pd.read_csv(fileLocation)<br/>

- fileLocation: Menyimpan lokasi file dataset dalam bentuk string. Dengan menggunakan r di awal string, path dianggap sebagai raw string sehingga karakter khusus seperti backslash tidak akan di-escape.
- df = pd.read_csv(fileLocation): Membaca file CSV yang ada di fileLocation dan menyimpannya dalam variabel df sebagai DataFrame.
##### 3. Menampilkan 5 Baris Pertama dan Terakhir
Menampilkan baris pertama dan terakhir dari dataset membantu kita memahami struktur data dan memeriksa apakah data sudah sesuai dengan yang diharapkan.<br/>

print("5 Baris Pertama:")<br/>
print(df.head())<br/>


print("\n5 Baris Terakhir:")<br/>
print(df.tail())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/71969ccb-f432-4bd7-8f08-c5d3f7e23d66)
##### 4. Menampilkan Informasi Dataset
Menampilkan informasi umum tentang dataset, seperti jumlah baris, kolom, tipe data, dan jumlah nilai non-missing di setiap kolom.<br/>

print("\nInformasi Dataset:")<br/>
print(df.info())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/a3175e71-ea63-45d0-8221-0ecdf5d415db)
Informasi ini memberikan gambaran tentang jumlah entri dalam dataset serta tipe data setiap kolom. Kita juga dapat memeriksa apakah ada nilai yang hilang.

##### 5. Menampilkan Statistik Deskriptif Dasar
Statistik deskriptif memberikan informasi ringkas tentang distribusi dan variasi data dalam setiap kolom numerik.<br/>

print("\nStatistik Deskriptif Dasar:")<br/>
print(df.describe())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/17d80c74-cfb4-4323-a977-3e2ffeb993b3)
Statistik deskriptif dasar ini mencakup rata-rata (mean), median, modus (mode), standar deviasi, dan rentang untuk setiap kolom numerik. Ini membantu dalam memahami distribusi data dan variasi antar variabel.

##### 6. Mengevaluasi Nilai yang Hilang
Nilai yang hilang atau missing values dapat mempengaruhi analisis data. Oleh karena itu, penting untuk memeriksa apakah ada nilai yang hilang dalam dataset.<br/>

print("\nJumlah Nilai Missing per Kolom:")<br/>
print(df.isnull().sum())<br/>

Hasil : <br/>
![image](https://github.com/user-attachments/assets/b3ca0a36-c055-46d8-a5ac-b69c5e2b7dfc)

#### Identifikasi Outliers
Outliers adalah data yang menyimpang signifikan dari pola umum data dan dapat mempengaruhi hasil analisis statistik serta model prediksi. Identifikasi outliers penting untuk memahami kualitas data dan dapat mempengaruhi pengambilan keputusan dalam analisis lebih lanjut.
##### 1. Mengidentifikasi Outliers Menggunakan Box Plot
Box plot adalah alat visual yang umum digunakan untuk mendeteksi outliers. Box plot menunjukkan distribusi data melalui kuartil, median, dan "whiskers" yang menunjukkan rentang data. Outliers biasanya ditunjukkan sebagai titik-titik di luar whiskers.<br/>

**Langkah-langkah**<br/>
- **a. Pilih Kolom Numerik** : Pertama, kita memilih kolom-kolom numerik dari dataset yang akan dianalisis untuk outliers.<br/>

numeric_cols = df.select_dtypes (include=np.number .columns.tolist()<br/>
- **b. Buat Box Plot untuk Setiap Kolom** : Untuk setiap kolom numerik, kita membuat box plot. Ini memungkinkan kita untuk visualisasi distribusi dan mengidentifikasi nilai-nilai yang menyimpang.

plt.figure(figsize=(15,10))<br/>
for i, column in enumerate(numeric_cols, 1):<br/>
    plt.subplot(4, 4, i)<br/>
    sns.boxplot(y=df[column])<br/>
    plt.title(f'Box Plot of {column}')<br/>
plt.tight_layout()<br/>
plt.show()<br/>

- **Fungsi**:
  - **plt.figure(figsize=(15,10))**: Mengatur ukuran dari figur plot.
  - **for i, column in enumerate(numeric_cols, 1)**: Iterasi untuk setiap kolom numerik, dimana setiap kolom akan diidentifikasi dan dipetakan ke subplot.
  - **sns.boxplot(y=df[column])**: Membuat box plot untuk setiap kolom numerik untuk mengidentifikasi outliers.
  - **plt.tight_layout()**: Mengatur tata letak subplot agar tidak saling tumpang tindih.
  - **plt.show()**: Menampilkan plot.

    Hasil :<br/>
    ![image](https://github.com/user-attachments/assets/10b290b6-9cfd-401b-9e4d-43019fa042aa)

Dari analisis box plot, beberapa kolom dalam dataset menunjukkan adanya outliers yang signifikan. Outliers ini bisa jadi merupakan indikasi dari data yang tidak valid atau kasus yang ekstrem, dan perlu ditangani dengan hati-hati. 
- Beberapa pendekatan untuk menangani outliers termasuk:
  - Pengecualian: Menghapus outliers dari dataset jika dianggap tidak representatif.
  - Transformasi: Menggunakan transformasi untuk mengurangi dampak outliers.
  - Analisis Terpisah: Menganalisis outliers secara terpisah untuk memahami pengaruhnya.

Identifikasi dan penanganan outliers yang tepat penting untuk memastikan kualitas dan keakuratan analisis data lebih lanjut.

#### Statik Dekriptif
Statistik deskriptif memberikan ringkasan numerik dari data dalam dataset, mencakup ukuran pusat, ukuran dispersi, dan distribusi data. Berikut adalah statistik deskriptif untuk setiap kolom numerik dalam dataset Heart Disease UCI.

##### 1. Mean
Mean adalah nilai rata-rata dari data dan memberikan gambaran umum tentang pusat distribusi.<br/>

print("\nMean:")<br/>
print(df.mean())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/a81b348c-64a0-4d45-ae5b-8c99f66f0f7d)

##### 2. Median
Median adalah nilai tengah yang membagi data menjadi dua bagian yang sama. Ini berguna untuk memahami pusat distribusi data, terutama jika data memiliki outliers.<br/>

print("\nMedian:")<br/>
print(df.median())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/82c404d8-bc00-47d8-a5c3-6960d0bd1af4)

##### 3. Mode
Mode adalah nilai yang paling sering muncul dalam dataset. Ini memberikan informasi tentang nilai yang paling umum.<br/>

print("\nMode:")<br/>
print(df.mode().iloc[0])<br/>

Hasil : <br/>
![image](https://github.com/user-attachments/assets/d3727bd3-7950-4ffc-b432-4f435a494c81)

##### 4. Standar Deviasi (Standard Deviation)
Standar deviasi mengukur seberapa jauh data menyebar dari nilai rata-rata. Nilai yang lebih tinggi menunjukkan variabilitas yang lebih besar.<br/>

print("\nStandard Deviation:")<br/>
print(df.std())<br/>

Hasil : <br/>
![image](https://github.com/user-attachments/assets/59f5c754-3efd-4cfc-a0d2-12b2362ba919)

##### 5. Variansi (Variance)
Variansi adalah ukuran seberapa jauh data menyebar dari rata-rata dan merupakan kuadrat dari standar deviasi.<br/>

print("\nVariance:")<br/>
print(df.var())<br/>

Hasil : <br/>
![image](https://github.com/user-attachments/assets/c0af9b8e-96ca-4f3f-bdb6-0117f511da20)

##### 6. Skewness
Skewness mengukur asimetri distribusi data. Skewness yang positif menunjukkan ekor distribusi di sisi kanan, sementara skewness negatif menunjukkan ekor di sisi kiri.<br/>

print("\nSkewness:")<br/>
print(df.skew())<br/>

Hasil : <br/>
![image](https://github.com/user-attachments/assets/9269f29c-bf1e-4083-927d-ecaa953e1e6f)

##### 7. Kurtosis
Kurtosis mengukur ketinggian puncak distribusi data. Kurtosis positif menunjukkan distribusi yang lebih tajam dengan ekor yang lebih berat, sementara kurtosis negatif menunjukkan distribusi yang lebih datar.<br/>

print("\nKurtosis:")<br/>
print(df.kurtosis())<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/b566a0a0-8920-439b-b47c-e8b6f71283a0)
Bagian statistik deskriptif ini memberikan gambaran menyeluruh tentang data dan memungkinkan untuk memahami karakteristik utama dari dataset sebelum melanjutkan dengan analisis lebih lanjut atau pemodelan.

#### Korelasi Antar Variabel
Korelasi adalah ukuran statistik yang menunjukkan derajat hubungan linear antara dua variabel. Nilai korelasi berkisar antara -1 hingga 1:
- 1 menunjukkan hubungan positif sempurna.
- -1 menunjukkan hubungan negatif sempurna.
- 0 menunjukkan tidak ada hubungan linear.

##### 1. Matriks Korelasi
Matriks korelasi adalah tabel yang menunjukkan nilai korelasi antara setiap pasangan variabel dalam dataset. Ini membantu untuk mengidentifikasi variabel yang memiliki hubungan kuat.<br/>

correlation_matrix = df.corr()<br/>

print("\nMatriks Korelasi:")<br/>
print(correlation_matrix)<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/97682769-92b6-4a71-81fa-aed4356640cc)

##### 2. Visualisasi Korelasi
Visualisasi matriks korelasi menggunakan heatmap membantu dalam memahami hubungan antar variabel secara lebih intuitif.<br/>

plt.figure(figsize=(12,8))<br/>
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')<br/>
plt.title('Matriks Korelasi Antar Variabel')<br/>
plt.show()<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/2baa0800-cebc-4ef7-b0b8-0fad75613fdd)

##### 3. Identifikasi Pasangan Variabel dengan Korelasi Tinggi
Pasangan variabel yang memiliki korelasi tinggi (> 0.5 atau < -0.5) menunjukkan hubungan yang signifikan dan dapat diperhatikan lebih lanjut dalam analisis.<br/>

threshold = 0.5<br/>

high_corr = correlation_matrix.abs() > threshold<br/>
high_corr = high_corr.where(np.triu(np.ones(high_corr.shape), k=1).astype(bool))<br/>
pairs = high_corr.stack().index.tolist()<br/>

print("\nPasangan Variabel dengan Korelasi Tinggi:")<br/>
for pair in pairs:<br/>
    print(f'{pair[0]} dan {pair[1]}: {correlation_matrix.loc[pair[0], pair[1]]}')<br/>

Hasil :<br/>
![image](https://github.com/user-attachments/assets/7d2b6a58-46c0-4732-8c2d-378f0838221c)
Bagian ini memberikan panduan rinci tentang korelasi antar variabel dalam dataset Heart Disease UCI. Informasi ini membantu untuk memahami hubungan antara variabel dan dapat digunakan untuk analisis lebih lanjut, seperti pemodelan dan prediksi.

#### Visualisasi Data
##### 1. Histogram
Histogram menggambarkan distribusi data untuk setiap variabel numerik dalam dataset. Ini membantu untuk memahami bentuk distribusi data dan mengidentifikasi pola seperti skewness atau outliers.<br/>

numeric_df.hist(bins=15, figsize=(15,10), layout=(4,4))<br/>
plt.suptitle('Histogram Variabel Numerik')<br/>
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Untuk menghindari overlap judul<br/>
plt.show()<br/>

Hasil :
![image](https://github.com/user-attachments/assets/5cffc65d-0e36-4f1d-bda7-b95c369c8053)

##### 2. Scetter Plot
Scatter plot adalah grafik yang menampilkan hubungan antara dua variabel numerik dengan setiap titik mewakili satu pengamatan. Ini digunakan untuk mengidentifikasi pola, tren, atau korelasi antara variabel.<br/>

threshold = 0.5<br/>
high_corr = correlation_matrix.abs() > threshold<br/>
high_corr = high_corr.where(np.triu(np.ones(high_corr.shape), k=1).astype(bool))<br/>
pairs = high_corr.stack().index.tolist()<br/>

for pair in pairs:<br/>
    if 'target' in df.columns:<br/>
        sns.scatterplot(x=pair[0], y=pair[1], data=df, hue='target')<br/>
        plt.title(f'Scatter Plot of {pair[0]} vs {pair[1]}')<br/>
        plt.show()<br/>
    else:<br/>
        sns.scatterplot(x=pair[0], y=pair[1], data=df)<br/>
        plt.title(f'Scatter Plot of {pair[0]} vs {pair[1]}')<br/>
        plt.show()<br/>

Hasil :<br/>
![1](https://github.com/user-attachments/assets/0d652d5e-f8b3-4d8b-9ea1-b301fc74b119)
![2](https://github.com/user-attachments/assets/611d8a7a-91cf-4fb1-9991-6f51f03c0c06)
![3](https://github.com/user-attachments/assets/670b55b2-4a83-4a58-bb49-b669da7d7b31)
![4](https://github.com/user-attachments/assets/64c17934-7745-4c5d-8bb9-e3799b6487ee)
![5](https://github.com/user-attachments/assets/40952722-f1b6-46c4-915a-be13fdbaf067)
![6](https://github.com/user-attachments/assets/c21d144b-bf84-41c3-8539-2e0a22465ba9)
![7](https://github.com/user-attachments/assets/6476480f-0115-4f3e-8b9b-4472bb985906)
![8](https://github.com/user-attachments/assets/2901c120-3411-496a-8ab0-b27a259832fe)
![9](https://github.com/user-attachments/assets/96334529-ceee-41cc-a0ba-3d7d49a14402)
![10](https://github.com/user-attachments/assets/36a139f6-3a66-4c20-aeb2-befbf394315b)
![11](https://github.com/user-attachments/assets/4941c1eb-8956-4e50-9a51-c395311cb1c9)
![12](https://github.com/user-attachments/assets/0c460a5a-a6da-4719-9b63-9d15d648f78f)
![13](https://github.com/user-attachments/assets/ea2b1963-2223-447d-9aef-b3b2a8fc3981)
![14](https://github.com/user-attachments/assets/7f59630e-abe3-4a47-8bef-bf99e5f7cdd5)
![15](https://github.com/user-attachments/assets/aa410900-6f06-475e-ab5e-3a59d474b6d3)
![16](https://github.com/user-attachments/assets/629e2380-0e8a-473d-8636-b329599eb370)
![17](https://github.com/user-attachments/assets/3fc1164f-8197-4714-8f7e-cdca6f4b695c)
![18](https://github.com/user-attachments/assets/fdcb153c-d8fd-401b-b146-6e8bdacb5cdb)
![19](https://github.com/user-attachments/assets/4a040f05-9c02-4743-826a-ceb5081ed50c)
![20](https://github.com/user-attachments/assets/68ddfa12-2540-4e75-9b18-285b73a3453d)
![21](https://github.com/user-attachments/assets/554d9555-7de9-4cf1-8482-e27a78a6c0af)
![22](https://github.com/user-attachments/assets/290d8ee0-c975-43e5-a7d8-8d986ac14332)
![23](https://github.com/user-attachments/assets/be5e27cc-2ec3-450b-90f8-16d56b987856)
![24](https://github.com/user-attachments/assets/b3f5e667-e2f5-41a1-a025-7d55133469fd)
![25](https://github.com/user-attachments/assets/5fa9f6bc-2a67-4bfd-874a-103b2f2fe364)
![26](https://github.com/user-attachments/assets/40031da8-f028-4927-993f-0988ade9510c)
![27](https://github.com/user-attachments/assets/440dbd64-e35e-402e-ac87-84adf2d2b7dd)
![28](https://github.com/user-attachments/assets/2fcc2b49-5a3f-4a1e-b849-35a01558f040)
![29](https://github.com/user-attachments/assets/34cd330a-a896-4e9b-bc44-9f5858df4406)

## Penutup
### Kesimpulan
Laporan ini menganalisis dataset Heart Disease UCI, memberikan wawasan mendalam tentang karakteristik data, seperti distribusi usia, tekanan darah, dan kolesterol yang menunjukkan ketidakseimbangan dan keberadaan outliers signifikan. Analisis mengidentifikasi korelasi penting, seperti antara usia dan detak jantung maksimum, serta kolesterol dan jumlah vessels, yang dapat mempengaruhi hasil analisis lebih lanjut. Visualisasi data menggunakan histogram, box plot, dan scatter plot membantu mengungkap pola distribusi dan hubungan antar variabel yang signifikan. Berdasarkan temuan ini, disarankan untuk memberikan perhatian khusus pada variabel dengan outliers dan mempertimbangkan transformasi data untuk menangani skewness, guna meningkatkan akurasi model prediktif penyakit jantung. Laporan ini menyediakan fondasi yang kuat untuk analisis lebih lanjut dan pengembangan model prediksi yang lebih efektif dalam mendeteksi risiko penyakit jantung.

****





