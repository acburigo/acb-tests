import json


class Test:
    def __init__(self, filepath):
        self._load_test(filepath)
        self._question_index = 0
        self._questions_answered = 0
        self._questions_answered_correctly = 0

    def _load_test(self, filepath):
        file = open(filepath, 'r')
        self.test_json = json.load(file)
        file.close()

    def _get_next_question(self):
        if len(self.test_json['questions']) <= self._question_index:
            return None
        question = Question(self.test_json['questions'][self._question_index])
        self._question_index += 1
        return question

    def _update_statistics(self, question_result):
        self._questions_answered += 1
        if question_result:
            self._questions_answered_correctly += 1

    def perform_test(self):
        question = self._get_next_question()
        while question is not None:
            print()
            question.show()
            is_correct = question.wait_for_answer()
            self._update_statistics(is_correct)

            if is_correct:
                print('Good job!')
            else:
                question.show_correct_answer()

            question = self._get_next_question()


class Question:
    def __init__(self, question_json):
        self.text = question_json['question']
        self.options = question_json['options']
        self.answer = question_json['answer']

    def show(self):
        print('Question: %s' % self.text)
        print()
        print('Options:')
        for index, option in enumerate(self.options):
            print('\t%d) %s' % (index, option))
        print()

    def show_correct_answer(self):
        print('The correct answer would be \"%s\".' % self.answer)

    def wait_for_answer(self):
        print('Answer:', end=' ')
        given_answer = input()
        return self.options[int(given_answer)] == self.answer
