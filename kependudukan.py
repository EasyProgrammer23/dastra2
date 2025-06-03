import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import altair as alt
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_kependudukan = load_lottiefile("media/kependudukan.json") 
Kependudukan = pd.read_excel('Kependudukan.xlsx')

col1,col2 = st.columns([1, 3], gap = "small", vertical_alignment="center")

with col1 :
    st_lottie(
    lottie_kependudukan,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=180,
    width=200,
    key=None,
)
with col2 :
    st.title(f"Anda Memasuki Data Kependudukan")

st.write("## Penduduk")
st.write("Penduduk adalah semua orang yang berdomisili di wilayah yang bersangkutan selama 6 bulan atau lebih dan atau mereka yang berdomisili kurang dari 6 bulan tetapi bertujuan untuk menetap")
# Pilihan kolom PDRB untuk divisualisasikan
penduduk_option2 = st.selectbox("Pilih jumlah Penduduk yang ingin divisualisasikan:", ["Sanggau", "Toba", "Meliau", "Kapuas", "Mukok", "Jangkang", "Bonti", "Parindu", "Tayan Hilir", "Balai", "Tayan Hulu", "Kembayan", "Beduai", "Noyan", "Sekayam", "Entikong"],key="penduduk_select_1")

min_year = Kependudukan["Tahun"].min()
max_year = Kependudukan["Tahun"].max()

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "jlh_pndk"
)

# Filter data sesuai tahun
filter_penduduk = Kependudukan[(Kependudukan["Tahun"] >= start_year) & (Kependudukan["Tahun"] <= end_year)]

# Checkbox pilihan jenis kelamin
col1, col2, col3 = st.columns(3)
with col1:
    show_total = st.checkbox("Total", value=True)
with col2:
    show_lk = st.checkbox("Laki-laki", value=True)
with col3:
    show_pr = st.checkbox("Perempuan", value=True)

# Siapkan data untuk visualisasi
data_dict = {"Tahun": filter_penduduk["Tahun"]}
if show_total:
    data_dict["Total"] = filter_penduduk[penduduk_option2]
if show_lk:
    data_dict["Laki-laki"] = filter_penduduk.get(f"{penduduk_option2} LK", pd.Series([None]*len(filter_penduduk)))
if show_pr:
    data_dict["Perempuan"] = filter_penduduk.get(f"{penduduk_option2} PR", pd.Series([None]*len(filter_penduduk)))

# Hanya lanjut jika ada yang dicentang
if len(data_dict) > 1:
    df_vis = pd.DataFrame(data_dict)
    df_melt = df_vis.melt(id_vars="Tahun", var_name="Kategori", value_name="Jumlah")

    # Visualisasi
    chart = alt.Chart(df_melt).mark_line(point=True).encode(
        x=alt.X("Tahun:O", title="Tahun"),
        y=alt.Y("Jumlah:Q", title="Jumlah Penduduk", scale=alt.Scale(zero=False)),
        color=alt.Color("Kategori:N", title="Kategori")
    ).properties(
        title=f"Jumlah Penduduk {penduduk_option2} berdasarkan Jenis Kelamin ({start_year}–{end_year})"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Pilih minimal satu kategori untuk ditampilkan.")
    
st.subheader("Contoh Intepretasi")
st.write("Semakin tinggi jumlah penduduk maka semakin banyak penduduk yang mendiami suatu wilayah.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk, Survei Penduduk Antar Sensus (SUPAS), dan Perhitungan Proyeksi Penduduk.")

st.write("## Kepadatan Penduduk")
st.write("Kepadatan penduduk kasar merupakan ukuran kepadatan penduduk yang umum digunakan, karena data dan perhitungannya sederhana, juga ukuran ini sudah distandardisasi dengan luas wilayah. Kepadatan penduduk kasar (Crude population density), yaitu menunjukkan banyaknya jumlah penduduk untuk setiap kilometer persegi luas wilayah.")
# Pilihan kolom PDRB untuk divisualisasikan
penduduk_option2 = st.selectbox("Pilih jumlah Penduduk yang ingin divisualisasikan:", ["Sanggau", "Toba", "Meliau", "Kapuas", "Mukok", "Jangkang", "Bonti", "Parindu", "Tayan Hilir", "Balai", "Tayan Hulu", "Kembayan", "Beduai", "Noyan", "Sekayam", "Entikong"],key="penduduk_select_2")

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "kepadatan_pndk"
)

# Filter data sesuai tahun
filter_penduduk = Kependudukan[(Kependudukan["Tahun"] >= start_year) & (Kependudukan["Tahun"] <= end_year)]

# Chart
chart_kepadatan = alt.Chart(filter_penduduk ).mark_line(point=True).encode(
    x='Tahun:O',
    y=alt.Y(penduduk_option2 + " Kepadatan", title="Kepadatan Penduduk", scale=alt.Scale(zero=False))
).properties(
    title=f"{penduduk_option2} dari {start_year} hingga {end_year}"
)

