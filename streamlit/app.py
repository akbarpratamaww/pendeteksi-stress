import streamlit as st
import pandas as pd
import numpy as np

# Membaca dataset dari file CSV
df = pd.read_csv('C:/Users/lenov/OneDrive/Documents/GitHub/FINAL-PROJECT-STATISTIKA-KOMPUTASI/Dataset_Stres - dataset.csv')

# Hapus kolom Deskripsi Gejala
df.drop('Deskripsi Gejala', axis=1, inplace=True)

# Mengonversi kolom nilai menjadi numerik
df['Nilai Gejala Berat (T3)'] = pd.to_numeric(df['Nilai Gejala Berat (T3)'], errors='coerce')
df['Nilai Gejala Sedang (T2)'] = pd.to_numeric(df['Nilai Gejala Sedang (T2)'], errors='coerce')
df['Nilai Gejala Ringan (T1)'] = pd.to_numeric(df['Nilai Gejala Ringan (T1)'], errors='coerce')


# Filter berdasarkan gejala yang memiliki nilai lebih dari 0.1
filtered_df_ringan = df[df['Nilai Gejala Ringan (T1)'] > 0.1]
Nilai_Awal_Ringan = filtered_df_ringan['Nilai Gejala Ringan (T1)'].sum()

filtered_df_sedang = df[df['Nilai Gejala Sedang (T2)'] > 0.1]
Nilai_Awal_Sedang = filtered_df_sedang['Nilai Gejala Sedang (T2)'].sum()

filtered_df_berat = df[df['Nilai Gejala Berat (T3)'] > 0.1]
Nilai_Awal_Berat = filtered_df_berat['Nilai Gejala Berat (T3)'].sum()

# Menghitung Nilai Bobot
Nilai_Bobot_Ringan = Nilai_Awal_Ringan / 3
Nilai_Bobot_Sedang = Nilai_Awal_Sedang / 3
Nilai_Bobot_Berat = Nilai_Awal_Berat / 3

# Streamlit input
st.markdown(
    "<h1 style='text-align: center;'>PENDETEKSI TINGKATAN STRES MAHASISWA AKHIR</h1>",
    unsafe_allow_html=True
)

st.markdown( 
    "Website Ini Akan Membantu Mendeteksi Tingkat Stres Yang Kalian Miliki &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)
data = {
    "Kode Gejala": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
             "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20",
             "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30"
            ],
    "Nama Gejala": ["Sakit Pinggang", "Sesak Nafas", "Gangguan Pencernaan Berat", "Keringat Berlebihan", "Nafsu Makan Menurun",
               "Terlalu Peka", "Merasa Putus Asa/Sudah Tidak Punya Harapan", "Merasa Takut", "Tremor(Gemetar Tidak Terkendali)", "Kurang Bersemangat",
               "Sering Emosi/Emosi Tidak Terkontrol", "Sakit Kepala", "Mudah Menangis","Merasa Cemas", "Suasana Hati Mudah Berubah(Moodyan)",
               "Pendiam (Introvert)", "Maag", "Sering Ketegangan Otot di bagian Tertentu(leher, bahu, dan punggung)", "Prestasi Menurun", "Mudah Lelah/Capek",
               "Sering Lupa", "Tidak Fokus (sulit konsentrasi)", "Sulit Tidur", "Hilang Rasa Percaya Diri", "Jantung Berdebar Semakin Meningkat",
               "Kehilangan Rasa Humor", "Mudah Tersinggung/Sensitif", "Pikiran Kacau", "Sering Menyendiri", "Alergi/Gatal-Gatal Pada Kulit"  
              ],
}

# Membuat DataFrame
df2 = pd.DataFrame(data)

st.markdown(
    "<h3 style='text-align: center;'>Tabel Gejala Penyakit</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='display: flex; justify-content: center;'><div style='text-align: center;'>"
    + df2.to_html(index=False)
    + "</div></div>",
    unsafe_allow_html=True,
)
# Form input user di Streamlit
with st.form(key="form_input"):
    nama = st.text_input("Masukkan Nama:")
    
    # Input Gejala: Menggunakan input tipe teks yang diharapkan dipisahkan koma
    stres_level = st.text_input("Masukkan Lima Kode Gejala Stres Anda (Misal: G1, G2, G3, G4, G5):")
    
    semester = st.selectbox(
        "Masukkan Semester Anda:",
        ("1", "2", "3", "4", "5", "6", "7", "8"),
        index=0,
        placeholder="Masukkan Semester",
    )

    submit_button = st.form_submit_button(label="Submit")

# Proses data setelah submit
if submit_button:
    if not nama:
        st.error("Nama tidak boleh kosong!")
    elif not stres_level:
        st.error("Tingkat stres tidak boleh kosong!")
    elif not semester:
        st.error("Mohon isi semester Anda!")
    else:
        # Proses input gejala dari Streamlit
        kode_input = [kode.strip() for kode in stres_level.split(',')]
        
        # Inisialisasi total nilai
        total_nilai_ringan = 0
        total_nilai_sedang = 0
        total_nilai_berat = 0

        # Mengambil nilai untuk setiap kode gejala yang dimasukkan
        for kode in kode_input:
            if kode in df['Kode Gejala'].values:
                nilai_gejala_ringan = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
                total_nilai_ringan += nilai_gejala_ringan


        # Mengambil nilai untuk gejala sedang
        for kode in kode_input:
            if kode in df['Kode Gejala'].values:
                nilai_gejala_sedang = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
                total_nilai_sedang += nilai_gejala_sedang


        # Mengambil nilai untuk gejala berat
        for kode in kode_input:
            if kode in df['Kode Gejala'].values:
                nilai_gejala_berat = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
                total_nilai_berat += nilai_gejala_berat


        # Menghitung prior x likelihood stress
        prior_ringan = Nilai_Bobot_Ringan
        likelihood_ringan = total_nilai_ringan
        PxL_ringan = prior_ringan * likelihood_ringan

        prior_sedang = Nilai_Bobot_Sedang
        likelihood_sedang = total_nilai_sedang
        PxL_sedang = prior_sedang * likelihood_sedang

        prior_berat = Nilai_Bobot_Berat
        likelihood_berat = total_nilai_berat
        PxL_berat = prior_berat * likelihood_berat

        posterior_ringan = PxL_ringan / (PxL_ringan + PxL_sedang + PxL_berat)
        posterior_sedang = PxL_sedang / (PxL_ringan + PxL_sedang + PxL_berat)
        posterior_berat = PxL_berat / (PxL_ringan + PxL_sedang + PxL_berat)

        if posterior_ringan > posterior_sedang and posterior_ringan > posterior_berat:
            st.success(f"Maka Anda mengalami Stress Ringan")
        elif posterior_sedang > posterior_berat:
            st.success(f"Maka Anda mengalami Stress Sedang")
        else:
            st.success(f"Maka Anda mengalami Stress Berat")
    #nyoba