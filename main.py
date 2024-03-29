import random, string

from flask import Flask, render_template, request, jsonify
from data import *
from sqlcode import *

from accusative import *
from dative import *
from genitive import *
from nominative import *
from prepositional import *

from conjugations import *

#Run SQL file
sql_alterdata()

#Function to choose noun
def pick_noun():
  noun_list = sql_pull("noun")
  data = random.choice(noun_list)
  russian = data[0]
  gender = data[1]
  return (russian, gender)

#Function to choose verb
def pick_verb():
  verb_list = sql_pull('verb')
  data = random.choice(verb_list)
  verb = data[0]
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
  route = '/2'

  if case == 'present':
    verb, subject = pick_verb()
    correct_ans = present_tense(verb, subject)
    subject = subjects[subject]
    english = ''
    russian = verb
    gender = ''
    

  else:
    russian, gender = pick_noun()
    english = "english"

    if case == 'genitive':
      correct_ans = genitive_sing(russian, gender)
    elif case =='genitive plural':
      correct_ans = genitive_plural(russian, gender)
    elif case == 'nominative plural':
      correct_ans = nom_plural(russian, gender)
    elif case == 'accusative singular':
      animate = nouns[english]['animate']
      correct_ans = accusative_sing(russian, gender, animate)
    elif case == 'accusative plural':
      animate = nouns[english]['animate']
      correct_ans = accusative_plural(russian, gender, animate)
    elif case == 'dative singular':
      correct_ans = dative_sing(russian, gender)
    elif case == 'dative plural':
      correct_ans = dative_plural(russian)
    elif case == 'prepositional singular':
      correct_ans = prepositional_sing(russian, gender)
    elif case == 'prepositional plural':
      correct_ans = prepositional_plural(russian)
    else:
      correct_ans = ''

    subject = case
      
  return render_template('prac_verb_or_noun.html', english = english, russian = russian, gender = gender, case = case, subject = subject, route = route, page_title = page_title, correct_ans = correct_ans)
  
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)