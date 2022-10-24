endings = {
  'ать': {
    '1s': 'ю',
    '2s': 'ешь',
    '3s': 'ет',
    '1p': 'ем',
    '2p': 'ете',
    '3p': 'ют'
  },
  'ить': {
    '1s': 'ю',
    '2s': 'ишь',
    '3s': 'ит',
    '1p': 'им',
    '2p': 'ите',
    '3p': 'ят'
  }
  'еть': {
    '1s': 'ю',
    '2s': 'шь',
    '3s': 'ет',
    '1p': 'ем',
    '2p': 'ете',
    '3p': 'ют'
  }
}

def present_tense(verb, subject):

  if verb[-3:] == 'ать':
    answer = verb[:-2] + endings['ать'][subject]
  
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
      if subject == '1s':
        answer = verb[:-3] + 'лю'
      else:
        answer = verb[:-3] + endings['ить'][subject]

    else:
      answer = verb[:-3] + endings['ить'][subject]

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
      answer = verb[:-2] + endings['еть'][subject]
    
  else:
    answer = 'Not covered'
  
  return answer