st.altair_chart(chart_kepadatan , use_container_width=True)

st.subheader("Contoh Intepretasi")
st.write("Angka kepadatan penduduk menunjukkan rata-rata jumlah penduduk tiap 1 kilo meter  persegi. Semakin besar angka kepadatan penduduk menunjukkan bahwa semakin padat  penduduk yang mendiami wilayah tersebut. Misalnya kepadatan penduduk Kabupaten  Sanggau tahun 2024 sebesar 44, hal tersebut dapat diinterpretasikan bahwa secara rata-rata  terdapat 44 penduduk setiap 1 kilometer persegi.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk, Survei Penduduk Antar Sensus (SUPAS), dan Perhitungan Proyeksi Penduduk.")
        
st.write("## Laju Pertumbuhan Penduduk")
st.write("Angka yang menunjukkan tingkat pertumbuhan penduduk per tahun dalam jangka waktu tertentu. Angka ini dinyatakan sebagai persentase dari penduduk dasar. Laju pertumbuhan penduduk dapat dihitung menggunakan tiga metode, yaitu aritmatik, geometrik, dan eksponensial. Metode yang digunakan di BPS adalah metode geometrik.")
# Pilihan kolom PDRB untuk divisualisasikan
penduduk_option2 = st.selectbox("Pilih jumlah Penduduk yang ingin divisualisasikan:", ["Sanggau", "Toba", "Meliau", "Kapuas", "Mukok", "Jangkang", "Bonti", "Parindu", "Tayan Hilir", "Balai", "Tayan Hulu", "Kembayan", "Beduai", "Noyan", "Sekayam", "Entikong"],key="penduduk_select_3")

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "laju_pndk"
)

# Filter data sesuai tahun
filter_penduduk = Kependudukan[(Kependudukan["Tahun"] >= start_year) & (Kependudukan["Tahun"] <= end_year)]

# Chart
chart_laju= alt.Chart(filter_penduduk ).mark_line(point=True).encode(
    x='Tahun:O',
    y=alt.Y(penduduk_option2 + " LPP", title="Laju Pertumbuhan", scale=alt.Scale(zero=False))
).properties(
    title=f"{penduduk_option2} dari {start_year} hingga {end_year}"
)

st.altair_chart(chart_laju , use_container_width=True)

st.subheader("Contoh Intepretasi")
st.write("a.r > 0, artinya terjadi penambahan jumlah penduduk pada tahun t dibandingkan tahun awal sebanyak r persen.")
st.write(" b. r = 0, artinya tidak terjadi perubahan jumlah penduduk pada tahun t dibandingkan tahun awal.")
st.write("c. r < 0, artinya terjadi pengurangan jumlah penduduk pada tahun t dibandingkan dengan tahun awal sebanyak mutlak r persen.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk & Survei Penduduk Antar Sensus (SUPAS) ")

st.write("## Rasio Jenis Kelamin")
st.write("Rasio jenis kelamin adalah perbandingan antara jumlah penduduk laki-laki dan jumlah penduduk perempuan pada suatu daerah dan pada waktu tertentu, yang biasanya dinyatakan dalam banyaknya penduduk laki-laki per 100 penduduk perempuan.")
# Pilihan kolom PDRB untuk divisualisasikan
penduduk_option2 = st.selectbox("Pilih jumlah Penduduk yang ingin divisualisasikan:", ["Sanggau", "Toba", "Meliau", "Kapuas", "Mukok", "Jangkang", "Bonti", "Parindu", "Tayan Hilir", "Balai", "Tayan Hulu", "Kembayan", "Beduai", "Noyan", "Sekayam", "Entikong"],key="penduduk_select_4")

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "rjk_pndk"
)
# Filter data sesuai tahun
filter_penduduk = Kependudukan[(Kependudukan["Tahun"] >= start_year) & (Kependudukan["Tahun"] <= end_year)]

# Chart
chart_Rasiojk= alt.Chart(filter_penduduk ).mark_line(point=True).encode(
    x='Tahun:O',
    y=alt.Y(penduduk_option2 + " RJK", title="Rasio", scale=alt.Scale(zero=False))
).properties(
    title=f"{penduduk_option2} dari {start_year} hingga {end_year}"
)

st.altair_chart(chart_Rasiojk , use_container_width=True)

st.subheader("Contoh Intepretasi")
st.write("a. 𝑆𝑅 > 0, artinya jumlah penduduk laki-laki lebih banyak dibandingkan jumlah penduduk perempuan sebanyak SR kali penduduk perempuan.")
st.write(" b. 𝑆𝑅 = 0, artinya jumlah penduduk laki-laki sama dengan jumlah penduduk perempuan. ")
st.write("c. 𝑆𝑅 < 0, artinya jumlah penduduk perempuan lebih banyak dibandingkan jumlah penduduk laki-laki sebanyak (1-SR) kali penduduk perempuan.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk & Survei Penduduk Antar Sensus (SUPAS)")