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