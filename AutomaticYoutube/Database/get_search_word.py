import sqlite3

class TikTok:
    def __init__(self, *args):
      pass
    
    def get_words(self):
      con = sqlite3.connect('/Users/mink/Documents/Pythons/AutoMaticYoutube/AutomaticYoutube/Database/automatic_youtube.db')
      cur = con.cursor()
      cur.execute("""
        SELECT word
        FROM search
        WHERE site_type=?
        ORDER BY download_count
        """, ('tiktok',))
      return cur.fetchall()
