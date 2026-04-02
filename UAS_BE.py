import pandas as pd
import numpy as np


#membaca dataset dari excel
df = pd.read_csv('C:/Penyimpanan Utama/Documents/GitHub/FINAL-PROJECT-STATISTIKA-KOMPUTASI/Dataset_Stres - dataset.csv')



df.head(10)

df.drop('Deskripsi Gejala', axis = 1, inplace = True)

df.head(30)

df.loc[29,'Nilai Gejala Berat (T3)'] = 0.3

df['Nilai Gejala Berat (T3)'] = pd.to_numeric(df['Nilai Gejala Berat (T3)'], errors='coerce')
df['Nilai Gejala Sedang (T2)'] = pd.to_numeric(df['Nilai Gejala Sedang (T2)'], errors='coerce')
df['Nilai Gejala Ringan (T1)'] = pd.to_numeric(df['Nilai Gejala Ringan (T1)'], errors='coerce')

filtered_df_ringan = df[df['Nilai Gejala Ringan (T1)']>0.1]
Nilai_Awal_Ringan = filtered_df_ringan['Nilai Gejala Ringan (T1)'].sum()
filtered_df_sedang = df[df['Nilai Gejala Sedang (T2)']>0.1]
Nilai_Awal_Sedang = filtered_df_sedang['Nilai Gejala Sedang (T2)'].sum()
filtered_df_berat = df[df['Nilai Gejala Berat (T3)']>0.1]
Nilai_Awal_Berat = filtered_df_berat['Nilai Gejala Berat (T3)'].sum()


Nilai_Bobot_Ringan = Nilai_Awal_Ringan/3
Nilai_Bobot_Sedang = Nilai_Awal_Sedang/3
Nilai_Bobot_Berat = Nilai_Awal_Berat/3

kode_input = input('Masukkan Kode Gejala (Misal : G1,G3,G7,G8,G9)').split(',')

df['Nilai Gejala Ringan (T1)'] = pd.to_numeric(df['Nilai Gejala Ringan (T1)'], errors='coerce')

#inisialisasi total_nilai_ringan
total_nilai_ringan = 0
total_nilai_sedang = 0
total_nilai_berat = 0


# Mengambil nilai untuk setiap kode gejala yang dimasukkan
for kode in kode_input:
  kode = kode.strip() #menghilangkan spasi
  if kode in df['Kode Gejala'].values:
    nilai_gejala_ringan = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
    total_nilai_ringan += nilai_gejala_ringan
    print(f'Nilai Gejala Ringan T1 untuk {kode}: {nilai_gejala_ringan}')


  else:
    print(f'Kode gejala {kode} tidak ditemukan dalam dataset.')



# Mengambil nilai untuk setiap kode gejala yang dimasukkan
for kode in kode_input:
  kode = kode.strip() #menghilangkan spasi
  if kode in df['Kode Gejala'].values:
    nilai_gejala_sedang = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
    total_nilai_sedang += nilai_gejala_sedang
    print(f'Nilai Gejala Ringan T1 untuk {kode}: {nilai_gejala_sedang}')


  else:
    print(f'Kode gejala {kode} tidak ditemukan dalam dataset.')



# Mengambil nilai untuk setiap kode gejala yang dimasukkan
for kode in kode_input:
  kode = kode.strip() #menghilangkan spasi
  if kode in df['Kode Gejala'].values:
    nilai_gejala_berat = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
    total_nilai_berat += nilai_gejala_berat
    print(f'Nilai Gejala Berat (T3) untuk {kode}: {nilai_gejala_berat}')


  else:
    print(f'Kode gejala {kode} tidak ditemukan dalam dataset.')



# Menghitung prior x likelihood stress RINGAN
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
  stress = 'Ringan'
  print('Maka anda mengalami Stress Ringan')
elif posterior_sedang > posterior_berat:
  stress = 'Sedang'
  print('Maka anda mengalami Stress Sedang')
else:
  stress = 'Berat'
  print('Maka anda mengalami Stress Berat')



