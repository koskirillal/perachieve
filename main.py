import logging
import telebot
import webbrowser
from telebot import types
import sqlite3
import requests
from bs4 import BeautifulSoup

from basepract import esr, to_name, pars_mephi, check_for_mephi

name = 'user'
spisok_olymp=''

TOKEN = "7941996491:AAF-fCmv3aaYtdHgTxUx13vyQjvsFqY40wo"
bot = telebot.TeleBot(TOKEN)

def pr():
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    maino=''
    cur.execute("SELECT * FROM users WHERE name = '%s'" %(name))
    d = cur.fetchone()
    print(d[0] , d[1] , d[2])



    cur.close()
    conn.close()




@bot.message_handler(commands=['show_me'])
def show_me(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    print(d)
    bot.send_message(message.chat.id , d[2])

    cur.close()
    conn.close()


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY , name UNIQUE, list TEXT )")
    conn.commit()
    bot.send_message(message.chat.id , "All good")
    cur.close()
    conn.close()

@bot.message_handler(commands=['reg'])
def reg(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    info = cur.execute("SELECT * FROM users WHERE name='%s'" % (name))
    if info.fetchone() is None:
        cur.execute("INSERT INTO users (name , list) VALUES ('%s' , '%s')" %(name , ' '))
        conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("User list", callback_data='seeall'))
    bot.send_message(message.chat.id, "All good", reply_markup=markup)




@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if (callback.data == 'seeall'):

        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
        d = cur.fetchone()
        print(d[0], d[1], d[2])

        cur.close()
        conn.close()

        bot.send_message(callback.message.chat.id, str(d))


@bot.message_handler(commands=["update"])
def update(message):
    bot.send_message(message.chat.id , "Text your olymp")
    bot.register_next_step_handler(message , olin)
def olin(message):
    global spisok_olymp
    olymp = message.text
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    maino = ''
    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    maino = d[2] + ' , ' + olymp
    spisok_olymp = maino[:]
    cur.close()
    conn.close()
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("UPDATE users set list = '%s' WHERE name = '%s'" % (maino, name))
    conn.commit()
    cur.close()
    conn.close()
    pr()

    bot.send_message(message.chat.id , "All good")


@bot.message_handler(commands=["esr"])
def esr_bot(message):
    bot.send_message(message.chat.id , "Введите вашу Фамилию ,  Имя  , Очество , Дату рождения через запятую (ГГГГ-ММ-ДД)")
    bot.send_message(message.chat.id , "Пример: Иванов , Иван ,Иванович ,2008-04-20")
    bot.register_next_step_handler(message , esout)
def esout(message):
    fullstr = message.text
    fullstr = fullstr.split(',')
    if (len(fullstr) == 4):
        global spisok_olymp
        spisok_esr=esr(fullstr[0].strip() , fullstr[1].strip() ,fullstr[2].strip() , fullstr[3].strip())
        spisok_esr = to_name(spisok_esr)
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()
        maino = ''
        cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
        d = cur.fetchone()
        maino = d[2]
        spisok_olymp = maino[:]
        for i in spisok_esr:
            if(maino.count(i) == 0):
                maino += ', ' + i
                spisok_olymp += ', ' + i

        cur.close()
        conn.close()
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("UPDATE users set list = '%s' WHERE name = '%s'" % (maino, name))
        conn.commit()
        cur.close()
        conn.close()
        pr()
        bot.send_message(message.chat.id, "All good")


@bot.message_handler(commands=['drop'])
def drop(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = '%s'" % (name))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id , "All good")

@bot.message_handler(commands=['is_mifi'])
def chek_mifi_bot(message):
    global spisok_olymp

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    spis=spisok_olymp.split(',')
    for i in range(len(spis)):
        spis[i]=spis[i].strip()

    print(spis)
    res_mifi = check_for_mephi(pars_mephi()  , spis)
    print(res_mifi)
    if (len(res_mifi) > 0):
        bot.send_message(message.chat.id , "Вы можете поступить в мифи по этим олимпиадам")
        for i in res_mifi:
            bot.send_message(message.chat.id, i)




@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id , "help info")




bot.polling(none_stop=True)
