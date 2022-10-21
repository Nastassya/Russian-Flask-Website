def present_tense(verb, subject):

  if verb[-3:] == 'ать':
    if subject == '1s':
      answer = verb[:-2] + 'ю'
    elif subject == '2s':
      answer = verb[:-2] + 'ешь'
    elif subject == '3s':
      answer = verb[:-2] + 'ет'
    elif subject == '1p':
      answer = verb[:-2] + 'ем'
    elif subject == '2p':
      answer = verb[:-2] + 'ете'
    elif subject == '3p':
      answer = verb[:-2] + 'ют'
  
  elif verb[-3:] == 'ить':

    #case for жить
    if len(verb) == 4:
      if subject == '1s':
        answer = verb[:-2] + 'ву'
      elif subject == '2s':
        answer = verb[:-2] + 'вёшь'
      elif subject == '3s':
        answer = verb[:-2] + 'вёт'
      elif subject == '1p':
        answer = verb[:-2] + 'вём'
      elif subject == '2p':
        answer = verb[:-2] + 'вёте'
      elif subject == '3p':
        answer = verb[:-2] + 'вут'

    #case for любить
    elif verb[-4] == 'б':
      stem = verb[:-3]

      if subject == '1s':
        answer = stem + 'лю'
      elif subject == '2s':
        answer = stem + 'ишь'
      elif subject == '3s':
        answer = stem + 'ит'
      elif subject == '1p':
        answer = stem + 'им'
      elif subject == '2p':
        answer = stem + 'ите'
      elif subject == '3p':
        answer = stem + 'ят'

    else:
      if subject == '1s':
        answer = verb[:-3] + 'ю'
      elif subject == '2s':
        answer = verb[:-2] + 'шь'
      elif subject == '3s':
        answer = verb[:-2] + 'ит'
      elif subject == '1p':
        answer = verb[:-2] + 'м'
      elif subject == '2p':
        answer = verb[:-3] + 'ите'
      elif subject == '3p':
        answer = verb[:-3] + 'ят'

  elif verb[-3:] == 'еть':

    #case for хотеть
    if verb[-4] == 'т':
      stem = verb[:2]
      if subject == '1s':
        answer = stem + 'чу'
      elif subject == '2s':
        answer = stem + 'чешь'
      elif subject == '3s':
        answer = stem + 'чет'
      elif subject == '1p':
        answer = stem + 'тим'
      elif subject == '2p':
        answer = stem + 'тите'
      elif subject == '3p':
        answer = stem + 'тят'

    else:
      stem = verb[:-2]
      if subject == '1s':
        answer = verb[:-3] + 'ю'
      elif subject == '2s':
        answer = verb[:-2] + 'шь'
      elif subject == '3s':
        answer = verb[:-2] + 'ет'
      elif subject == '1p':
        answer = verb[:-2] + 'ем'
      elif subject == '2p':
        answer = verb[:-3] + 'ете'
      elif subject == '3p':
        answer = verb[:-3] + 'ют'
    
  else:
    answer = 'Not covered'
  
  return answer