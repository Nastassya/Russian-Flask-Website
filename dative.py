from data import *

def dative_sing(noun, gender):
  if noun['gender'] == 'm':
    if noun[-1] in consonants:
      answer = noun[:-1] + 'у'
    elif noun[-1] in ['й', 'ь']:
      answer = noun[:-1] + 'ю'
  elif noun['gender'] == 'f':
    if noun[-2:] == 'ия' or noun[-1] == 'ь':
      answer = noun[:-1] + 'и'
    elif noun[-1] in ['а', 'я']:
      answer = noun[:-1] + 'е'
  else:
    if noun[-1] == 'о':
      answer = noun[:-1] + 'у'
    elif noun[-1] == 'е':
      answer = noun[:-1] + 'ю'
    
    return answer

def dative_plural(noun):
  if noun[-1] in consonants:
    answer = noun + 'ам'
  elif noun[-1] in ['о', 'а']:
    answer = noun[:-1] + 'ам'
  else:
    answer = noun[:-1] + 'ям'
  
  return answer