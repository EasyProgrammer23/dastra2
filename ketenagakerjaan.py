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

lottie_ketenagakerjaan = load_lottiefile("media/ketenagakerjaan.json") 

ketenagakerjaan = pd.read_excel("Ketenagakerjaan.xlsx")
col1,col2 = st.columns([1, 3], gap = "small", vertical_alignment="center")
with col1 :
    st_lottie(
    lottie_ketenagakerjaan,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=None,
    width=200,
    key=None,
)
with col2 :
    st.title("Anda Memasuki Data Ketenagakerjaan")
st.write("## Angkatan Kerja")
st.write("Angkatan Kerja adalah penduduk usia kerja (15 tahun ke atas) yang bekerja, atau punya pekerjaan namun sementara tidak bekerja, dan pengangguran. Sebaliknya, Bukan Angkatan Kerja adalah penduduk usia kerja (15 tahun ke atas) yang tidak bekerja karena bersekolah, mengurus rumah tangga, dan/atau melakukan kegiatan lainnya.")
# Pilihan kolom PDRB untuk divisualisasikan
min_year = ketenagakerjaan["Tahun"].min()
max_year = ketenagakerjaan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "angkt_kerja"
)
# Filter data sesuai tahun
filter_kerja = ketenagakerjaan[(ketenagakerjaan["Tahun"] >= start_year) & (ketenagakerjaan["Tahun"] <= end_year)]

    # Checkbox pilihan jenis kelamin
col1, col2, col3 = st.columns(3)
with col1:
    show_total = st.checkbox("Total", value=True)
with col2:
    show_lk = st.checkbox("Laki-laki", value=True)
with col3:
    show_pr = st.checkbox("Perempuan", value=True)
# Siapkan data untuk visualisasi
data_dict = {"Tahun": filter_kerja["Tahun"]}
if show_total:
    data_dict["Total"] = filter_kerja["Angkatan Kerja"]
if show_lk:
    data_dict["Laki-laki"] = filter_kerja.get(f"Angkatan Kerja LK", pd.Series([None]*len(filter_kerja)))
if show_pr:
    data_dict["Perempuan"] = filter_kerja.get(f"Angkatan Kerja PR", pd.Series([None]*len(filter_kerja)))

# Hanya lanjut jika ada yang dicentang
if len(data_dict) > 1:
    df_vis = pd.DataFrame(data_dict)
    df_melt = df_vis.melt(id_vars="Tahun", var_name="Kategori", value_name="Jumlah")

    # Visualisasi
    chart = alt.Chart(df_melt).mark_line(point=True).encode(
        x=alt.X("Tahun:O", title="Tahun"),
        y=alt.Y("Jumlah:Q", title="Jumlah", scale=alt.Scale(zero=False)),
        color=alt.Color("Kategori:N", title="Kategori")
    ).properties(
        title=f"Jumlah Angkatan Kerja berdasarkan Jenis Kelamin ({start_year}–{end_year})"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Pilih minimal satu kategori untuk ditampilkan.")

st.subheader("Contoh Intepretasi")
st.write("Semakin tinggi jumlah angkatan kerja berarti semakin banyak jumlah penduduk yang berpotensi untuk bekerja.")
st.subheader("Sumber Data")
st.write("Survei Angkatan Kerja Nasional (SAKERNAS), Survei Sosial Ekonomi Nasional (SUSENAS), SUPAS, dan Sensus Penduduk.")

st.write("## Tingkat Partisipasi Angkatan Kerja")
st.write("ersentase angkatan kerja terhadap penduduk usia kerja.")
# Pilihan kolom PDRB untuk divisualisasikan
min_year = ketenagakerjaan["Tahun"].min()
max_year = ketenagakerjaan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "tpak"
)

# Filter data sesuai tahun
filter_kerja = ketenagakerjaan[(ketenagakerjaan["Tahun"] >= start_year) & (ketenagakerjaan["Tahun"] <= end_year)]

    # Checkbox pilihan jenis kelamin
col1, col2, col3 = st.columns(3)
with col1:
    show_total = st.checkbox("Total", value=True, key="total_checkbox_3")
with col2:
    show_lk = st.checkbox("Laki-laki", value=True, key="lk_checkbox_3")
with col3:
    show_pr = st.checkbox("Perempuan", value=True, key="pr_checkbox_3")
# Siapkan data untuk visualisasi
data_dict = {"Tahun": filter_kerja["Tahun"]}
if show_total:
    data_dict["Total"] = filter_kerja["TPAK"]
if show_lk:
    data_dict["Laki-laki"] = filter_kerja.get(f"TPAK LK", pd.Series([None]*len(filter_kerja)))
if show_pr:
    data_dict["Perempuan"] = filter_kerja.get(f"TPAK PR", pd.Series([None]*len(filter_kerja)))

# Hanya lanjut jika ada yang dicentang
if len(data_dict) > 1:
    df_vis = pd.DataFrame(data_dict)
    df_melt = df_vis.melt(id_vars="Tahun", var_name="Kategori", value_name="Jumlah")

    # Visualisasi
    chart = alt.Chart(df_melt).mark_line(point=True).encode(
        x=alt.X("Tahun:O", title="Tahun"),
        y=alt.Y("Jumlah:Q", title="Jumlah", scale=alt.Scale(zero=False)),
        color=alt.Color("Kategori:N", title="Kategori")
    ).properties(
        title=f"Jumlah TPAK berdasarkan Jenis Kelamin ({start_year}–{end_year})"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Pilih minimal satu kategori untuk ditampilkan.")
    
st.subheader("Contoh Intepretasi")
st.write("Semakin tinggi TPAK menunjukkan bahwa semakin tinggi pula pasokan tenaga kerja (labor supply ) yang tersedia untuk memproduksi barang dan jasa dalam suatu perekonomian. Contoh: Jika TPAK sebesar 71.69 persen di Kab. Sanggau tahun 2024, maka dari 100 penduduk usia 15 tahun ke atas, terdapat sebanyak 71 hingga 72 orang tersedia untuk memproduksi pada periode tertentu di Kab. Sanggau tahun 2024.")
st.subheader("Sumber Data")
st.write("Survei Angkatan Kerja Nasional (SAKERNAS)")

st.write("## Tingkat Pengangguran Terbuka")
st.write("Persentase penduduk yang mencari pekerjaan, yang mempersiapkan usaha, yang tidak mencari pekerjaan karena merasa tidak mungkin pekerjaan, yang sudah mempunyai pekerjaan tetapi belum mulai bekerja dari sejumlah angkatan kerja yang ada.")
# Pilihan kolom PDRB untuk divisualisasikan
min_year = ketenagakerjaan["Tahun"].min()
max_year = ketenagakerjaan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "tpt"
)

# Filter data sesuai tahun
filter_kerja = ketenagakerjaan[(ketenagakerjaan["Tahun"] >= start_year) & (ketenagakerjaan["Tahun"] <= end_year)]

    # Checkbox pilihan jenis kelamin
col1, col2, col3 = st.columns(3)
with col1:
    show_total = st.checkbox("Total", value=True, key="total_checkbox_1")
with col2:
    show_lk = st.checkbox("Laki-laki", value=True, key="lk_checkbox_1")
with col3:
    show_pr = st.checkbox("Perempuan", value=True, key="pr_checkbox_1")
# Siapkan data untuk visualisasi
data_dict = {"Tahun": filter_kerja["Tahun"]}
if show_total:
    data_dict["Total"] = filter_kerja["TPT"]
if show_lk:
    data_dict["Laki-laki"] = filter_kerja.get(f"TPT LK", pd.Series([None]*len(filter_kerja)))
if show_pr:
    data_dict["Perempuan"] = filter_kerja.get(f"TPT PR", pd.Series([None]*len(filter_kerja)))

# Hanya lanjut jika ada yang dicentang
if len(data_dict) > 1:
    df_vis = pd.DataFrame(data_dict)
    df_melt = df_vis.melt(id_vars="Tahun", var_name="Kategori", value_name="Jumlah")

    # Visualisasi
    chart = alt.Chart(df_melt).mark_line(point=True).encode(
        x=alt.X("Tahun:O", title="Tahun"),
        y=alt.Y("Jumlah:Q", title="Jumlah", scale=alt.Scale(zero=False)),
        color=alt.Color("Kategori:N", title="Kategori")
    ).properties(
        title=f"Jumlah TPT berdasarkan Jenis Kelamin ({start_year}–{end_year})"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Pilih minimal satu kategori untuk ditampilkan.")
    
st.subheader("Contoh Intepretasi")
st.write("TPT yang tinggi menunjukkan bahwa terdapat banyak angkatan kerja yang tidak diserap pada pasar kerja. Misal: TPT Sanggau pada tahun 2024 adalah 3.71, artinya dari 100 penduduk usia 15 tahun ke atas yang tersedia untuk memproduksi barang dan jasa (angkatan kerja) terdapat 3 hingga 4 orang merupakan pengangguran")
st.subheader("Sumber Data")
st.write("Survei Angkatan Kerja Nasional (SAKERNAS), Survei Sosial Ekonomi Nasional (SUSENAS), dan Sensus Penduduk.")

st.write("## Tingkat Kesempatan Bekerja")
st.write("Peluang seorang penduduk usia kerja yang termasuk angkatan kerja untuk bekerja. ")
# Pilihan kolom ketenagakerjaan untuk divisualisasikan
min_year = ketenagakerjaan["Tahun"].min()
max_year = ketenagakerjaan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "TKK"
)

