import sqlite3

def sql_alterdata():
  con = sqlite3.connect('words.db')
  cur = con.cursor()

  '''
  data = [
    ('знать', 'to know'),
    ('жить', 'to live'),
    ('любить', 'to love/like'),
    ('работать', 'to work'),
    ('понимать', 'to understand'),
    ('хотеть', 'to want'),
    ('делать', 'to do'),
    ('помнить', 'to remember')
  ]
  
  cur.execute('CREATE TABLE IF NOT EXISTS verbs (russian UNIQUE, english, exceptions);')
  '''

  cur.executemany("INSERT OR IGNORE INTO verbs (russian, english) VALUES (?, ?)", data)

  con.commit()

def sql_pull(category):
  con = sqlite3.connect('words.db')
  cur = con.cursor()

  if category == 'noun':
    cursor_object = cur.execute('SELECT * FROM nouns;')

  if category == 'verb':
    cursor_object = cur.execute('SELECT * FROM verbs;')

  objects = cursor_object.fetchall()

  return objects