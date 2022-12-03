import sqlite3
con = sqlite3.connect('words.db')

def sql_interact():
  cur = con.cursor()

  data = [
    ('стул', 'm', 'n', 'chair'),
    ('кошка', 'f', 'y', 'cat'),
  ]
  #cur.execute('CREATE TABLE IF NOT EXISTS nouns (russian UNIQUE, gender, animate, english, exceptions);')

  cur.executemany("INSERT OR IGNORE INTO nouns (russian, gender, animate, english) VALUES (?, ?, ?, ?)", data)

  con.commit()

  cursor_object = cur.execute('SELECT * FROM nouns;')

  objects = cursor_object.fetchall()

  print(objects)