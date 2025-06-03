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

lottie_pmanusia = load_lottiefile("media/pmanusia.json") 

PManusia = pd.read_excel("PembangunanManusia.xlsx")

col1,col2 = st.columns([1, 3], gap = "small", vertical_alignment="center")

with col1 :
    st_lottie(
    lottie_pmanusia,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=None,
    width=200,
    key=None,
)
with col2 :
    st.header("Anda Memasuki Data Pembangunan Manusia")

st.write("## Angka Harapan Hidup")
st.write("Rata-rata tahun hidup yang masih akan dijalani oleh seseorang yang telah berhasil mencapai umur x, pada suatu tahun tertentu dalam situasi mortalitas yang berlaku di lingkungan masyarakat. Penggunaan AHH didasarkan atas pertimbangan bahwa angka ini merupakan hasil dari berbagai indikator kesehatan. AHH merupakan cerminan dari ketersediaan sarana dan prasarana kesehatan, sanitasi lingkungan, pengetahuan ibu tentang kesehatan, gaya hidup masyarakat, pemenuhan gizi ibu dan bayi, dan lain- lain.")
# Pilihan kolom PDRB untuk divisualisasikan
min_year = PManusia["Tahun"].min()
max_year = PManusia["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "AHH"
)
# Filter data sesuai tahun
filter_pembangunan = PManusia[(PManusia["Tahun"] >= start_year) & (PManusia["Tahun"] <= end_year)]
chart_AHH= alt.Chart(filter_pembangunan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("AHH:Q", title="Tahun", scale=alt.Scale(zero=False)),
    tooltip=["Tahun:O", "AHH:Q"] 
).properties(
    title=f"Angka Harapan Hidup dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_AHH, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Angka harapan hidup menggambarkan rata-rata tahun hidup yang dijalani oleh seseorang. Misalnya angka harapan hidup Indonesia yang terhitung untuk Indonesia dari Sensus Penduduk tahun 1971 adalah 47,7 tahun, artinya bayi-bayi yang dilahirkan menjelang tahun 1971 akan dapat hidup sampai 47 sampai 48 tahun.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk, Registrasi Penduduk, Survei Penduduk Antar Sensus (SUPAS), Survei Sosial Ekonomi Nasional (Susenas).")

st.write("## Rata-rata Lama Sekolah")
st.write("Rata-rata lama sekolah (Mean Years School/MYS) adalah jumlah tahun yang digunakan oleh penduduk dalam menjalani pendudukan formal. Diasumsikan bahwa dalam kondisi normal rata-rata lama sekolah suatu wilayah tidak akan turun. Cakupan penduduk yang dihitung dalam penghitungan rata-rata lama sekolah adalah penduduk berusia 25 tahun ke atas.")
# Pilihan kolom PManusia untuk divisualisasikan
min_year = PManusia["Tahun"].min()
max_year = PManusia["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "RLS"
)
# Filter data sesuai tahun
filter_pembangunan = PManusia[(PManusia["Tahun"] >= start_year) & (PManusia["Tahun"] <= end_year)]
chart_RLS= alt.Chart(filter_pembangunan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("RLS:Q", title="Tahun", scale=alt.Scale(zero=False)),
    tooltip=["Tahun:O", "RLS:Q"] 
).properties(
    title=f"Rata-rata lama sekolah dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_RLS, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Tingginya angka Rata-rata lama sekolah menunjukkan jenjang Pendidikan yang pernah/sedang diduduki oleh seseorang. Semakin tinggi angka RLS maka semakin lama/tinggi jenjang Pendidikan yang ditamatkannya.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk, Survei Penduduk Antar Sensus (SUPAS), Survei Sosial Ekonomi Nasional (SUSENAS).")

st.write("## Harapan Lama Sekolah")
st.write("Angka Harapan Lama Sekolah (HLS) dihitung pada penduduk berusia 7 tahun ke atas. HLS dihitung pada usia 7 tahun ke atas karena mengikuti kebijakan pemerintah yaitu program wajib belajar. Diasumsikan bahwa peluang anak tersebut akan tetap bersekolah pada umur-umur berikutnya sama dengan peluang penduduk yang bersekolah per jumlah penduduk untuk umur yang sama saat ini.")
# Pilihan kolom PManusia untuk divisualisasikan
min_year = PManusia["Tahun"].min()
max_year = PManusia["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "HLS"
)
# Filter data sesuai tahun
filter_pembangunan = PManusia[(PManusia["Tahun"] >= start_year) & (PManusia["Tahun"] <= end_year)]
chart_HLS= alt.Chart(filter_pembangunan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("HLS:Q", title="Tahun", scale=alt.Scale(zero=False)),
    tooltip=["Tahun:O", "HLS:Q"] 
).properties(
    title=f"Harapan lama sekolah dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_HLS, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Tingginya angka harapan lama sekolah (HLS) menunjukkan lamanya sekolah yang diharapkan oleh anak pada umur tertentu di masa mendatang. Semakin tinggi angka HLS maka semakin lama/tinggi jenjang Pendidikan yang diharapkan akan ditamatkannya.")
