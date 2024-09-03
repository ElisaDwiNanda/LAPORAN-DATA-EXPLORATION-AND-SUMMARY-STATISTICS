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
- **Pilih Kolom Numerik** : Pertama, kita memilih kolom-kolom numerik dari dataset yang akan dianalisis untuk outliers.<br/>

numeric_cols = df.select_dtypes (include=np.number .columns.tolist()<br/>
- **Buat Box Plot untuk Setiap Kolom** : Untuk setiap kolom numerik, kita membuat box plot. Ini memungkinkan kita untuk visualisasi distribusi dan mengidentifikasi nilai-nilai yang menyimpang.

plt.figure(figsize=(15,10))<br/>
for i, column in enumerate(numeric_cols, 1):<br/>
    plt.subplot(4, 4, i)<br/>
    sns.boxplot(y=df[column])<br/>
    plt.title(f'Box Plot of {column}')<br/>
plt.tight_layout()<br/>
plt.show()<br/>



- 
- 
