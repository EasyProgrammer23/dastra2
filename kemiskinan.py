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

lottie_kemiskinan = load_lottiefile("media/kemiskinan.json") 

kemiskinan = pd.read_excel("Kemiskinan.xlsx")

col1,col2 = st.columns([1, 3], gap = "small", vertical_alignment="center")

with col1 :
    st_lottie(
    lottie_kemiskinan,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=150,
    width=200,
    key=None,
)
with col2 :
    st.title(f"Anda Memasuki Data Kemiskinan")

st.write("## Garis Kemiskinan")
st.write("Garis kemiskinan merupakan representasi dari jumlah rupiah minimum yangdibutuhkan untuk memenuhi kebutuhan pokok minimum makanan yang setara dengan2100 kilokalori per kapita per hari dan kebutuhan pokok bukan makanan. Gariskemiskinan (GK) merupakan penjumlahan dari Garis Kemiskinan Makanan (GKM)dan Garis Kemiskinan non Makanan (GKNM). Garis kemiskinan makanan merupakannilai pengeluaran kebutuhan minimum makanan yang disetarakan dengan 2100kilokalori per kapita per hari. Paket komoditi kebutuhan dasar makanan diwakili oleh52 jenis komoditi (padi- padian, umbi-umbian, ikan, daging, telur dan susu, sayuran,kacang- kacangan, buah-buahan, minyak, dll.). Garis kemiskinan non makanan adalahkebutuhan minimum untuk perumahan, sandang, Pendidikan, dan Kesehatan. Paketkomoditi kebutuhan dasar non makanan diwakili oleh 51 jenis komoditi di perkotaandan 47 jenis di perdesaan.")
# Pilihan kolom kemiskinan untuk divisualisasikan
min_year = kemiskinan["Tahun"].min()
max_year = kemiskinan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "GK"
)
# Filter data sesuai tahun
filter_kemiskinan = kemiskinan[(kemiskinan["Tahun"] >= start_year) & (kemiskinan["Tahun"] <= end_year)]
chart_GK= alt.Chart(filter_kemiskinan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("GK:Q", title="Persentase", scale=alt.Scale(zero=False))
).properties(
    title=f"Garis Kemiskinan dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_GK, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Garis kemiskinan menunjukkan jumlah rupiah minimum yang dibutuhkan untuk memenuhi kebutuhan pokok minimum makanan yang setara dengan 2100 kilokalori per kapita per hari dan kebutuhan pokok non makanan. Penduduk yang memiliki rata-rata pengeluaran konsumsi per kapita per bulan di bawah garis kemiskinan dikategorikan sebagai penduduk miskin.")
st.subheader("Sumber Data")
st.write("Susenas Modul Konsumsi dan Kor.")

st.write("## Persentase Penduduk Miskin")
st.write("Persentase penduduk miskin yang berada di bawah garis kemiskinan. Headcount index secara sederhana mengukur proporsi yang dikategorikan miskin.")
# Pilihan kolom kemiskinan untuk divisualisasikan
min_year = kemiskinan["Tahun"].min()
max_year = kemiskinan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "PPM"
)
# Filter data sesuai tahun
filter_kemiskinan = kemiskinan[(kemiskinan["Tahun"] >= start_year) & (kemiskinan["Tahun"] <= end_year)]
chart_GK= alt.Chart(filter_kemiskinan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("PersentaseKemiskinan:Q", title="Persentase", scale=alt.Scale(zero=False))
).properties(
    title=f"Persentase Penduduk Miskin dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_GK, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Angka yang ditunjukkan oleh P0 menunjukkan proporsi penduduk miskin di suatu wilayah. Persentase penduduk miskin (P0) yang tinggi menunjukkan bahwa tingkat kemiskinan di suatu wilayah juga tinggi.")
st.subheader("Sumber Data")
st.write("Survei Sosial Ekonomi Nasional (SUSENAS)")

st.write("## Indeks Kedalaman Kemiskinan")
st.write("Indeks kedalaman kemiskinan (Poverty Gap Index – P1) merupakan ukuran rata rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan.")
# Pilihan kolom kemiskinan untuk divisualisasikan
min_year = kemiskinan["Tahun"].min()
max_year = kemiskinan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "KedalamanKemiskinan"
)
# Filter data sesuai tahun
filter_kemiskinan = kemiskinan[(kemiskinan["Tahun"] >= start_year) & (kemiskinan["Tahun"] <= end_year)]
chart_GK= alt.Chart(filter_kemiskinan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("KedalamanKemiskinan:Q", title="Nilai", scale=alt.Scale(zero=False))
).properties(
    title=f"Kedalaman Miskin dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_GK, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Penurunan nilai indeks kedalaman kemiskinan mengindikasikan bahwa rata- rata pengeluaran penduduk miskin cenderung semakin mendekati garis kemiskinan dan ketimpangan pengeluaran penduduk miskin juga semakin menyempit.")
st.subheader("Sumber Data")
st.write("Survei Sosial Ekonomi Nasional (SUSENAS)")

st.write("## Indeks Keparahan Kemiskinan")
st.write("Indeks keparahan kemiskinan (Poverty Severity Index – P1) memberikan gambaran mengenai penyebaran pengeluaran di antara penduduk miskin.")
# Pilihan kolom kemiskinan untuk divisualisasikan
min_year = kemiskinan["Tahun"].min()
max_year = kemiskinan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "KeparahanKemiskinan"
)
# Filter data sesuai tahun
filter_kemiskinan = kemiskinan[(kemiskinan["Tahun"] >= start_year) & (kemiskinan["Tahun"] <= end_year)]
chart_GK= alt.Chart(filter_kemiskinan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("KeparahanKemiskinan:Q", title="Nilai", scale=alt.Scale(zero=False))
).properties(
    title=f"Keparahan Miskin dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_GK, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Semakin tinggi nilai indeks, semakin tinggi ketimpangan pengeluaran di antara penduduk miskin.")
st.subheader("Sumber Data")
st.write("Survei Sosial Ekonomi Nasional (SUSENAS)")