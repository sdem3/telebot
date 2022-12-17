from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import Question, Answer

last_question = '4'
choice_1 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Новодевичий', callback_data='mus2_1_ans_1'),
    InlineKeyboardButton('Соловецкий', callback_data='mus2_1_ans_0'),
    InlineKeyboardButton('Высоко-Петровский', callback_data='mus2_1_ans_2'))



choice_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Виолончель', callback_data='mus2_2_ans_1'),
    InlineKeyboardButton('Скрипка', callback_data='mus2_2_ans_0'),
    InlineKeyboardButton('Гитара', callback_data='mus2_2_ans_2'),
)


choice_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Апрель', callback_data='mus2_3_ans_1'),
    InlineKeyboardButton('Май', callback_data='mus2_3_ans_0'),
    InlineKeyboardButton('Ноябрь', callback_data='mus2_3_ans_2'),
)


choice_4 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Деревянная', callback_data='mus2_4_ans_1'),
    InlineKeyboardButton('Железная', callback_data='mus2_4_ans_0'),
    InlineKeyboardButton('Керамическая', callback_data='mus2_4_ans_2'),
)


right_answer_dict = { '1' : Answer('text1', '2'), '2': Answer('text2', '0'),
                      '3' : Answer('text3', '1'), '4': Answer('text4', '0')
}


question_dict = {
    'mus2_1_qst__' : Question('''В 2003 году А. Шилов написал картину, на которой изображен П.Я. Шейманидзе.
Его образ привлекает нас своим чистым, без толики лукавства взглядом.
Посмотрите на листы богослужебной книги – кажется, что еще чуть-чуть, и они
колыхнутся от движения воздуха. Вопрос: Послушником какого монастыря, что
попал в название картины, является П.Я. Шейманидзе?''',  choice_1),

    'mus2_2_qst__' : Question(''' На картине «Где царствуют звуки (Юлия Волченкова)» перед нашим взором
предстает женственная, одухотворённая, нежная девушка. Она мягко склоняет
голову в нашу сторону, будто приглашая окунуться вместе с ней в удивительный
мир музыки. Что на данном портрете держит в руках девушка?''',  choice_2),

    'mus2_3_qst__' : Question('''Какой месяц изображен Шиловым, на картине 1987 г., в которой представлена
перед нами тихая окраина села Федоскино с деревянным храмом и домами''',  choice_3),

    'mus2_4_qst__' : Question('''Полотно «Одна» было написано в 1980 году. На нем изображена пожилая
женщина. Она печально смотрит перед собой, ведь ей грустно и одиноко. Она
сидит за столом, пьет чай, кушает конфеты. Вопрос: Из какого материала кружка
изображенная на картине?''',  choice_4),
}