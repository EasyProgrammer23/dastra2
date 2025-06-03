import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import altair as alt
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
Pdrb= st.Page(
    page="pdrb.py",
    title="Produk Domestik Regional Bruto",
    icon=":material/bar_chart:"
)
Ketenagakerjaan = st.Page(
    page="ketenagakerjaan.py",
    title="Ketenagakerjaan",
    icon=":material/engineering:"
)
Kependudukan = st.Page(
    page="kependudukan.py",
    title="Kependudukan",
    icon=":material/groups:"
)
Kemiskinan = st.Page(
    page="kemiskinan.py",
    title="Kemiskinan",
    icon=":material/sick:"
)
PManusia = st.Page(
    page="PembangunanManusia.py",
    title="Pembangunan Manusia",
    icon=":material/diversity_3:"
)
menu = st.navigation(
    {
        "Data Strategis" : [Pdrb, Kependudukan, Ketenagakerjaan, Kemiskinan, PManusia]
    }
)
st.logo("media/2_2.png")
st.sidebar.image("media/logo_bps.svg")
menu.run()

