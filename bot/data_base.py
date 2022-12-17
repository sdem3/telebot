import sqlite3 as sq
from aiogram import Bot
from config import TOKEN
bot = Bot(token=TOKEN)
def sql_start():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor()
    if base:
        print("Successfully connect with data base")
    base.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, user_id TEXT, age TEXT, gender TEXT, result_mus1 TEXT, result_mus2 TEXT, result_mus3 TEXT, result_mus4 TEXT, result_mus5 TEXT )')
    base.commit()
async def sql_add_command(state):
    async with state.proxy() as data:

        cur.execute('INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_get_result(idx, quiz_index):
    flag = True
    for req in cur.execute('SELECT * FROM user').fetchall():
        print(idx)

        if (req[1] == str(idx) and req[quiz_index + 3] != '-1' and flag):
            await bot.send_message(idx, text = 'набранный вами результат:' + req[quiz_index + 3])
            flag = False

    if flag:
        await bot.send_message(idx, text= 'вы еще не проходили тест')


async def sql_check_user(chat, quiz_index):
    for req in cur.execute('SELECT * FROM user').fetchall():
        if (req[1] == str(chat) and (req[quiz_index+3] != '-1')):
            await bot.send_message(chat, 'вы уже проходили тест, нажмите /result, для получения результата')
            return False
    return True