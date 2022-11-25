from data import *

def nom_plural(noun, gender):
  if gender == 'm':
    if noun[-1] in consonants:
      answer = spell_except(noun + 'ы')
    else:
      answer = noun[:-1] + 'и'
  
  elif gender == 'f':
    if noun[-1] in ['я', 'ь']:
      answer = noun[:-1] + 'и'
    elif noun[-1] == 'а':
      answer = spell_except(noun[:-1] + 'ы')
  
  else:
    if noun[-1] == 'о':
      answer = noun[:-1] + 'а'
    elif noun[-1] == 'я':
      if noun[-2] == 'м':
        answer = noun[:-1] + 'ена'
      else:
        answer = noun[:-1] + 'я'
  
  return answer