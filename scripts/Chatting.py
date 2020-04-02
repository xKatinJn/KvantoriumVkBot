import random
import os

from resources.Phrases import PHRASES


class Conversation:
    @staticmethod
    def answer_hello(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id, message=message if message else PHRASES['hello'], random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id, message=message if message else PHRASES['default'],
                         random_id=0, keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz_correct(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id,
                         message=message if message else random.choice(PHRASES['quiz_correct']), random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz_incorrect(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id,
                         message=random.choice(PHRASES['quiz_incorrect'])+message, random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz_ended(vk, message, keyboard, event, correct_answers, num_of_questions):
        phrase = message
        if correct_answers > num_of_questions//2:
            phrase += PHRASES['quiz_ended_congratulations'][1]
        else:
            phrase += PHRASES['quiz_ended_congratulations'][0]
        phrase += PHRASES['quiz_ended_conclusion'][0] + str(correct_answers) + '. ' + \
                  PHRASES['quiz_ended_conclusion'][1] + os.environ.get('form_url')

        vk.messages.send(peer_id=event.obj.peer_id,
                         message=phrase, random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz_value_error(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id,
                         message=message if message else PHRASES['quiz_value_error'], random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)

    @staticmethod
    def answer_quiz_limit(vk, message, keyboard, event):
        vk.messages.send(peer_id=event.obj.peer_id,
                         message=message if message else PHRASES['quiz_limited'], random_id=0,
                         keyboard=keyboard.get_keyboard() if keyboard else None)
