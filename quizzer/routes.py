from quizzer import app
from quizzer.questions import QUESTIONS
from flask import render_template, request, session, url_for, redirect

@app.route('/')
def index():
	session['q_index'] = 0
	session['rights'] = 0
	session['num_questions'] = len(QUESTIONS)

	return render_template('index.html')

@app.route('/question')
def ask():
	if session['q_index'] == session['num_questions']:
		return redirect(url_for('results'))


	question = QUESTIONS[session['q_index']]
	button_text = 'Get Results' if session['q_index'] == session['num_questions'] - 1 else 'Next'

	session['answer'] = question.get('choices')[question.get('answer_index')]

	return render_template('question.html', button_text=button_text, q=question)

@app.route('/eval_choice', methods=['POST'])
def eval_choice():
	chosen_option = request.form.get('option')
	if chosen_option == session['answer']:
		session['rights'] += 1
	session['q_index'] += 1
	return redirect(url_for('ask'))

@app.route('/results')
def results():
	return render_template(
		'results.html',
		correct_answers=session['rights'],
		total_questions=session['num_questions'])