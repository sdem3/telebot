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
    base.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, user_id TEXT, age TEXT, gender TEXT, user_result TEXT )')
    base.commit()
async def sql_add_command(state):
    async with state.proxy() as data:
        print('!!!!!!!!!!!!!!!!'+str(data.values())+'!!!!!!!!!!')
        cur.execute('INSERT INTO user VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_get_result(message):
    flag = True
    for req in cur.execute('SELECT * FROM user').fetchall():
        print(message.from_user.id)
        print(type(message.from_user.id))
        if (req[1] == str(message.from_user.id) and flag):
            await bot.send_message(message.from_user.id, text = req[4])
            flag = False
    if flag:
        await bot.send_message(message.from_user.id, text= 'вы еще не проходили тест')


async def sql_check_user(chat):
    for req in cur.execute('SELECT * FROM user').fetchall():
        if (req[1] == str(chat)):
            await bot.send_message(chat, 'вы уже проходили тест, нажмите /result, для получения результата')
            return False
    return True