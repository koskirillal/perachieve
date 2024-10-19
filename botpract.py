import logging
import telebot
import webbrowser
from telebot import types
import sqlite3
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

name = 'user'

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
    olymp = message.text
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    maino = ''
    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    maino = d[2] + ' , ' + olymp

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

@bot.message_handler(commands=['drop'])
def drop(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = '%s'" % (name))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id , "All good")




@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = (types.InlineKeyboardButton("Go to site" , url='https://olymp.mephi.ru/'))
    markup.row(btn1)
    btn2 = (types.InlineKeyboardButton("Delete photo" ,callback_data='delete'))
    btn3 = (types.InlineKeyboardButton("Change text" ,callback_data='edit'))
    markup.row(btn2 , btn3)
    bot.reply_to(message , "Very beautifull" , reply_markup =markup)
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if(callback.data == 'delete'):
        bot.delete_message(callback.message.chat.id , callback.message.message_id -1)
    elif callback.data == 'edit':
        bot.edit_message_text("Edit text" , callback.message.chat.id ,callback.message.message_id )





@bot.message_handler(commands=['site' , 'mfti'])
def site(message):
    webbrowser.open("https://olymp-online.mipt.ru/")


@bot.message_handler(commands=['mifi'])
def site(message):
    webbrowser.open("https://org.mephi.ru/index/index")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id , "help info")




bot.polling(none_stop=True)
