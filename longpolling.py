import os

from scripts.Chatting import Conversation
from scripts.Interface import Interface
from scripts.Support import Support

from kvantorium_bot import vk, longpoll
from vk_api.bot_longpoll import VkBotEventType


conversation = Conversation()
questions = {
    'q1': {
        'question': 'Рекурсия это...\n'+
                    'a) То, что никогда не используется\n'+
                    'б) Функция, которая вызывает сама себя и имеет условие для выхода',
        'answers': ['а', 'б'],
        'true': 1
    },
    'q2': {
        'question': 'Что такое ардуино?',
        'answers': ['ЯП для электроники на опр. чипсетах', 'ЯП для сумасшедших', 'ЯП для создания 3Д игр', 'ЯП для всего'],
        'true': 0
    }
}

quiz_info = {
    'ids': [],
    'answered': [],
    'correct_answers': []
}
continued_peer_ids = []
quiz = None
qst = None

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.peer_id in quiz_info['ids']:
            peer_index = quiz_info['ids'].index(event.obj.peer_id)
            try:
                num_of_question = quiz_info['answered'][peer_index]
                true_answer = Support.get_true_answer(questions, num_of_question)
                try:
                    if Support.check_correct(Support.get_answer(questions, num_of_question,
                                                                event.obj.text), true_answer[0]):
                        quiz_info['correct_answers'][peer_index] += 1
                        conversation.answer_quiz_correct(vk, None, None, event)
                    else:
                        conversation.answer_quiz_incorrect(vk, true_answer[1], None, event)
                except ValueError:
                    conversation.answer_quiz_value_error(vk, None, qst[1], event)
                    continue
                quiz_info['answered'][peer_index] += 1
                qst = next(quiz)
                conversation.answer_quiz(vk, qst[0], qst[1], event)
            except StopIteration:
                correct_answers = quiz_info['correct_answers'][peer_index]
                quiz_info['answered'].remove(quiz_info['answered'][peer_index])
                quiz_info['correct_answers'].remove(quiz_info['correct_answers'][peer_index])
                quiz_info['ids'].remove(event.obj.peer_id)
                Support.csv_writer(os.environ.get('csv_path'), [event.obj.peer_id])
                conversation.answer_quiz_ended(vk, 'На этом все. ', None, event, correct_answers, len(questions))

        if 'привет' in event.obj.text.lower().split():
            conversation.answer_hello(vk, None, Interface.get_simple_keyboard(['Приступим']), event)

        if 'приступим' in event.obj.text.lower().split():
            with open(os.environ.get('csv_path'), 'r') as file:
                data = file.readlines()

            for peer_value in data:
                peer = peer_value.rstrip()
                if peer not in continued_peer_ids:
                    continued_peer_ids.append(peer)

            if str(event.object.from_id) not in continued_peer_ids:
                quiz = Interface(questions).get_quiz_keyboard()
                quiz_info['ids'].append(event.obj.peer_id)
                quiz_info['answered'].append(0)
                quiz_info['correct_answers'].append(0)

                try:
                    qst = next(quiz)
                    conversation.answer_quiz(vk, qst[0], qst[1], event)
                except StopIteration:
                    raise Warning('No one question has been received.')
            else:
                conversation.answer_quiz_limit(vk, None, None, event)
