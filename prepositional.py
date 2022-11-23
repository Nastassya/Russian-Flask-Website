from data import *

def prepositional_sing(noun, gender):
  if noun['gender'] == 'm':
    answer = noun + 'е'
  elif noun['gender'] == 'f':
    if noun[-1] in ['а', 'я']:
      answer = noun[:-1] + 'е'
    elif noun[-1] == 'ь':
      answer = noun[:-1] + 'и'

  else:
    if noun[-1] == 'о':
      answer = noun[:-1] + 'е'
    else:
      answer = noun

  return answer

def prepositional_plural(noun):
  if noun[-1] in consonants or noun[-1] in ['о', 'а']:
    answer = noun[:-1] + 'ах'
  else:
    answer = noun[:-1] + 'ях'

  return answer