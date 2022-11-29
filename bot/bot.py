from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import data_base
class UserState(StatesGroup):
    user_id = State()
    user_name = State()
    age = State()
    sex = State()
    result = State()
    endgame = State()
import keyboards as kb

ID = None
bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

user_result = dict()
@dp.message_handler(commands = ['moderator'], is_chat_admin = True)
async def make_chages_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, 'hi my lord')


@dp.message_handler(lambda c: c.text == 'choice museum', state = "*")
async def show_process_list_museums(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'text', reply_markup=kb.choice_museum)


@dp.message_handler(commands=['result'], state = '*')
async def show_res(message: types.Message):
    await data_base.sql_get_result(message)


@dp.message_handler(commands=['start'], state = None)
async def process_start_command(message: types.Message):
    state = dp.current_state(user = message.from_user.id)
    await UserState.user_name.set()
    await message.reply("Hi, whats your name?")


@dp.message_handler(state = UserState.user_name )
async def show(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.text
        data['user_id'] = message.from_user.id
    await UserState.next()
    await message.reply(f'Приветствуем, { data["user_name"] }, введите свой возраст')


@dp.message_handler(state = UserState.age)
async def show(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await UserState.next()
    await bot.send_message(message.from_user.id, f'your age: {data["age"]}, введите свой пол')


@dp.message_handler(state = UserState.sex)
async def show(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = message.text
    await UserState.next()
    await bot.send_message(message.from_user.id, f'your id: {data["user_id"]}', reply_markup= kb.start_choice)




@dp.callback_query_handler(lambda c: c.data[0:11] == 'tretyakovka', state = UserState.result)
async def quiz_tretyakovka(callback_query: types.CallbackQuery, state: FSMContext):
    number_of_question = callback_query.data[12:13]
    type = callback_query.data[14:17]
    chat = callback_query.from_user.id
    flag = await data_base.sql_check_user(chat)
    if not(flag):
        return
    if type == 'qst':
        question = kb.question_tretyakovka_dict.get(callback_query.data)
        text = question.text
        keyboard = question.keyboard
    elif type == 'ans':
        answer =  kb.right_ans_tretyakovka_dict.get(callback_query.data)
        if (number_of_question == '1'):
            async with state.proxy() as data:
                data['result_tretyakovka'] = 0
        if (answer.right_ans == answer.ans):
            text = answer.text + 'right!'
            async with state.proxy() as data:
                data['result_tretyakovka'] += 1
        else:
            print(str(state))
            text = answer.text + ' wrong!'
        keyboard = answer.keyboard
        if number_of_question == '3':
            keyboard = None
            await UserState.next()
            await data_base.sql_add_command(state)
            async with state.proxy() as data:
                text +='\n' + f'your result: {data["result_tretyakovka"]} '
    await bot.send_message(chat, text, reply_markup=keyboard)

async def on_startup(_):
    print('BOT ONLINE')
    data_base.sql_start()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup)