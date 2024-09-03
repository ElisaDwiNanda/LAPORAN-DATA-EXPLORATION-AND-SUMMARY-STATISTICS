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
##### Import Library
**import pandas as pd**
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
