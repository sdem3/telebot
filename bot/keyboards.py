from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start_choice = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)

button_help = KeyboardButton('Помощь', callback_data='help')

button_choice_museum = KeyboardButton('Выбрать музей', callback_data='museums')

start_choice.add(button_help).add(button_choice_museum)

get_result_keyboard = InlineKeyboardMarkup(one_time_keyboard=True).add(
                  InlineKeyboardButton('галерея искусства стран европы и америки 19-20 веков', callback_data='res4', resize_button = True)).add(
                  InlineKeyboardButton('галерея глазунова', callback_data='res1')).add(
                  InlineKeyboardButton('галерея шилова', callback_data='res2')).add(
                  InlineKeyboardButton('дом-музей булгакова', callback_data='res3')).add(
                  InlineKeyboardButton('пушкинская галерея', callback_data='res5'))


button_museums = [InlineKeyboardButton('галерея стран европы и америки', callback_data='mus4_1_qst__'),
                  InlineKeyboardButton('галерея глазунова', callback_data='mus1_1_qst__'),
                  InlineKeyboardButton('галерея шилова', callback_data='mus2_1_qst__'),
                  InlineKeyboardButton('дом-музей булгакова', callback_data='mus3_1_qst__'),
                  InlineKeyboardButton('пушкинская галерея', callback_data='mus5_1_qst__')]

choice_museum = InlineKeyboardMarkup(one_time_keyboard=True)
for button in button_museums:
    choice_museum.add(button)



moderator_start_keyboard = InlineKeyboardMarkup()
moderator_start_buttons = [
                            InlineKeyboardButton('quest 1', callback_data = 'quest_1'),
                            InlineKeyboardButton('quest 2', callback_data = 'quest_2'),
                            InlineKeyboardButton('quest 3', callback_data= 'quest_3')
]
moderator_start_keyboard.add(moderator_start_buttons)

