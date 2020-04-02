import csv


class Support:
    @staticmethod
    def check_correct(answer, true_answer):
        try:
            if not (int == type(answer)):
                answer = int(answer)
        except TypeError:
            raise Warning(f'Incorrect data: cannot make int variable from "{answer}"')

        if answer == true_answer:
            return True
        else:
            return False

    @staticmethod
    def get_true_answer(questions, num_of_question):
        for i, question in enumerate(questions):
            print(i, question)
            if i == num_of_question:
                true = questions[question]['true']
                return tuple((true, questions[question]['answers'][true]))
        raise IndexError

    @staticmethod
    def get_answer(questions, num_of_question, answer):
        for i, question in enumerate(questions):
            print(i, question)
            if i == num_of_question:
                print(questions[question]['answers'])
                print(answer)
                print(answer in questions[question]['answers'])
                answer = questions[question]['answers'].index(answer)
                return answer
        raise IndexError

    @staticmethod
    def csv_writer(path, data):
        with open(path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(data)
