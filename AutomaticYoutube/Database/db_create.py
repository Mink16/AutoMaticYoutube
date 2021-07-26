import sqlite3

con = sqlite3.connect('./AutomaticYoutube/Database/automatic_youtube.db')
cursor = con.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS search;
CREATE TABLE search(
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,site_type
  ,word TEXT
  ,download_count INTEGER
  ,last_update TEXT
)
""")

data = [
  ('tiktok', '胸キュンダンス', 0, '20201213'),
  ('tiktok', 'あるあるネタ', 0, '20201213'),
  ('tiktok', 'ネタ', 0, '20201213'),
  ('tiktok', 'イケメン', 0, '20201213'),
  ('tiktok', 'ノーズペイント', 0, '20201213'),
  ('tiktok', 'あるある', 0, '20201213'),
  ('tiktok', '有名人になりたい', 0, '20201213'),
  ('tiktok', 'おすすめ', 0, '20201213'),
  ('tiktok', 'コメディー部門', 0, '20201213'),
  ('tiktok', 'バスれ', 0, '20201213'),
]
cursor.executemany('INSERT INTO search(site_type, word, download_count, last_update) VALUES(?, ?, ?, ?)', data)

cursor.executescript("""
DROP TABLE IF EXISTS movie;
CREATE TABLE movie(
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,search_id INTEGER
  ,url TEXT
  ,last_update TEXT
)
""")
con.commit()