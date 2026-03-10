from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests

def fetch_nasa():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    print(r.json())

def fetch_crypto():
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    print(r.json())

def fetch_country():
    r = requests.get("https://restcountries.com/v3.1/all")
    print(r.json())

with DAG(
    dag_id="api_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    nasa = PythonOperator(
        task_id="nasa",
        python_callable=fetch_nasa
    )

    crypto = PythonOperator(
        task_id="crypto",
        python_callable=fetch_crypto
    )

    country = PythonOperator(
        task_id="countries",
        python_callable=fetch_country
    )

    nasa >> crypto >> country