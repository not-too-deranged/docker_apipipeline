from backend.db import get_connection


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS crypto (
        id SERIAL PRIMARY KEY,
        bitcoin_price FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    #TODO: Change this to work with NASA data

    cur.execute("""
    CREATE TABLE IF NOT EXISTS nasa (
        id SERIAL PRIMARY KEY,
        temperature FLOAT,
        city TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id SERIAL PRIMARY KEY,
        name TEXT,
        population BIGINT
    )
    """)

    conn.commit()
    cur.close()
    conn.close()