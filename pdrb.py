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

lottie_pdrb = load_lottiefile("media/pdrb.json") 
pdrb = pd.read_excel('PDRB.xlsx')
adhk_Lapus = pd.read_excel("ADHK_Lapus.xlsx")
adhb_Lapus = pd.read_excel("ADHB_Lapus.xlsx")
col3,col4 = st.columns([3, 1], gap = "small", vertical_alignment="top")
col1,col2 = st.columns([1, 3], gap = "small", vertical_alignment="top")

with col1 :
    st_lottie(
    lottie_pdrb,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=None,
    width=200,
    key=None,
)
with col2 :
    st.title(f"Anda Memasuki Data PDRB")

st.write("## PDRB")
st.write("Nilai keseluruhan semua barang dan jasa yang diproduksi dalam suatu wilayah  dalam suatu jangka waktu tertentu (biasanya satu tahun). PDRB terbagi menjadi dua  jenis, yaitu PDRB atas dasar harga berlaku (nominal) dan PDRB atas dasar harga  konstan (riil). PDRB atas dasar harga konstan digunakan untuk mengetahui  pertumbuhan ekonomi dari tahun ke tahun, sedangkan PDRB atas dasar harga berlaku  digunakan untuk menunjukkan kemampuan sumber daya ekonomi yang dihasilkan  suatu wilayah. ")
# Pilihan kolom PDRB untuk divisualisasikan
pdrb_option = st.selectbox("Pilih jenis PDRB untuk divisualisasikan:", ["PDRB ADHB", "PDRB ADHK"])

min_year = pdrb["Tahun"].min()
max_year = pdrb["Tahun"].max()

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Filter data sesuai tahun
filter_pdrb = pdrb[(pdrb["Tahun"] >= start_year) & (pdrb["Tahun"] <= end_year)]
# Chart
chart_pdrb = alt.Chart(filter_pdrb).mark_line(point=True).encode(
    x='Tahun:O',
    y=alt.Y(pdrb_option, title="PDRB", scale=alt.Scale(zero=False))
).properties(
    title=f"{pdrb_option} dari {start_year} hingga {end_year} dalam juta"
)
st.altair_chart(chart_pdrb, use_container_width=True)

if pdrb_option == "PDRB ADHB":
    pdrb_lapus = adhb_Lapus
else:
    pdrb_lapus = adhk_Lapus

selected_year = st.selectbox("Pilih Tahun", pdrb_lapus['Tahun'])
row = pdrb_lapus.loc[pdrb_lapus['Tahun'] == selected_year].iloc[0]
sektor_data = {
    'Pertanian, Kehutanan, dan Perikanan': row['Pertanian, Kehutanan, dan Perikanan'],
    'Pertambangan dan Penggalian ': row['Pertambangan dan Penggalian '],
    'Industri Pengolahan': row['Industri Pengolahan'],
    'Pengadaan Listrik dan Gas': row['Pengadaan Listrik dan Gas'],
    'Pengadaan Air, Pengelolaan Sampah, Limbah dan Daur Ulang': row['Pengadaan Air, Pengelolaan Sampah, Limbah dan Daur Ulang'],
    'Konstruksi': row['Konstruksi'],
    'Perdagangan Besar dan Eceran; Reparasi Mobil dan Sepeda Motor': row['Perdagangan Besar dan Eceran; Reparasi Mobil dan Sepeda Motor'],
    'Transportasi dan Pergudangan ': row['Transportasi dan Pergudangan '],
    'Penyediaan Akomodasi dan Makan Minum': row['Penyediaan Akomodasi dan Makan Minum'],
    'Informasi dan Komunikasi': row['Informasi dan Komunikasi'],
    'Jasa Keuangan dan Asuransi': row['Jasa Keuangan dan Asuransi'],
    'Real Estate': row['Real Estate'],
    'Jasa perusahaan': row['Jasa perusahaan'],
    'Administrasi pemerintahan, pertahanan, dan Jaminan sosial wajib': row['Administrasi pemerintahan, pertahanan, dan Jaminan sosial wajib'],
    'Jasa Pendidikan': row['Jasa Pendidikan'],
    'Jasa Kesehatan dan Kegiatan Sosial': row['Jasa Kesehatan dan Kegiatan Sosial'],
    'Jasa Lainnya': row['Jasa Lainnya']
}
st.bar_chart(sektor_data) 
    
st.subheader("Contoh Intepretasi")
st.write("Misalnya pada tahun 2024 diketahui PDRB Kabupaten Sanggau sebesar 26.523.743.32 juta rupiah, artinya jumlah barang dan jasa yang dihasilkan di Kabupaten Sanggau pada tahun  2024 adalah 26.523.743.32 juta rupiah.")
st.subheader("Sumber Data")
st.write("Susenas; Dokumen Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang(PIB) yang diterima BPS dari kantor Bea Cukai; Data sayur- sayuran dan buah-buahandiperoleh dari Dinas Pertanian; data produksi tanaman perkebunan besar dari BPS, dataproduksi perkebunan rakyat dari Dinas Pertanian; Laporan Tahunan Pertambangan Energi,Departemen Energi dan Sumber Daya Mineral, Survei Tahunan Industri Besar Sedang,Laporan Tahunan Pertambangan Migas dan Pertamina; PN Gas, dan PDAM; LaporanKeuangan perusahaan, dll.")
st.write("## PDRB Per Kapita")
st.write("Merupakan nilai PDRB dibagi jumlah penduduk dalam suatu wilayah per periode  tertentu.")
# Pilihan kolom PDRB untuk divisualisasikan
pdrb_option2 = st.selectbox("Pilih jenis PDRB untuk divisualisasikan:", ["PDRB ADHB Per Kapita", "PDRB ADHK Per Kapita" ])

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "pdrb_kapita"
)

# Filter data sesuai tahun
filter_pdrb = pdrb[(pdrb["Tahun"] >= start_year) & (pdrb["Tahun"] <= end_year)]

# Chart
chart_pdrb = alt.Chart(filter_pdrb).mark_line(point=True).encode(
    x='Tahun:O',
    y=alt.Y(pdrb_option2, title="PDRB per Kapita", scale=alt.Scale(zero=False))
).properties(
    title=f"{pdrb_option2} dari {start_year} hingga {end_year}  dalam juta"
)

st.altair_chart(chart_pdrb, use_container_width=True)

st.subheader("Contoh Intepretasi")
st.write("Saat ini PDRB per kapita Kabupaten Sanggau sudah mencapai 51,96 juta rupiah. Nilai PDRB  per kapita tersebut dapat diartikan bahwa dalam setahun pendapatan tiap penduduk  Kabupaten Sanggau secara rata-rata sudah mencapai 51,96 juta.")
st.subheader("Sumber Data")
st.write("Susenas; Dokumen Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang(PIB) yang diterima BPS dari kantor Bea Cukai; Data sayur- sayuran dan buah-buahandiperoleh dari Dinas Pertanian; data produksi tanaman perkebunan besar dari BPS, dataproduksi perkebunan rakyat dari Dinas Pertanian; Laporan Tahunan Pertambangan Energi,Departemen Energi dan Sumber Daya Mineral, Survei Tahunan Industri Besar Sedang,Laporan Tahunan Pertambangan Migas dan Pertamina; PN Gas, dan PDAM; LaporanKeuangan perusahaan, dll.")
        
st.write("## Laju Pertumbuhan PDRB")
st.write("Menunjukkan pertumbuhan produksi barang dan jasa di suatu wilayah perekonomian dalam selang waktu tertentu. Penghitungan pertumbuhan ekonomi menggunakan PDRB atas dasar harga konstan dengan tahun dasar tertentu untuk mengeliminasi faktor kenaikan harga.")

start_year, end_year, = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key="slider_laju"
)

# Filter data sesuai tahun
filter_pdrb= pdrb[(pdrb["Tahun"] >= start_year) & (pdrb["Tahun"] <= end_year)]

chart_pdrb= alt.Chart(filter_pdrb).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("Laju PDRB:Q", title="Laju PDRB", scale=alt.Scale(zero=False))
).properties(
    title=f"{pdrb_option} dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_pdrb, use_container_width=True)

st.subheader("Contoh Intepretasi")
st.write("Pertumbuhan ekonomi menunjukkan pertumbuhan produksi barang dan jasa di suatu wilayah perekonomian dalam selang waktu tertentu. Semakin tinggi pertumbuhan ekonomi suatu wilayah menandakan semakin bergairahnya perekonomian di wilayah tersebut. Dengan asumsi pertumbuhan ekonomi yang tinggi akan menyerap tenaga kerja yang tinggi pula, yang pada hakikatnya meningkatkan pendapatan dan daya beli masyarakat.")
st.subheader("Sumber Data")
st.write("Susenas; Dokumen Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang(PIB) yang diterima BPS dari kantor Bea Cukai; Data sayur- sayuran dan buah-buahandiperoleh dari Dinas Pertanian; data produksi tanaman perkebunan besar dari BPS, dataproduksi perkebunan rakyat dari Dinas Pertanian; Laporan Tahunan Pertambangan Energi,Departemen Energi dan Sumber Daya Mineral, Survei Tahunan Industri Besar Sedang,Laporan Tahunan Pertambangan Migas dan Pertamina; PN Gas, dan PDAM; LaporanKeuangan perusahaan, dll.")

st.write("## Indeks Implisit PDRB")
st.write("Suatu indeks yang menunjukkan tingkat perkembangan harga di tingkat produsen (producer price index).")

start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key="slider_imp"
)

# Filter data sesuai tahun
filter_pdrb = pdrb[(pdrb["Tahun"] >= start_year) & (pdrb["Tahun"] <= end_year)]

chart_pdrb= alt.Chart(filter_pdrb).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("Indeks Implisit:Q", title="Indeks Implisit", scale=alt.Scale(zero=False))
).properties(
    title=f"{pdrb_option} dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_pdrb, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("Besarnya indeks implisit menunjukkan perubahan harga produsen sebesar (100 dikurangi besarnya indeks implisit) dibandingkan harga produsen pada tahun dasar (2010). Laju Indeks Implisit Kabupaten Sanggau pada tahun 2019 mencapai 2,03.")
st.subheader("Sumber Data")
st.write("Susenas; Dokumen Pemberitahuan Ekspor Barang (PEB) dan Pemberitahuan Impor Barang(PIB) yang diterima BPS dari kantor Bea Cukai; Data sayur- sayuran dan buah-buahandiperoleh dari Dinas Pertanian; data produksi tanaman perkebunan besar dari BPS, dataproduksi perkebunan rakyat dari Dinas Pertanian; Laporan Tahunan Pertambangan Energi,Departemen Energi dan Sumber Daya Mineral, Survei Tahunan Industri Besar Sedang,Laporan Tahunan Pertambangan Migas dan Pertamina; PN Gas, dan PDAM; LaporanKeuangan perusahaan, dll.")


    