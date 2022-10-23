import random, string

from flask import Flask, render_template, request, jsonify
from data import *
from genitive import *
from conjugations import *


#Function to choose noun
def pick_noun():
  noun_list = list(nouns)
  english = random.choice(noun_list)
  russian = nouns[english]["russian"]
  gender = nouns[english]["gender"]
  return (english, russian, gender)

def pick_verb():
  verb_list = list(verbs)
  verb = random.choice(verb_list)
  subject_list = list(subjects)
  subject = random.choice(subject_list)
  return(verb, subject)

#Variable for user's input
user_ans = ""

app = Flask(
  __name__,

  template_folder='templates',
  
  static_folder='static'
)

@app.route('/')
def home():
  random_num = random.randint(1, 100)
  
  return render_template('home.html',)

@app.route('/2', methods=['POST'])
def to_practice_page():
  data = request.form
  case = data['case']
  page_title = string.capwords(case)
  english, russian, gender = pick_noun()
  route = '/2'

  if case == 'genitive':
    correct_ans = nom_to_gen(russian, gender)
  elif case =='genitive plural':
    correct_ans = nom_gen_plural(russian, gender)
  else:
    correct_ans = ''
    
  return render_template('noun_case.html', english = english, russian = russian, gender = gender, case = case, route = route, page_title = page_title, correct_ans = correct_ans)


'''
def genitive():
  case = "genitive"
  page_title = string.capwords(case)
  english, russian, gender = pick_noun()
  correct_ans = nom_to_gen(russian, gender)
  route = '/2'
  return render_template('noun_case.html', english = english, russian = russian, gender = gender, case = case, route = route, page_title = page_title, correct_ans = correct_ans)

def genitive():
  case = "genitive"
  page_title = string.capwords(case)
  english, russian, gender = pick_noun()
  route = '/2'
  return render_template('noun_case.html', english = english, russian = russian, gender = gender, case = case, route = route, page_title = page_title)
'''

@app.route('/2.1')
def gen_plural():
  case = "genitive plural"
  page_title = string.capwords(case)
  english, russian, gender = pick_noun()
  route = '/2.1'
  return render_template('noun_case.html', english = english, russian = russian, gender = gender, case = case, route = route, page_title = page_title)

@app.route('/3', methods=['POST'])
def check_answer():
  # https://pythonbasics.org/flask-http-methods/
  data = request.form
  russian = data['russian']
  gender = data['gender']
  case = data['case']
  user_ans = data['answer'].lower()
  route = data['route']
  page_title = data['page_title']

  if case == 'genitive':
    correct_ans = nom_to_gen(russian, gender)
  elif case == 'genitive plural':
    correct_ans = nom_gen_plural(russian, gender)

  if user_ans == correct_ans:
    print(correct_ans)
    print(user_ans)
    return render_template('correct_answer.html', russian = russian, case = case, user_ans = user_ans, correct_ans = correct_ans, route = route, page_title = page_title)
  else:
    return render_template('noun_case_incorrect.html', russian = russian, case = case, user_ans = user_ans, correct_ans = correct_ans, route = route, page_title = page_title)

   #print("you answered {0}".format(data['answer']))

   # send a JSON response to the client
   #return jsonify(response="you answered {0}".format(data['answer']))

@app.route('/verb_conj')
def verb_conj():
  verb, case = pick_verb()
  page_title = string.capwords(subjects[case])
  subject = subjects[case]
  route = '/verb_conj'
  return render_template('verb_conj.html', verb = verb, case = case, subject = subject, route = route, page_title = page_title)

@app.route('/4', methods=['POST'])
def check_verb():
  # https://pythonbasics.org/flask-http-methods/
  data = request.form
  verb = data['verb']
  case = data['case']
  user_ans = data['answer'].lower()
  route = data['route']
  page_title = data['page_title']
  subject = data['subject']

  answer = present_tense(verb, case)

  if user_ans == answer:
    return render_template('correct_answer.html', russian = verb, case = subject, user_ans = user_ans, correct_ans = answer, route = route, page_title = page_title)
  else:
    return render_template('noun_case_incorrect.html', russian = verb, case = subject, user_ans = user_ans, correct_ans = answer, route = route, page_title = page_title)
  
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
  
