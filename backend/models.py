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


    cur.execute("""
    CREATE TABLE IF NOT EXISTS nasa (
        id SERIAL PRIMARY KEY,
        date DATE,
        start_date DATE,
        end_date DATE,
        count INT,
        thumbs BOOLEAN
  
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