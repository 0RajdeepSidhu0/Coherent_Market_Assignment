import sqlite3
import pandas as pd


DB_PATH = "../data/startups.db"


def create_connection():
    return sqlite3.connect(DB_PATH)


def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS startups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        slug TEXT,
        link TEXT UNIQUE,
        source TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn.execute(query)
    conn.commit()


def insert_data(conn, df: pd.DataFrame):
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO startups (name, slug, link, source)
                VALUES (?, ?, ?, ?)
            """, (row["name"], row["slug"], row["link"], row["source"]))
        except Exception as e:
            print(e)

    conn.commit()


def main():
    conn = create_connection()
    create_table(conn)

    df = pd.read_csv("data/startups_clean.csv")
    insert_data(conn, df)

    print("Data inserted into database!")

    conn.close()


if __name__ == "__main__":
    main()




'''
def insert_data(conn, df: pd.DataFrame):
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO startups (name, slug, link, source)
                VALUES (?, ?, ?, ?)
            """, (row["name"], row["slug"], row["link"], row["source"]))
        except Exception as e:
            print(e)

    conn.commit()
'''