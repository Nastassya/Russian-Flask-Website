import random
from main import *
from data import *

def genitive_sing(russian, gender):

#http://masterrussian.com/aa061500a.shtml
  
  if gender == "m":
    if russian[-1] in consonants:
      answer = russian + "а"
    elif russian[-1] in ["й", "ь"]:
      answer = russian[:-1] + "я"
    elif russian[-1] == "а":
      answer = russian[:-1] + "ы"
  
  elif gender == "f":
    if russian[-1]  in ["я", "ь"]:
      answer = russian[:-1] + "и"
    elif russian[-1] == "а":
      if russian[-2] in ['к', 'г', 'х', 'ж', 'ш']:
        answer = russian[:-1] + "и"
      else:
        answer = russian[:-1] + "ы"

  elif gender == "n":
    if russian[-1] == "о":
      answer = russian[:-1] + "а"
    #need to add a case for special consonants
    elif russian[-1] == "е":
      answer = russian[:-1] + "я"
    elif russian[-1] == "я":
      answer = russian[:-1] + "и"

  return answer

def genitive_plural(russian, gender):

  if gender == "m":
    if russian[-1] in consonants:
      if russian[-1] in ["ж,ч,ш,щ"]:
        answer = russian + "ей"
      else:
        answer = russian + "ов"
    elif russian[-1] == "й":
      answer = russian[:-1] + "ев"
    elif russian[-1] in ['ь', 'я']:
      if russian[-2] == 'ь':
        answer = russian[:-2] + "ей"
      else:
        answer = russian[:-1] + "ей"
    elif russian[-1] == 'а':
      answer = russian[:-1]
      #Figure out how to code the following -- Add -ёв to one-syllable nouns like край, чай. Exceptions are nouns like брат, лист which get the ending -ьев.

    #from earlier code. Not sure of origin
    '''
    elif noun[-1] in ["й", "ц"]:
      answer = russian[:-1] + "ев"
    else:
      answer = russian + "ов"
    '''
  
  elif gender == "f":
    if russian[-1] == "а":
      if russian[-2] in consonants:
        if russian[-3] not in consonants:
          answer = russian[:-1]
        elif russian[-3] in ['ч', 'ш']:
          answer = russian[:-2] + 'е' + russian[-2]
        else:
          answer = russian[:-2] + 'о' + russian[-2]
      else:
        answer = russian[:-1]
    elif russian[-1] == "я":
      if russian[-2] in consonants:
        answer = russian[:-1] + "ь"
      else:
        answer = russian[:-1] + "й"
    elif russian[-1] == "ь":
      answer = russian[-1] + "ей"

  elif gender == "n":
    if russian[-1] == "о":
      answer = russian[:-1]
    elif russian[-1] == "е":
      if russian[-2] == 'и':
        answer = russian[:-1] + "й"
      else:
        answer = russian + "й"

  return answer