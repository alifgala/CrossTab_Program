import streamlit as st
import pandas as pd

# Fungsi untuk menyimpan hasil analisis antar iterasi
if "all_results" not in st.session_state:
    st.session_state["all_results"] = []  # Untuk menyimpan semua hasil iterasi

# Judul aplikasi
st.title("Aplikasi Automasi Analisis Crosstab")
st.title("(Masukkan file berekstensi excel yang memiliki minimal 3 kolom/fitur")

# Unggah file Excel
uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx", "csv"])

# Pastikan file diunggah
if uploaded_file is not None:
    # Baca file
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
   # Bersihkan nama kolom
    df.columns = df.columns.str.strip().str.upper()
    st.write("Data yang diunggah:")
    st.write(df.head())

    # Input kolom indeks
    index_column = st.text_input("Masukkan kolom indeks (contoh: Q7):").strip().upper()
    if index_column and index_column not in df.columns:
        st.warning(f"Kolom indeks '{index_column}' tidak ditemukan di data.")
    elif index_column:
        # Input kolom yang ingin diproses
        columns_to_analyze = st.text_input("Masukkan kolom yang ingin diproses (pisahkan dengan koma):")
        columns_to_analyze = [col.strip().upper() for col in columns_to_analyze.split(',')]
        columns_to_analyze = [col for col in columns_to_analyze if col in df.columns]

        if not columns_to_analyze:
            st.warning("Tidak ada kolom yang valid untuk diproses.")
        else:
            # Input kolom values dan tipe agregasi
            value_column = st.text_input("Masukkan kolom untuk values (atau ketik 'count' untuk menghitung frekuensi):").strip().upper()
            agg_func = st.text_input("Masukkan tipe agregasi (contoh: sum, mean, min, max, count):").strip().lower()

            # Input metode perhitungan persentase
            percentage_method = st.radio("Masukkan metode persentase:", ["baris", "kolom"]).lower()

            # Tombol untuk memulai analisis
            if st.button("Mulai Analisis"):
                crosstab_results = []

                for col in columns_to_analyze:
                    # Buat crosstab sesuai input pengguna
                    if value_column.lower() == 'count':
                        crosstab_result = pd.crosstab(index=df[index_column], columns=df[col])
                    else:
                        crosstab_result = pd.crosstab(index=df[index_column], columns=df[col], 
                                                      values=df[value_column], aggfunc=agg_func)

                    # Hitung persentase
                    if percentage_method == 'baris':
                        crosstab_percentage = crosstab_result.div(crosstab_result.sum(axis=1), axis=0) * 100
                    elif percentage_method == 'kolom':
                        crosstab_percentage = crosstab_result.div(crosstab_result.sum(axis=0), axis=1) * 100

                    # Format hasil sesuai permintaan
                    crosstab_df = crosstab_result.stack().reset_index()
                    crosstab_df.columns = ['Value_indeks', 'Value', 'Frekuensi']
                    crosstab_df['Persentase'] = crosstab_percentage.stack().values
                    crosstab_df['Kolom yang Dianalisis'] = col
                    crosstab_df['Indeks yang Digunakan'] = index_column

                    # Atur urutan kolom
                    crosstab_df = crosstab_df[['Kolom yang Dianalisis', 'Indeks yang Digunakan', 'Value', 
                                               'Value_indeks', 'Persentase']]

                    # Tambahkan ke hasil iterasi
                    crosstab_results.append(crosstab_df)

                # Gabungkan hasil iterasi
                iter_result = pd.concat(crosstab_results, ignore_index=True)
                st.session_state["all_results"].append(iter_result)

                # Tampilkan hasil iterasi saat ini
                st.write("Hasil Crosstab Iterasi Saat Ini:")
                st.dataframe(iter_result)

    # Jika ada hasil dari iterasi sebelumnya
    if st.session_state["all_results"]:
        # Gabungkan semua hasil
        final_result = pd.concat(st.session_state["all_results"], ignore_index=True)
        st.write("Hasil Gabungan Semua Iterasi:")
        st.dataframe(final_result)

        # Tombol unduh hasil gabungan
        if st.button("Unduh Hasil Gabungan"):
            final_file = "hasil_crosstab_gabungan.xlsx"
            final_result.to_excel(final_file, index=False)
            with open(final_file, "rb") as f:
                st.download_button("Klik untuk Mengunduh", f, file_name=final_file)
