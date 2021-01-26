from quizzer import app
from quizzer.questions import QuestionBox, get_questions
from flask import render_template, request, session, url_for, redirect

question_box = QuestionBox(session, get_questions('questions.json'))


@app.route('/')
def index():
	question_box.init()

	return render_template('index.html', qc=question_box.num_questions)


@app.route('/question')
def ask():
	if not question_box.has_questions():
		return redirect(url_for('results'))

	data = {
		'button_text': question_box.get_button_text(),
		'q': question_box.question,
	}

	print(data['q'].options)

	return render_template('question.html', **data)


@app.route('/eval_choice', methods=['POST'])
def eval_choice():
	question_box.submit_answer(request.form.get('option'))

	return redirect(url_for('ask'))


@app.route('/results')
def results():
	data = {
		'correct_answers': question_box.right_answers_count,
		'total_questions': question_box.num_questions,
	}

	return render_template('results.html', **data)
