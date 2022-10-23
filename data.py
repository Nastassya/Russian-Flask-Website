consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

subjects = {'1s': '1st person singular', '2s': '2nd person singular', '3s': '3rd person singular', '1p': '1st person plural', '2p': '2nd person plural', '3p': '3rd person plural'}

nouns = {
  "table": {"russian": "стол", "gender": "m"},
  "plate": {"russian": "тарелка", "gender": "f"},
  #"towel": {"russian": "полотенце", "gender": "n"},
  #"child": {"russian": "ребёнок", "gender": "m"},
  "woman": {"russian": "женщина", "gender": "f"},
  'person': {'russian': 'человек', 'gender': 'm'},
  
  #need to find way of defining genitive plural
  #'friend': {'russian': 'друг', 'gender': 'm'},
  
  'man': {'russian': 'мужчина', 'gender': 'm'},
  'boy': {'russian': 'мальчик' , 'gender': 'm'},
  'girl': {'russian': 'девочка', 'gender': 'f'},
  'young woman; girl; girlfriend': {'russian': 'девушка', 'gender': 'f'},

  #need to find way of defining genitive singular and plural
  #'young man; boy; boyfriend': {'russian': 'парень', 'gender': 'm'},

  #need to find way of defining genitive singular and plural
  #'name': {'russian': 'имя', 'gender': 'n'},
  'surname/family name': {'russian': 'фамилия', 'gender': 'f'},
  'boss': {'russian': 'начальник', 'gender': 'm'},
  'visitor/guest': {'russian': 'гость', 'gender': 'm'},
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