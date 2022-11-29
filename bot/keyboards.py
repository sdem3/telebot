from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start_choice = ReplyKeyboardMarkup()

button_help = KeyboardButton('help', callback_data='help')

button_choice_museum = KeyboardButton('choice museum', callback_data='museums')

start_choice.add(button_help).add(button_choice_museum)



button_museums = [InlineKeyboardButton('tretyakovka', callback_data='tretyakovka_1_qst__'),
                  InlineKeyboardButton('2', callback_data='2'),
                  InlineKeyboardButton('3', callback_data='3'),
                  InlineKeyboardButton('4', callback_data='4'),
                  InlineKeyboardButton('5', callback_data='5')]


choice_museum = InlineKeyboardMarkup()
for button in button_museums:
    choice_museum.add(button)


choice_tretyakovka_1 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('да', callback_data='tretyakovka_1_ans_1'),
    InlineKeyboardButton('нет', callback_data='tretyakovka_1_ans_0'))

right_ans_tretyakovka_1 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('cледующий вопрос', callback_data = 'tretyakovka_2_qst__'),
)

choice_tretyakovka_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('да', callback_data='tretyakovka_2_ans_1'),
    InlineKeyboardButton('нет', callback_data='tretyakovka_2_ans_0'))

right_ans_tretyakovka_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('cледующий вопрос', callback_data = 'tretyakovka_3_qst__'),
)

choice_tretyakovka_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('да', callback_data='tretyakovka_3_ans_1'),
    InlineKeyboardButton('нет', callback_data='tretyakovka_3_ans_0') )
right_ans_tretyakovka_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('cледующий вопрос', callback_data = 'next_3'),
)
class Answer:
    def __init__(self, text, ans, right_ans, keyboard):
        self.text = text
        self.ans = ans
        self.right_ans = right_ans
        self.keyboard = keyboard


right_ans_tretyakovka_dict = {'tretyakovka_1_ans_1': Answer('this picture...', 1, 0, right_ans_tretyakovka_1),
                              'tretyakovka_2_ans_1': Answer('blabla', 1, 0, right_ans_tretyakovka_2),
                              'tretyakovka_3_ans_1': Answer('rrrrr', 1, 1, right_ans_tretyakovka_3),
                              'tretyakovka_1_ans_0': Answer('this picture...', 0, 0, right_ans_tretyakovka_1),
                              'tretyakovka_2_ans_0': Answer('blabla', 0, 0, right_ans_tretyakovka_2),
                              'tretyakovka_3_ans_0': Answer('rrrr', 0, 1, right_ans_tretyakovka_3)
                              }


class Question:
    def __init__(self, text, keyboard):
        self.text = text

        self.keyboard = keyboard



question_tretyakovka_dict = {
    'tretyakovka_1_qst__' : Question('question1',  choice_tretyakovka_1),
    'tretyakovka_2_qst__' : Question('question2',  choice_tretyakovka_2),
    'tretyakovka_3_qst__' : Question('question3',  choice_tretyakovka_3),
}

moderator_start_keyboard = InlineKeyboardMarkup()
moderator_start_buttons = [
                            InlineKeyboardButton('quest 1', callback_data = 'quest_1'),
                            InlineKeyboardButton('quest 2', callback_data = 'quest_2'),
                            InlineKeyboardButton('quest 3', callback_data= 'quest_3')
]
moderator_start_keyboard.add(moderator_start_buttons)
