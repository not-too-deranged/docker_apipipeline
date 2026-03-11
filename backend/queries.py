from backend.db import get_connection


def insert_crypto(price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO crypto (bitcoin_price) VALUES (%s)",
        (price,)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_crypto_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM crypto ORDER BY timestamp DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def insert_nasa_data(date, start_date, end_date, count, thumbs):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO nasa (date, start_date, end_date, count, thumbs) VALUES (%s, %s, %s, %s, %s)",
        (date, start_date, end_date, count, thumbs)
    )

    conn.commit()
    cur.close()
    conn.close()

def get_nasa_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM nasa ORDER BY date DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def insert_country(name, population):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO countries (name, population) VALUES (%s, %s)",
        (name, population)
    )

    conn.commit()
    cur.close()
    conn.close()

def get_countries():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM countries")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows