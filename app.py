import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(page_title="JEWEL MAVEN PVT LTD", layout="wide")

# ---------------- DATA LOAD ----------------
INVENTORY = pd.read_excel("INVENTORY DATA.xlsx", sheet_name="INVENTORY")
SALES_DATA = pd.read_excel("INVENTORY DATA.xlsx", sheet_name="SALE")
SILVERCOSTING_DATA = pd.read_excel("INVENTORY DATA.xlsx", sheet_name="SILVER")
GOLDCOSTING_DATA = pd.read_excel("INVENTORY DATA.xlsx", sheet_name="GOLD")

LOGO_PATH = "C:/Users/Subun Sahu/Downloads/PDF/logo.png"

# ---------------- HEADER ----------------
st.image(LOGO_PATH, width=150)
st.title("JEWEL MAVEN PVT LTD")

# ---------------- SIDEBAR ----------------
if st.sidebar.button("INVENTORY"):
    st.subheader("INVENTORY DATA")
    st.dataframe(INVENTORY)

    st.subheader("CATEGORY WISE SUMMARY")
    st.dataframe(
        INVENTORY.pivot_table(
            index="DESP",
            values=["GR.WT IN GMS", "GOLD  WT IN GMS", "DIA WT IN CTS", "NO OF PCS", "TAG"],
            aggfunc=np.sum,
            sort=False
        )
    )
    st.subheader("FLOOR WISE SUMMARY")
    st.dataframe(
        INVENTORY.pivot_table(
            index="FLOOR",
            values=["GR.WT IN GMS", "GOLD  WT IN GMS", "DIA WT IN CTS", "NO OF PCS", "TAG"],
            aggfunc=np.sum,
            sort=False
        )
    )

if st.sidebar.button("SALES"):
    st.subheader("SALES DATA")
    st.data_editor(SALES_DATA)

if st.sidebar.button("SILVER COSTING"):
    st.subheader("SILVER COSTING DATA")
    st.dataframe(SILVERCOSTING_DATA)

if st.sidebar.button("GOLD COSTING"):
    st.subheader("GOLD COSTING DATA")
    st.dataframe(GOLDCOSTING_DATA)