# Filter data sesuai tahun
filter_kerja = ketenagakerjaan[(ketenagakerjaan["Tahun"] >= start_year) & (ketenagakerjaan["Tahun"] <= end_year)]

        # Checkbox pilihan jenis kelamin
col1, col2, col3 = st.columns(3)
with col1:
    show_total = st.checkbox("Total", value=True, key="total_checkbox_2")
with col2:
    show_lk = st.checkbox("Laki-laki", value=True, key="lk_checkbox_2")
with col3:
    show_pr = st.checkbox("Perempuan", value=True, key="pr_checkbox_2")
# Siapkan data untuk visualisasi
data_dict = {"Tahun": filter_kerja["Tahun"]}
if show_total:
    data_dict["Total"] = filter_kerja["TKK"]
if show_lk:
    data_dict["Laki-laki"] = filter_kerja.get(f"TKK LK", pd.Series([None]*len(filter_kerja)))
if show_pr:
    data_dict["Perempuan"] = filter_kerja.get(f"TKK PR", pd.Series([None]*len(filter_kerja)))

# Hanya lanjut jika ada yang dicentang
if len(data_dict) > 1:
    df_vis = pd.DataFrame(data_dict)
    df_melt = df_vis.melt(id_vars="Tahun", var_name="Kategori", value_name="Jumlah")

    # Visualisasi
    chart = alt.Chart(df_melt).mark_line(point=True).encode(
        x=alt.X("Tahun:O", title="Tahun"),
        y=alt.Y("Jumlah:Q", title="Jumlah", scale=alt.Scale(zero=False)),
        color=alt.Color("Kategori:N", title="Kategori")
    ).properties(
        title=f"Jumlah TKK berdasarkan Jenis Kelamin ({start_year}–{end_year})"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Pilih minimal satu kategori untuk ditampilkan.")

st.subheader("Contoh Intepretasi")
st.write("Peluang seseorang yang termasuk dalam angkatan kerja untuk dapat terserap dalam pasar kerja atau dapat bekerja. Semakin besar RK, maka semakin baik pula kondisi ketenagakerjaan dalam suatu wilayah.")
st.subheader("Sumber Data")
st.write("Sakernas, Susenas, dan Sensus Penduduk ")

st.write("## Rasio Ketergantungan")
st.write("Rasio ketergantungan (depandency ratio) adalah perbandingan antara jumlah penduduk umur 0-14 tahun ditambah dengan penduduk umur 65 tahun ke atas (keduanya disebut sebagai bukan angkatan kerja) dibandingkan dengan jumlah penduduk umur 15-64 tahun (angkatan kerja).")
# Pilihan kolom ketenagakerjaan untuk divisualisasikan
min_year = ketenagakerjaan["Tahun"].min()
max_year = ketenagakerjaan["Tahun"].max()
start_year, end_year = st.slider(
    "Pilih rentang tahun:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1,
    key = "tkk"
)

# Filter data sesuai tahun
filter_kerja = ketenagakerjaan[(ketenagakerjaan["Tahun"] >= start_year) & (ketenagakerjaan["Tahun"] <= end_year)]
chart_RK= alt.Chart(filter_kerja).mark_line(point=True).encode(
    x= alt.X("Tahun:O", title="Tahun"),
    y= alt.Y("RK:Q", title="Jumlah", scale=alt.Scale(zero=False))
).properties(
    title=f"RK dari {start_year} hingga {end_year}"
)
st.altair_chart(chart_RK, use_container_width=True)
st.subheader("Contoh Intepretasi")
st.write("   Rasio ketergantungan merupakan salah satu indikator yang penting. Rasio ketergantungan menunjukkan tingginya beban yang harus ditanggung penduduk yang produktif untuk membiayai hidup penduduk yang belum produktif dan penduduk yang sudah tidak produktif lagi. Misalnya terdapat rasio ketergantungan sebesar 43 persen sanggau pada tahun 2024, artinya setiap 100 orang yang berusia produktif di sanggau pada tahun 2024 mempunyai tanggungan sebanyak 43 orang yang tidak produktif.")
st.subheader("Sumber Data")
st.write("SUPAS dan Sensus Penduduk ")