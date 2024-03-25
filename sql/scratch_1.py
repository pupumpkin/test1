import sqlite3


con = sqlite3.connect('scratch.db')

cur = con.cursor()

query = CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    product_type TEXT DEFAULT "Фильм",
    release_year INTEGER
);

cur.execute(query)

con.close()