from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import Question, Answer

last_question = '9'
choice_1 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нападение ягуара на лошадь', callback_data='mus4_1_ans_1')).add(
    InlineKeyboardButton('Нападение Льва на антилопу', callback_data='mus4_1_ans_0')).add(
    InlineKeyboardButton('Нападение кота на воробья', callback_data='mus4_1_ans_2'))


choice_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('«Эрос»', callback_data='mus4_2_ans_1')).add(
    InlineKeyboardButton('«Скрипка»', callback_data='mus4_2_ans_0')).add(
    InlineKeyboardButton('«Мандолина»', callback_data='mus4_2_ans_2'))


choice_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('«Ферма»', callback_data='mus4_3_ans_1')).add(
    InlineKeyboardButton('«Карнавал Арлекина» ', callback_data='mus4_3_ans_0')).add(
    InlineKeyboardButton('«Композиция»', callback_data='mus4_3_ans_2'))




choice_4 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('«Пьеро и Арлекин»', callback_data='mus4_4_ans_1')).add(
    InlineKeyboardButton('«Игра в карты» ', callback_data='mus4_4_ans_0')).add(
    InlineKeyboardButton('«Большие купальщицы»', callback_data='mus4_4_ans_2'))

choice_5 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Автопортрет ', callback_data='mus4_5_ans_1')).add(
    InlineKeyboardButton('Вид моста Севр и холмов Кламара, Сен Клу и Бельвю', callback_data='mus4_5_ans_0')).add(
    InlineKeyboardButton('Сон цыганки ', callback_data='mus4_5_ans_2'))

choice_6 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('«Человек в трауре»', callback_data='mus4_6_ans_1')).add(
    InlineKeyboardButton('«Человек с того света»', callback_data='mus4_6_ans_0')).add(
    InlineKeyboardButton('«Человек в пальто»', callback_data='mus4_6_ans_2'))

choice_7 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Обнаженные в лесу', callback_data='mus4_7_ans_1')).add(
    InlineKeyboardButton('Строители', callback_data='mus4_7_ans_0')).add(
    InlineKeyboardButton('Город', callback_data='mus4_7_ans_2'))


choice_8 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Портрет Герника ', callback_data='mus4_8_ans_1')).add(
    InlineKeyboardButton('Портрет Анхеля Фернандеса де Сото ', callback_data='mus4_8_ans_0')).add(
    InlineKeyboardButton('Портрет Сабартеса', callback_data='mus4_8_ans_2'))


choice_9 = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Красная комната', callback_data='mus4_9_ans_1')).add(
    InlineKeyboardButton('Настурции. Панно «Танец» II', callback_data='mus4_9_ans_0')).add(
    InlineKeyboardButton('Танец', callback_data='mus4_9_ans_2'))






right_answer_dict = { '1' : Answer('text1', '1'), '2': Answer('text2', '0'),
                      '3' : Answer('text3', '2'), '4': Answer('text4', '1'),
                      '5' : Answer('text5', '0'), '6': Answer('text6', '2'),
                      '7':  Answer('text7', '0'), '8' :Answer('text8', '2'),
                      '9': Answer('text9', '0')
}


question_dict = {
    'mus4_1_qst__' : Question('''Глядя на картину Анри Руссо, изображающую схватку двух животных, вы сразу не сможете сказать кто на кого напал. Назоваите картину
''',  choice_1),

    'mus4_9_qst__' : Question('''Если вам кажется, что вы плохо танцуете, посмотрите на эту картину Анри Матисса и вам сразу же станет легче.
''',  choice_9),

    'mus4_2_qst__' : Question('''Хороший скрипач после смерти становится Скрипкой Страдивари, а плохой - этим экспонатом Армана Фернандеса.''',  choice_2),

    'mus4_3_qst__' : Question(''' Эта картина Хуана Миро является универсальным ответом на приглашение выпить в пятницу.''',  choice_3),

    'mus4_4_qst__' : Question(''' Герои картины Поля Сезанна являются полными противоположностями. Тем не менее, судя по их настроению можно сделать вывод о том, что они отлично ладят. ''',
        choice_4),
    'mus4_5_qst__' : Question('''Дирижабль - удивительное средство воздушного перемещения 19 века. Тем не менее, во всей галерее он изображён только на одной картине. Найдите картину с дирижаблем. ''', choice_5),

    'mus4_6_qst__' : Question('''В отличие от картин Рене Магритта, этот мужчина в котелке не падает с неба, а мирно стоит в одном из залов. Назовите его
''', choice_6),

    'mus4_7_qst__' : Question(''' 20 век - это время революционной борьбы. Рабочие по всему миру брали свободу в свои руки. Однако, рабочие с этой картины Фернана Леже решили взять в свои руки алоэ.  Назовите эту картину ''', choice_7),

    'mus4_8_qst__' : Question('''Молодого человека с этой картины Пабло Пикассо не утешает даже кружка пива в руке. Неудивительно - он же поэт.  Чей это портрет?  ''', choice_8)
}