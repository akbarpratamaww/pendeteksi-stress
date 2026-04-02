import streamlit as st
import pandas as pd
import numpy as np

# Membaca dataset dari file CSV
df = pd.read_csv('dataset_stres.csv')

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

# Menambahkan gaya CSS dan animasi
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f7fa;
    }
    .main-title {
        text-align: center;
        color: #3d85c6;
        animation: fadeIn 2s;
    }
    .sub-title {
        text-align: center;
        color: #6aa84f;
        margin-bottom: 20px;
        animation: fadeInUp 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .card {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
        padding: 20px;
        margin: 10px 0;
        animation: fadeIn 2s;
    }
    .dataframe {
        text-align: center;
        color: #333;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 10px;
        font-size: 14px;
    }
    .dataframe th, .dataframe td {
        text-align: center;
        padding: 8px;
    }
    .dataframe th {
        background-color: #3d85c6;
        color: #fff;
    }
</style>
    """,
    unsafe_allow_html=True,
)

# Judul dan Deskripsi
st.markdown("<h1 class='main-title'>✨ PENDETEKSI TINGKAT STRES MAHASISWA AKHIR ✨</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 class='sub-title'>😊 Selamat Datang! Kami siap membantu Anda mendeteksi tingkat stres Anda.😊 </h4>",
    unsafe_allow_html=True,
)

data = {
    "Kode Gejala": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
             "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20",
             "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30"],
    "Nama Gejala": [
        "Sakit Pinggang", "Sesak Nafas", "Gangguan Pencernaan Berat", "Keringat Berlebihan", "Nafsu Makan Menurun",
        "Terlalu Peka", "Merasa Putus Asa/Sudah Tidak Punya Harapan", "Merasa Takut", "Tremor(Gemetar Tidak Terkendali)", "Kurang Bersemangat",
        "Sering Emosi/Emosi Tidak Terkontrol", "Sakit Kepala", "Mudah Menangis","Merasa Cemas", "Suasana Hati Mudah Berubah(Moodyan)",
        "Pendiam (Introvert)", "Maag", "Sering Ketegangan Otot di bagian Tertentu(leher, bahu, dan punggung)", "Prestasi Menurun", "Mudah Lelah/Capek",
        "Sering Lupa", "Tidak Fokus (sulit konsentrasi)", "Sulit Tidur", "Hilang Rasa Percaya Diri", "Jantung Berdebar Semakin Meningkat",
        "Kehilangan Rasa Humor", "Mudah Tersinggung/Sensitif", "Pikiran Kacau", "Sering Menyendiri", "Alergi/Gatal-Gatal Pada Kulit"
    ],
}

df2 = pd.DataFrame(data)

st.markdown("<h3 class='main-title'>📋 Tabel Gejala Penyakit 📋</h3>", unsafe_allow_html=True)
st.table(df2)

with st.form(key="form_input"):
    nama = st.text_input("Masukkan Nama 🧑‍🎓:")
    stres_level = st.text_input("Masukkan Lima Kode Gejala Anda 🧠 (Misal: G1, G2, G3):")
    semester = st.selectbox("Pilih Semester Anda 📚:", ("1", "2", "3", "4", "5", "6", "7", "8"), index=0)
    submit_button = st.form_submit_button(label="Submit 🚀")

if submit_button:
    if not nama:
        st.error("🚫 Nama tidak boleh kosong! 🙅‍♂️")
    elif not stres_level:
        st.error("🚫 Tingkat stres tidak boleh kosong! 🛑")
    elif not semester:
        st.error("🚫 Harap isi semester Anda! 🤔")
    else:
        kode_input = [kode.strip() for kode in stres_level.split(',')]
        total_nilai_ringan = 0
        total_nilai_sedang = 0
        total_nilai_berat = 0

        for kode in kode_input:
            if kode in df['Kode Gejala'].values:
                nilai_gejala_ringan = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
                total_nilai_ringan += nilai_gejala_ringan

                nilai_gejala_sedang = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
                total_nilai_sedang += nilai_gejala_sedang

                nilai_gejala_berat = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
                total_nilai_berat += nilai_gejala_berat

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

        if posterior_ringan > posterior_sedang:
            st.success("\U0001F33C Maka Anda mengalami Stres Ringan \U0001F33C")
            st.markdown(
                """
                <p style="font-size: 16px; text-align: center;">
                    Mengalami stres ringan adalah hal yang wajar, namun penting untuk segera menanganinya agar tidak berkembang menjadi masalah yang lebih besar.
                </p>
                """,
                unsafe_allow_html=True,
            )
            
            # Dropdown saran untuk stres ringan
            saran_opsi = st.selectbox(
                "\U0001F4A1 Pilih saran yang ingin Anda coba untuk mengatasi stres ringan:",
                [
                    "Peregangan dan Olahraga Ringan \U0001F3C3\u200D\U0001F3FC",
                    "Pernapasan Dalam \U0001F9D8",
                    "Mendengarkan Musik \U0001F3B5",
                    "Hindari Kafein dan Nikotin \u2615\u200D\U0001F6AB",
                    "Curhat ke Teman atau Keluarga \U0001F91D",
                    "Menulis Jurnal \U0001F4D2",
                    "Melakukan Aktivitas yang Disukai \U0001F3A8"
                ],
            )

            # Tampilkan deskripsi saran berdasarkan pilihan
            if saran_opsi == "Peregangan dan Olahraga Ringan \U0001F3C3\u200D\U0001F3FC":
                st.info("Luangkan waktu 10-15 menit untuk berjalan kaki atau melakukan peregangan. Ini bisa membantu melepaskan hormon endorfin yang mengurangi stres.")
            elif saran_opsi == "Pernapasan Dalam \U0001F9D8":
                st.info("Cobalah teknik pernapasan dalam atau meditasi. Duduk dengan nyaman, tutup mata, dan tarik napas dalam-dalam melalui hidung, tahan sebentar, lalu hembuskan perlahan melalui mulut.")
            elif saran_opsi == "Mendengarkan Musik \U0001F3B5":
                st.info("Putar lagu favorit Anda atau musik yang menenangkan. Musik memiliki kekuatan untuk mengubah suasana hati dan memberikan rasa tenang.")
            elif saran_opsi == "Hindari Kafein dan Nikotin \u2615\u200D\U0001F6AB":
                st.info("Bahan-bahan ini bisa meningkatkan kadar stres. Coba ganti dengan air putih, teh herbal, atau jus buah.")
            elif saran_opsi == "Curhat ke Teman atau Keluarga \U0001F91D":
                st.info("Berbagi perasaan dan cerita dengan orang terdekat bisa sangat membantu. Mereka mungkin memberikan perspektif yang berbeda atau hanya menjadi pendengar yang baik.")
            elif saran_opsi == "Menulis Jurnal \U0001F4D2":
                st.info("Tuliskan apa yang membuat Anda stres dan bagaimana perasaan Anda. Ini bisa membantu Anda memproses emosi dan menemukan solusi yang mungkin belum terpikirkan.")
            elif saran_opsi == "Melakukan Aktivitas yang Disukai \U0001F3A8":
                st.info("Lakukan sesuatu yang Anda nikmati, seperti membaca, menggambar, menonton film, atau berkebun. Aktivitas ini bisa menjadi pelarian sejenak dari tekanan.")

            st.markdown(
                "<p style='text-align: center; font-size: 14px;'>Ingatlah, setiap orang memiliki cara berbeda untuk mengatasi stres. Temukan yang terbaik untuk Anda dan tetap semangat! \U0001F33C</p>",
                unsafe_allow_html=True,
            )

        elif posterior_sedang > posterior_berat:
            st.success("Maka Anda mengalami Stres Sedang")
            st.success("Maka Anda mengalami Stres Sedang")
            st.markdown(
                """
                Berikut adalah saran singkat untuk mengatasi stres sedang:
                
                - **Olahraga Teratur:** Aktivitas fisik seperti jogging atau yoga.
                - **Rencana dan Prioritas:** Buat daftar tugas dan atur prioritas.
                - **Teknik Relaksasi:** Meditasi, pernapasan dalam, atau relaksasi otot progresif.
                - **Batasi Pemicu Stres:** Hindari hal-hal yang membuat Anda stres.
                - **Diet Sehat:** Konsumsi makanan seimbang dan hindari kafein.
                - **Cari Dukungan:** Berbicara dengan teman, keluarga, atau profesional.
                - **Mengembangkan Hobi:** Luangkan waktu untuk aktivitas yang Anda nikmati.
                - **Tidur yang Cukup:** Pastikan tidur Anda berkualitas.
                - **Berlatih Mindfulness:** Fokus pada momen saat ini.
                - **Pertimbangkan Terapi:** Konsultasi dengan terapis jika diperlukan.
                """,
                unsafe_allow_html=True
            )
        else:
            st.success("Maka Anda mengalami Stres Berat")
            st.warning("Anda disarankan untuk berkonsultasi lebih lanjut mengenai kondisi Anda.")
            st.markdown(
                """
                <a href="https://www.halodoc.com/kesehatan-mental" target="_blank" style="text-decoration:none;">
                    <button style="background-color:#ff4d4d; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;">
                        Konsultasi Sekarang di Halodoc
                    </button>
                </a>
                """,
                unsafe_allow_html=True,
            )