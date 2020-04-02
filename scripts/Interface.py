from vk_api.keyboard import VkKeyboard, VkKeyboardColor


"""
questions{
    q1{
        answers: ['...', '...']
        true: integer index
    }

}

"""


class Interface:
    def __init__(self, questions: dict, one_time=True):
        self.questions = questions
        self.one_time = one_time

    @staticmethod
    def get_simple_keyboard(buttons: list, one_time=True):
        keyboard = VkKeyboard(one_time=one_time)
        for i, button in enumerate(buttons):
            if i % 2 == 0 and i != 0:
                keyboard.add_line()
            keyboard.add_button(button, VkKeyboardColor.PRIMARY)
        return keyboard

    def get_quiz_keyboard(self):
        for key in self.questions:
            answer_keyboard = VkKeyboard(one_time=self.one_time)
            print(self.questions[key])
            for i, answer in enumerate(self.questions[key]['answers']):
                if i % 2 == 0 and i != 0:
                    answer_keyboard.add_line()
                print(answer)
                answer_keyboard.add_button(answer, color=VkKeyboardColor.PRIMARY)
            yield tuple((self.questions[key]['question'], answer_keyboard))
