from data import *
from nominative import *
from genitive import *

def accusative_sing(noun, gender, animate):
  if gender == 'f':
    if noun[-1] == 'а':
      answer = noun[:-1] + 'у'
    elif noun[-1] == 'я':
      answer = noun[:-1] + 'ю'
    else:
      answer = noun
  
  elif gender == 'm':
    if animate == 'n':
      answer = noun
    else:
      if noun[-1] in consonants or noun[-1] == 'ь':
        answer = noun + 'а'
      else:
        answer = noun[:-1] + 'я'
  
  else:
    answer = noun

  return answer

def accusative_plural(noun, gender, animate):
  if animate == 'n':
    answer = nom_plural(noun, gender)
  else:
    answer = genitive_plural(noun, gender)

  return answer