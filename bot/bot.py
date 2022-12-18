from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import data_base
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import keyboards as kb
import glasunov_galery_keyboards as kbmus1
import shilov_galery_keyboards as kbmus2
import bulgakov as kbmus3
import europeneangalery as kbmus4
import pushkin as kbmus5
museum_dict = {'mus1': kbmus1, 'mus2': kbmus2, 'mus3' : kbmus3, 'mus4': kbmus4, 'mus5': kbmus5}
class UserState(StatesGroup):
    user_id = State()
    user_name = State()
    age = State()
    sex = State()
    result = State()
    endgame = State()


bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())



@dp.message_handler(commands = ['help'], state = '*')
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'это проект учениц хихигса и студента МФТИ')


@dp.message_handler(text = 'Помощь', state= '*')
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Если у вас возникли сложности с нашим ботом, напишите пожалуйста нашим менеджерам и вам ответят как можно скорее: @Dorofeya @sdementev33')



@dp.message_handler(commands = ['moderator'], is_chat_admin = True)
async def make_chages_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, 'hi my lord')


@dp.message_handler(lambda c: c.text == 'Выбрать музей', state = "*")
async def show_process_list_museums(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выберите музей в который хотите отправиться', reply_markup=kb.choice_museum)



@dp.message_handler(commands=['result'], state = '*')
async def show_res(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'выберите по какому квесту вы хотите узнать свой результат',
    reply_markup=kb.get_result_keyboard)


@dp.callback_query_handler(lambda c: c.data[0:3] == 'res', state = UserState.result)
async def get_result(callback_query: types.CallbackQuery, state: FSMContext):
    query = callback_query.data[3]
    await data_base.sql_get_result(callback_query.from_user.id, int(query))
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=None
    )

@dp.message_handler(commands=['start'], state = None)
async def process_start_command(message: types.Message, state:  FSMContext):
    async with state.proxy() as data:
        data['user_name'] = '0'
        data['user_id'] = '0'
        data['age'] = '0'
        data['sex'] = '0'
        data['result_mus1'] = -1
        data['result_mus2'] = -1
        data['result_mus3'] = -1
        data['result_mus4'] = -1
        data['result_mus5'] = -1

    state = dp.current_state(user = message.from_user.id)
    await UserState.user_name.set()
    await message.reply("Приветствую вас в уникальном проекте, с помощью которого проходить музеи будет не только полезно и познавательно, но ещё и очень интересно! С помощью данного бота, вы можете выбрать любой музей, и пройти уникальный квест, разработанный нашей группой. Квесты можно проходить только один раз, поэтому внимательно выбирайте ответы. Для того, чтобы начать наше путешествие, пожалуйста, напишите своё имя")


@dp.message_handler(state = UserState.user_name )
async def show(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.text
        data['user_id'] = message.from_user.id
        print(data)
    await UserState.next()
    await message.reply(f'Приветствуем, { data["user_name"] }, введите свой возраст')


@dp.message_handler(state = UserState.age)
async def show(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
    async with state.proxy() as data:
        data['age'] = message.text
    await UserState.next()
    await bot.send_message(message.from_user.id, f'ваш возраст: {data["age"]}, введите свой пол')


@dp.message_handler(state = UserState.sex)
async def show(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
    async with state.proxy() as data:
        data['sex'] = message.text
    await UserState.next()
    await bot.send_message(message.from_user.id, f'ваш пол: {data["sex"]}', reply_markup= kb.start_choice)


@dp.callback_query_handler(lambda c: c.data[0:3] == 'mus', state = UserState.result)
async def quiz_glasunov(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=None
    )
    museum = callback_query.data[0:4]
    museum_file = museum_dict[museum]
    number_of_question = callback_query.data[5]
    type = callback_query.data[7:10]
    chat = callback_query.from_user.id
    flag = await data_base.sql_check_user(chat, int(callback_query.data[3]))
    if not(flag):
        return
    async with state.proxy() as data:
        print(data)
    print('work')
    if type == 'qst':
        question = museum_file.question_dict.get(callback_query.data)
        text = question.text
        keyboard = question.keyboard
    elif type == 'ans':
        right_answer = museum_file.right_answer_dict.get(number_of_question)
        answer = callback_query.data[11]
        result_name = 'result_' + museum
        callback = museum + '_' + str(int(number_of_question) + 1) + '_qst__'
        if (number_of_question == '1'):
            async with state.proxy() as data:
                data[result_name] = 0
        if (right_answer.value == answer):
            text = 'Поздравляем, правильный ответ'
            async with state.proxy() as data:
                data[result_name] += 1

        else:
            print(str(state))
            text = 'К сожалению, вы ошиблись! Надеюсь в следующих вопросах, удача будет на вашей стороне '
        print(callback)
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton('cледующий вопрос', callback_data=callback),
        )

        if number_of_question == museum_file.last_question:
            keyboard = None
            #await UserState.next()
            await data_base.sql_add_command(state)
            async with state.proxy() as data:
                text +='\n' + f'Ваш результат: {data[result_name]} '
    await bot.send_message(chat, text, reply_markup=keyboard)


async def on_startup(_):
    print('BOT ONLINE')
    data_base.sql_start()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup)