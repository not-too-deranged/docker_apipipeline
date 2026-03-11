import streamlit as st
import pandas as pd
import psycopg2



from backend.models import create_tables

create_tables()


st.title("Global Data Dashboard")

st.write("API Data Visualization")

from backend.queries import get_crypto_data


data = get_crypto_data()

df = pd.DataFrame(data, columns=["id", "price", "timestamp"])

st.subheader("Bitcoin Price")

st.line_chart(df["price"])

from backend.queries import get_nasa_data

nasa_data = get_nasa_data()

nasa_df = pd.DataFrame(nasa_data, columns=["id", "date", "start_date", "end_date", "count", "thumbs"])

st.subheader("NASA Data")

st.line_chart(nasa_df["count"])

from backend.queries import get_country_data

country_data = get_country_data()

country_df = pd.DataFrame(country_data, columns=["id", "name", "population"])

st.subheader("Country Population")

st.bar_chart(country_df.set_index("name")["population"])

