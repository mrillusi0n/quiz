import random
import json


class Question:
	def __init__(self, question, incorrect_options, answer, option_font_type):
		self.question = question
		self.incorrect_options = incorrect_options
		self.answer = answer
		self.option_font_type = option_font_type

	@classmethod
	def from_dict(cls, data):
		return cls(**data)

	@property
	def options(self):
		options = [self.answer] + self.incorrect_options
		random.shuffle(options)

		return options

	def __repr__(self):
		return f'{self.question}: {self.options}'


class QuestionBox:
	def __init__(self, session, questions):
		self.questions = questions
		self.session = session

	@property
	def right_answers_count(self):
		return self.session['right_answers_count']

	@right_answers_count.setter
	def right_answers_count(self, count):
		self.session['right_answers_count'] = count

	@property
	def question(self):
		return self.questions[self.q_index]

	@property
	def num_questions(self):
		return self.session['num_questions']

	@num_questions.setter
	def num_questions(self, val):
		self.session['num_questions'] = val

	@property
	def q_index(self):
		return self.session['q_index']

	@property
	def correct_answers(self):
		return self.session['correct_answers']

	@q_index.setter
	def q_index(self, val):
		self.session['q_index'] = val

	def init(self):
		self.q_index = 0
		self.right_answers_count = 0
		self.num_questions = len(self.questions)

	def submit_answer(self, answer):
		self.right_answers_count += (self.question.answer == answer)
		self.q_index += 1

	def get_button_text(self):
		return 'Results' if self.q_index == self.num_questions - 1 else 'Next'

	def has_questions(self):
		return self.q_index < self.num_questions


def get_questions(filename):
	with open(filename) as questions_file:
		return list(map(Question.from_dict, json.load(questions_file)))


if __name__ == '__main__':
	main()