st.subheader("Sumber Data")
st.write("Sensus Penduduk, Survei Penduduk Antar Sensus (SUPAS), Survei Sosial Ekonomi Nasional (SUSENAS), Direktorat Pendidikan Islam Kemenag.")

st.write("## Rata-rata Pengeluaran Per Kapita yang Disesuaikan")
st.write("Rata-rata pengeluaran per kapita yang disesuaikan (Purchasing Power Parity/PPP) atau daya beli adalah kemampuan masyarakat dalam membelanjakan uangnya dalam bentuk barang maupun jasa. Penghitungan paritas daya beli menggunakan 96komoditas dimana 66 komoditas merupakan makanan dan 30 komoditas merupakan komoditas non makanan.")
# Pilihan kolom PManusia untuk divisualisasikan
min_year = PManusia["Tahun"].min()
max_year = PManusia["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "RPP"
)
# Filter data sesuai tahun
filter_pembangunan = PManusia[(PManusia["Tahun"] >= start_year) & (PManusia["Tahun"] <= end_year)]
chart_RPP= alt.Chart(filter_pembangunan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("RatarataPengeluaran:Q", title="juta Rp/Thn", scale=alt.Scale(zero=False)),
    tooltip=["Tahun:O", "RatarataPengeluaran:Q"] 
).properties(
    title=f"Rata-rata pengeluaran per kapita yang disesuaikan dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_RPP, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Kemampuan daya beli antar daerah berbeda-beda. Semakin rendahnya nilai daya beli suatu masyarakat berkaitan erat dengan kondisi perekonomian pada saat itu yang sedang memburuk yang berarti semakin rendah kemampuan masyarakat untuk membeli suatu barang atau jasa.")
st.subheader("Sumber Data")
st.write("Survei Sosial Ekonomi Nasional (SUSENAS)")

st.write("## Indeks Pembangunan Manusia ")
st.write("IPM adalah indeks yang mengukur pembangunan manusia dari tiga aspek dasar yaitu umur Panjang dan hidup sehat; pengetahuan/Pendidikan; dan standar hidup layak. Ketiga aspek tersebut memiliki pengertian yang sangat luas karena merupakan gabungan dari berbagai faktor. Untuk mengukur dimensi Kesehatan, digunakan angka harapan hidup waktu lahir. Selanjutnya untuk mengukur dimensi Pendidikan digunakan gabungan indikator rata-rata lama sekolah dan angka harapan lama sekolah. Adapun untuk mengukur dimensi hidup layak digunakan indikator kemampuan daya beli masyarakat terhadap sejumlah kebutuhan pokok yang dilihat dari rata-rata besarnya pengeluaran per kapita.")
# Pilihan kolom PManusia untuk divisualisasikan
min_year = PManusia["Tahun"].min()
max_year = PManusia["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "IPM"
)
# Filter data sesuai tahun
filter_pembangunan = PManusia[(PManusia["Tahun"] >= start_year) & (PManusia["Tahun"] <= end_year)]
chart_IPM= alt.Chart(filter_pembangunan).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("IPM:Q", title="Poin", scale=alt.Scale(zero=False)),
    tooltip=["Tahun:O", "IPM:Q"] 
).properties(
    title=f"Indeks Pembangunan Manusia dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_IPM, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Angka IPM memberikan gambaran komprehensif mengenai tingkat pencapaian pembangunan manusia sebagai dampak dari kegiatan pembangunan yang dilakukan oleh suatu negara/daerah. Semakin tinggi nilai IPM suatu negara/daerah, menunjukkan pencapaian pembangunan manusianya semakin baik.")
st.subheader("Sumber Data")
st.write("Survei Sosial Ekonomi Nasional (SUSENAS) dan Survei Angkatan Kerja Nasional (SAKERNAS) ")
