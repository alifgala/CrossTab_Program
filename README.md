# Aplikasi Automasi Analisis Crosstab

Aplikasi ini memungkinkan pengguna untuk mengunggah file Excel atau CSV dan melakukan analisis crosstab secara otomatis, termasuk perhitungan frekuensi dan persentase berdasarkan kolom yang dipilih. Hasil dari setiap iterasi analisis dapat disimpan dan digabungkan untuk menghasilkan hasil analisis akhir yang dapat diunduh dalam format Excel.

## Fitur
- Mengunggah file Excel atau CSV untuk analisis.
- Menentukan kolom indeks untuk digunakan dalam analisis.
- Memilih kolom yang ingin dianalisis dengan crosstab.
- Memilih kolom nilai dan metode agregasi (misalnya: `sum`, `mean`, `count`).
- Pilih metode perhitungan persentase (berdasarkan baris atau kolom).
- Lihat hasil analisis crosstab secara langsung di aplikasi.
- Simpan dan unduh hasil analisis gabungan dalam format Excel.

## Cara Menggunakan Aplikasi
1. **Unggah File**  
   Unggah file Excel (`.xlsx`) atau CSV (`.csv`) dengan data yang ingin dianalisis.

2. **Masukkan Kolom Indeks**  
   Masukkan nama kolom yang ingin digunakan sebagai indeks dalam analisis crosstab.

3. **Pilih Kolom untuk Analisis**  
   Masukkan kolom-kolom yang ingin dianalisis (pisahkan dengan koma).

4. **Pilih Kolom Nilai dan Metode Agregasi**  
   Tentukan kolom yang berisi nilai untuk dihitung dan pilih metode agregasi seperti `sum`, `mean`, `count`, dll.

5. **Pilih Metode Persentase**  
   Pilih apakah Anda ingin menghitung persentase berdasarkan baris atau kolom.

6. **Mulai Analisis**  
   Klik tombol untuk memulai analisis. Hasil analisis akan ditampilkan dalam bentuk tabel crosstab dengan frekuensi dan persentase.

7. **Unduh Hasil Gabungan**  
   Jika Anda ingin mengunduh hasil analisis gabungan dari semua iterasi, klik tombol "Unduh Hasil Gabungan".

## Instalasi
1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/repository.git
2. Masuk ke direktori proyek:
   ```bash
   cd repository
3. Buat lingkungan virtual dan aktifkan:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Di MacOS/Linux
   venv\Scripts\activate  # Di Windows
4. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
5. Jalankan aplikasi:
   ```bash
   streamlit run app.py

## Teknologi yang Digunakan
Streamlit: Framework untuk membuat aplikasi web interaktif dengan Python.
Pandas: Library Python untuk manipulasi data dan analisis.
XlsxWriter: Digunakan untuk menulis file Excel dalam format .xlsx.
## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork repositori ini, lakukan perubahan pada cabang (branch) Anda, dan buat pull request.
