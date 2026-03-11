import streamlit as st
import pandas as pd
import psycopg2
import sys


sys.path.insert(1, '../backend')

from backend.models import create_tables

create_tables()


st.title("Global Data Dashboard")

#st.write("API Data Visualization")

from backend.queries import get_crypto_data

st.write("test")

data = get_crypto_data()

df = pd.DataFrame(data, columns=["id", "price", "timestamp"])

st.subheader("Bitcoin Price")

st.line_chart(df["price"])

