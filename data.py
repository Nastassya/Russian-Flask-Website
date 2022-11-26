consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

subjects = {'1s': '1st person singular', '2s': '2nd person singular', '3s': '3rd person singular', '1p': '1st person plural', '2p': '2nd person plural', '3p': '3rd person plural'}

def spell_except(word):
  if word[-2] in ['г', 'к', 'х', 'ж', 'ч', 'ш', 'щ']:
    if word[-1] == 'ы':
      word = word[:-1] + 'и'
    else:
      word = word
  
  return word

nouns = {
  "table": {"russian": "стол", "gender": "m", 'animate': 'n'},
  "plate": {"russian": "тарелка", "gender": "f", 'animate': 'n'},
  #"towel": {"russian": "полотенце", "gender": "n"},
  #"child": {"russian": "ребёнок", "gender": "m"},
  "woman": {"russian": "женщина", "gender": "f", 'animate': 'y'},
  'person': {'russian': 'человек', 'gender': 'm', 'animate': 'y'},
  
  #need to find way of defining genitive plural
  #'friend': {'russian': 'друг', 'gender': 'm'},

  'man': {'russian': 'мужчина', 'gender': 'm', 'animate': 'y'},
  'boy': {'russian': 'мальчик' , 'gender': 'm', 'animate': 'y'},
  'girl': {'russian': 'девочка', 'gender': 'f', 'animate': 'y'},
  'young woman; girl; girlfriend': {'russian': 'девушка', 'gender': 'f', 'animate': 'y'},

  #need to find way of defining genitive singular and plural
  #'young man; boy; boyfriend': {'russian': 'парень', 'gender': 'm'},

  #need to find way of defining genitive singular and plural
  #'name': {'russian': 'имя', 'gender': 'n'},
  'surname/family name': {'russian': 'фамилия', 'gender': 'f', 'animate': 'n'},
  'boss': {'russian': 'начальник', 'gender': 'm', 'animate': 'y'},
  'visitor/guest': {'russian': 'гость', 'gender': 'm', 'animate': 'y'},
}

verbs = {
  'знать': 'to know',
  'жить': 'to live',
  'любить': 'to love/like',
  'работать': 'to work',
  #'говорить': 'to speak',
  #'думать': 'to think',
  'понимать': 'to understand',
  #'мочь': 'to be able to',
  'хотеть': 'to want',
  'делать': 'to do',
  #'брать': 'to take',
  #'давать': 'to give',
  'помнить': 'to remember'
}