'''
def to_practice_page():
  data = request.form
  case = data['case']
  print(case)

  if case == 'genitive':
    def genitive():
      page_title = string.capwords(case)
      english, russian, gender = pick_noun()
      correct_ans = nom_to_gen(russian, gender)
      route = '/2'
      return render_template('noun_case.html', english = english, russian = russian, gender = gender, case = case, route = route, page_title = page_title, correct_ans = correct_ans)
'''