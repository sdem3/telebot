from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import Question, Answer

last_question = '7'
choice_1 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Брак в Кане Галилейской', callback_data='mus5_1_ans_1')).add(
    InlineKeyboardButton('Тайная вечеря', callback_data='mus5_1_ans_0')).add(
    InlineKeyboardButton('Христос у Марфы и Марии', callback_data='mus5_1_ans_2'))


choice_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Давид', callback_data='mus5_2_ans_1')).add(
    InlineKeyboardButton('Артур', callback_data='mus5_2_ans_0')).add(
    InlineKeyboardButton('Теодорих', callback_data='mus5_2_ans_2'))


choice_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Любовь и пороки обезоруживают правосудие', callback_data='mus5_3_ans_1')).add(
    InlineKeyboardButton('Похищение Европы', callback_data='mus5_3_ans_0')).add(
    InlineKeyboardButton('Аполлон и Марсий', callback_data='mus5_3_ans_2'))


choice_4 = InlineKeyboardMarkup(resize_keyboard = True).add(
    InlineKeyboardButton('Мадонна со святым Людовиком Тулузским, Антонием Падуанским и Франциском Ассизским', callback_data='mus5_4_ans_1') ).add(
    InlineKeyboardButton('Непорочное зачатие', callback_data='mus5_4_ans_0')).add(
    InlineKeyboardButton('Аллегория с Венерой и временей', callback_data='mus5_4_ans_2'))

choice_5 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Римский форум с аркой Тита и фигурами на фоне Капитолия', callback_data='mus5_5_ans_1')).add(
    InlineKeyboardButton('Сивилла предсказывает рождение Христа', callback_data='mus5_5_ans_0')).add(
    InlineKeyboardButton('Застолье над ионическим портиком', callback_data='mus5_5_ans_2'))

choice_6 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Смерть Дидоны', callback_data='mus5_6_ans_1')).add(
    InlineKeyboardButton('Иаков зарывает идолов в землю под Сихемским дубом', callback_data='mus5_6_ans_0')).add(
    InlineKeyboardButton('Жертвоприношение Ноя', callback_data='mus5_6_ans_2'))

choice_7 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Клеопатра-Селена. Сардоникс, Александрия. 1 в до н.э.', callback_data='mus5_7_ans_1')).add(
    InlineKeyboardButton('Скульптуры восточного фронтона Парфенона. Ок. 440-432 гг до н.э.', callback_data='mus5_7_ans_0')).add(
    InlineKeyboardButton('Кони Гелиоса 442-432 гг до н.э.', callback_data='mus5_7_ans_2'))



right_answer_dict = { '1' : Answer('text1', '1'), '2': Answer('text2', '0'),
                      '3' : Answer('text3', '2'), '4': Answer('text4', '1'),
                      '5' : Answer('text5', '0'), '6': Answer('text6', '2'),
                      '7':  Answer('text7', '0')
}


question_dict = {
    'mus5_1_qst__' : Question('''«Что ж за свадьба без вина?!» - подумал Иисус и превратил воду в вино. Женщина в центре композиции в прямом смысле светится от радости, а Иисус скромно сидит рядом. Назовите эту картину
''',  choice_1),

    'mus5_2_qst__' : Question('''этот легендарный король будет спать в каменной пещере до тех пор, пока он не потребуется своей стране. Но поскольку он каждый день нужен посетителям музея, приходится стоять. Фишер Петер Старший, мастерская. Назовите короля 
.''',  choice_2),

    'mus5_3_qst__' : Question('''Никогда не вызывайте богов на музыкальные состязания. Победителя в паука превратят, а проигравшего - и того хуже. Подтверждение вы найдёте на картине Луки Джордано. Выберете ее название : 
''',  choice_3),

    'mus5_4_qst__' : Question(''' Компанию Богоматери составляют 3 святых, несколько ангелочков и пёс. Зачем им череп - непонятно. Джованни Баттиста Тьеполо написал эту картину, а вы выберете ее название: 
''',  choice_4),

    'mus5_5_qst__' : Question(''' Являя посетителям свои работы, Джованни Паоло Панини предлагает посетителям сыграть в игру «Найди 10 отличий». Исчезновение собаки сразу же бросается в глаза. Джованни Паоло Панини был великим художником, сможете ли вы выбрать, о какой картине идёт речь?''',
        choice_5),
    'mus5_6_qst__' : Question(''' На картине Себастьяна Бурдона животные выглядят намного выразительнее людей, но это можно объяснить. Пережить Всемирный потоп и сразу после этого быть принесенным в жертву Ноем, удовольствие не из приятных. Выберете, о какой картине идёт речь Жертвоприношение Ноя.''', choice_6),

    'mus5_7_qst__' : Question('''У Коня богини Селены сохранилась только голова. Впрочем, и сама Селена сохранилась не лучше. Найдите данные скульптуры и выберете название: Скульптуры восточного фронтона Парфенона. Ок. 440 - 432 гг. до н.э.''', choice_7)

}