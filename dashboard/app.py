import streamlit as st
import pandas as pd
import psycopg2

st.title("Global Data Dashboard")

st.write("API Data Visualization")

from backend.queries import get_crypto_data

st.title("Global Data Dashboard")

data = get_crypto_data()

df = pd.DataFrame(data, columns=["id", "price", "timestamp"])

st.subheader("Bitcoin Price")

st.line_chart(df["price"])