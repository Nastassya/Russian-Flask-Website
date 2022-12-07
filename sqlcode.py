import sqlite3

def sql_alterdata():
  con = sqlite3.connect('words.db')
  cur = con.cursor()
  
  data = [
    ('стол', 'm', 'n', 'table'),
    ('тарелка', 'f', 'n', 'plate'),
    ('женщина', 'f', 'y', 'woman'),
    ('человек', 'm', 'y', 'person'),
    ('мужчина', 'm', 'y', 'man'),
    ('мальчик', 'm', 'y', 'boy'),
    ('девочка', 'f', 'y', 'girl'),
    ('девушка', 'f', 'y', 'young woman; girl; girlfriend'),
    ('фамилия', 'f', 'n', 'surname/family name'),
    ('начальник', 'm', 'y', 'boss'),
    ('гость', 'm', 'y', 'visitor/guest')
  ]
  
  #cur.execute('CREATE TABLE IF NOT EXISTS nouns (russian UNIQUE, gender, animate, english, exceptions);')

  cur.executemany("INSERT OR IGNORE INTO nouns (russian, gender, animate, english) VALUES (?, ?, ?, ?)", data)

  con.commit()

def sql_pull(category):
  con = sqlite3.connect('words.db')
  cur = con.cursor()

  if category == 'noun':
    cursor_object = cur.execute('SELECT * FROM nouns;')

  objects = cursor_object.fetchall()

  return objects