import logging

import markup
import telebot
import webbrowser
from telebot import types
import sqlite3
import ast
import requests
from bs4 import BeautifulSoup

from basepract import esr, to_name, pars_mephi, check_for_mephi, chech_for_mephi2, pars_mephi2
from mftipract import pars_mfti, pars_mfti2, check_for_mfti, pars_mfti3
from msupract import check_for_msu, pars_msu
from rsosh import rsosh, rsosh2, check_for_rsosh

name = 'user'
spisok_olymp=''

TOKEN = "7112683153:AAGJj2A0covZ9xHye-zNBADPjIfqrpzoFNI"
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
    global name

    reg_button = types.KeyboardButton('Увидеть свои данные')
    esr_button = types.KeyboardButton('Скопировать свои олимпиады с еср')
    help_button = types.KeyboardButton('Помощь')
    mifi_button = types.KeyboardButton('Куда я могу поступить в МИФИ')
    update_button = types.KeyboardButton('Добавить Олимпиаду')
    drop_button = types.KeyboardButton('Удалить мои данные')
    rsosh_button = types.KeyboardButton("Увидеть свои олимпиады из РСОШ")
    mfti_button = types.KeyboardButton("Какие олимпиады принимает МФТИ")
    delete_button = types.KeyboardButton("Удалить олимпиаду")
    msu_button = types.KeyboardButton("МГУ ВМК ПМИ")
    another_button=types.KeyboardButton("Какие вузы принимают мои олимпиады")
    markup = types.ReplyKeyboardMarkup()
    (markup.add(help_button).add( esr_button ).add(reg_button).add( mifi_button) .add( update_button) .add(rsosh_button).add(mfti_button)
     .add(msu_button)).add(another_button).add(delete_button).add( drop_button)
    conn = sqlite3.connect('dbase.sql')
    name = message.chat.username
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY , name UNIQUE, list TEXT )")
    conn.commit()
    bot.send_message(message.chat.id , "All good" , reply_markup=markup)
    cur.close()
    conn.close()
    bot.send_message(message.chat.id , "Привет! Я бот , который поможет тебе с мониторингом и применением своих личных достижений"
                                       "для этого мне нужен список твоих достижений"
                                       ",после этого я смогу помочь тебе их использовать ")
    bot.send_message(message.chat.id,
                     "Чтоб ознакомица с интрукцией и с ботом нажми кнопку 'Помощь'")

@bot.message_handler(content_types=['text'])
def discrim(message):
    if (message.text == 'drop'):

        drop(message)
    elif(message.text == 'Увидеть свои данные'):
        seeadmin(message)
        '''done '''
    elif(message.text == 'Скопировать свои олимпиады с еср'):
        '''done'''
        esr_bot(message)
    elif(message.text == 'Помощь'):
        '''not done idgf btw'''
        help(message)
    elif(message.text == 'Куда я могу поступить в МИФИ'):
        '''done without cout'''
        chek_mephi_bot(message)
    elif(message.text == 'Добавить Олимпиаду'):
        '''done'''
        update(message)
    elif(message.text == "Удалить мои данные"):
        '''done'''
        drop(message)
    elif(message.text == "Увидеть свои олимпиады из РСОШ"):
        '''done'''
        rss(message)
    elif(message.text == "Какие олимпиады принимает МФТИ"):
        '''done without cout idgaf'''
        mftitry(message)
    elif(message.text=="Удалить олимпиаду"):
        delolymp(message)
    elif(message.text == 'МГУ ВМК ПМИ'):
        trymsu(message)
    elif(message.text == "Какие вузы принимают мои олимпиады"):
        another(message)

@bot.message_handler(commands=['another'])
def another(message):
    global spisok_olymp
    global name
    reg_admin(message)

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if (len(spisok_olymp) > 3):
        spis = ast.literal_eval(spisok_olymp)

        ans = check_for_rsosh(rsosh2() , spis)
        if (len(ans) > 0):
            f1=0
            for i in ans:
                if (i[2]==2 or i[2] == '2' or i[2]==1 or i[2]=='1'):
                    f1=1
            if(f1 == 1):
                bot.send_message(message.chat.id , "У вас есть олимпиады 1-2 уровня ,вы можете получить особые права при поступление в эти вузы")
                bot.send_message(message.chat.id , "ИТМО \n МИСИС \n РТУ МИРЕЭА \n Санкт-Петербургский политехнический университет Петра Великого \n "
                                                   "Московский государственный технологический университет 'СТАНКИН' \n"
                                                   "Казанский (Приволжский) федеральный университет \n"
                                                   "Уральский федеральный университет имени первого Президента России Б.Н. Ельцина \n"
                                                   "Национальный исследовательский Томский политехнический университет"


                                 )

            else:
                bot.send_message(message.chat.id , "МИСИС \n РТУ МИРЕЭА \n Санкт-Петербургский политехнический университет Петра Великого \n "
                                                   "Московский государственный технологический университет 'СТАНКИН' \n"
                                                   "Казанский (Приволжский) федеральный университет \n"
                                                   "Уральский федеральный университет имени первого Президента России Б.Н. Ельцина \n"
                                                   "Национальный исследовательский Томский политехнический университет")

    else:
        bot.send_message(message.chat.id,
                         "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")

@bot.message_handler(commands=['seeforadmin'])
def seeadmin(message):
    reg_admin(message)
    global spisok_olymp
    global name

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if (len(spisok_olymp) > 3):
        spis = ast.literal_eval(spisok_olymp)


        for i in spis:
            bot.send_message(message.chat.id, str(i))

    else:
        bot.send_message(message.chat.id,
                         "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")



@bot.message_handler(commands=['reg'])
def reg(message):
    global name
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    name = message.chat.username
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
    global name
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
    reg_admin(message)
    bot.send_message(message.chat.id , "Введите ПОЛНОЕ НАИМЕНОВАНИЕ вашей олимпиады с предметом через запятую")
    bot.register_next_step_handler(message , olin)
def olin(message):
    reg_admin(message)
    global spisok_olymp
    global name

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if(len(spisok_olymp)>3):
        spis = ast.literal_eval(spisok_olymp)
        olymp =  (str(message.text)).split(',')
        spis.append(olymp)

        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("UPDATE users set list = ? WHERE name = ?", (str(spis), name))
        conn.commit()
        cur.close()
        conn.close()
        pr()
    else:
        a=list()
        olymp = (str(message.text)).split(',')
        a.append(olymp)
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("UPDATE users set list = ? WHERE name = ?", (str(a), name))
        conn.commit()
        cur.close()
        conn.close()
        pr()

    bot.send_message(message.chat.id, "All good")





@bot.message_handler(commands=["esr"])
def esr_bot(message):
    reg_admin(message)
    bot.send_message(message.chat.id , "Введите вашу Фамилию ,  Имя  , Очество , Дату рождения через запятую (ГГГГ-ММ-ДД)")
    bot.send_message(message.chat.id , "Пример: Иванов , Иван ,Иванович ,2008-04-20")
    bot.register_next_step_handler(message , esout)
def esout(message):
    reg_admin(message)
    fullstr = message.text
    fullstr = fullstr.split(',')
    if (len(fullstr) == 4):
        global spisok_olymp
        global name
        spisok_esr=esr(fullstr[0].strip() , fullstr[1].strip() ,fullstr[2].strip() , fullstr[3].strip())
        spisok_esr = to_name(spisok_esr)
        print(spisok_esr)
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
        d = cur.fetchone()
        maino = d[2]
        print(maino ,len(maino))
        if(len(maino)>3):
            ml = ast.literal_eval(maino)
            for i in spisok_esr:
                f=0
                for j in ml:
                    if i[0] == j[0] and i[1]==j[1]:
                        f=1
                if(f==0 ):
                    ml.append(i)
        else:
            ml = spisok_esr

        print(str(ml) )
        maino=str(ml)

        cur.close()
        conn.close()
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("UPDATE users set list = ? WHERE name = ?" , (maino, name))
        conn.commit()
        cur.close()
        conn.close()
        pr()
        bot.send_message(message.chat.id, "All good")
    else:
        bot.send_message(message.chat.id, "Некорректный ввод")

@bot.message_handler(commands=['delete_olymp'])
def delolymp(message):
    reg_admin(message)
    seeadmin(message)
    bot.send_message(message.chat.id , "Напишити номер олимпимады которую вы хотите удалить нумерация идет с 0")
    bot.register_next_step_handler(message , dely)
def dely(message):
    reg_admin(message)
    number = (str(message.text))
    if(number.isdigit()==1 and int(number) > 0):
        number=int(number)
        global spisok_olymp
        global name

        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
        d = cur.fetchone()
        spisok_olymp = d[2]

        cur.close()
        conn.close()
        if(len(spisok_olymp)>3):
            spis = ast.literal_eval(spisok_olymp)
            if(number < len(spis)):
                spis.remove(spis[number])
                conn = sqlite3.connect('dbase.sql')
                cur = conn.cursor()

                cur.execute("UPDATE users set list = ? WHERE name = ?", (str(spis), name))
                conn.commit()
                cur.close()
                conn.close()
                pr()
                bot.send_message(message.chat.id, "All good")
            else:
                bot.send_message(message.chat.id, "Out of range")
        else:
            bot.send_message(message.chat.id,
                             "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")


    else:
        bot.send_message(message.chat.id , "WRONG")








@bot.message_handler(commands=['drop'])
def drop(message):
    global name
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = '%s'" % (name))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id , "All good")

@bot.message_handler(commands=['is_mephfi'])
def chek_mephi_bot(message):
    global spisok_olymp
    global name
    reg_admin(message)

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if (len(spisok_olymp)>3):
        spis=ast.literal_eval(spisok_olymp)


        print(spis)
        ans = chech_for_mephi2(pars_mephi2() , spis)
        print(ans)
        for i in ans:
            bot.send_message(message.chat.id, str(i))


        bot.send_message(message.chat.id, "Эти дипломы должны быть за 10-11 класс")
    else:
        bot.send_message(message.chat.id,
                         "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")




@bot.message_handler(commands=['rsosh'])
def rss(message):
    reg_admin(message)
    global spisok_olymp
    global name

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()

    if (len(spisok_olymp)>3):
        spis = ast.literal_eval(spisok_olymp)
        rsosh = rsosh2()


        ans = check_for_rsosh(rsosh , spis)
        for i in ans:
            bot.send_message(message.chat.id , str(i))
    else:
        bot.send_message(message.chat.id,
                         "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")


@bot.message_handler(commands=['mfti'])
def mftitry(message):
    reg_admin(message)
    global spisok_olymp
    global name

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if (len(spisok_olymp)>3):
        spis = ast.literal_eval(spisok_olymp)


        ans = check_for_mfti(pars_mfti3() , spis)
        for i in ans:
            bot.send_message(message.chat.id , str(i))
        bot.send_message(message.chat.id, "Эти дипломы должны быть за 11 класс")
    else:
        bot.send_message(message.chat.id,"Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")



@bot.message_handler(commands=['MSU'])
def trymsu(message):
    reg_admin(message)
    global spisok_olymp
    global name

    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    spisok_olymp = d[2]

    cur.close()
    conn.close()
    if (len(spisok_olymp) > 3):
        spis = ast.literal_eval(spisok_olymp)

        ans = check_for_msu(pars_msu() , spis)

        for i in ans:
            bot.send_message(message.chat.id, str(i))
        bot.send_message(message.chat.id, "Эти дипломы должны быть за 11 класс")
    else:
        bot.send_message(message.chat.id,
                         "Простите но вы не добавили олимпиады добавьте их вручную или нажмите кнопку 'Скопировать свои олимпиады с еср'")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id , "Нажав кнопку 'Увидеть свои данные' вы увидете все свои данные которые у нас есть")
    bot.send_message(message.chat.id ,
                     "Нажав кнопку 'Скопировать свои олимпиады с еср' бот запросит вашу Фамилию, Имя, Отчество, "
                     "Дату рождения, чтобы потом получить все ваши олмпиады")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'Добавить олимпиаду' вы должны будите написать ПОЛНОЕ ИМЯ вашей олимпиады которую вы хотите добавить "
                     "ВАЖНО если вы введете не полное имя то бот будет работать не коректно")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'Удалить мои данный' бот удалит вас из своей базы данных")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'МГУ ВМК ПМИ ' бот выведет вам олимпиады которые принимает МГУ на это напрвление")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'Куда я могу поступить в МИФИ' бот выведит все списки напрвлений куды вы можете поступить ")
    bot.send_message(message.chat.id , "Нажав кнопку 'Какие олимпиады принимает МФТИ' бот выведет олимпиады которые принимает вуз ")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'Увидеть свои олимпиады из РСОШ' вы увидете свои олмпиады которые есть в списке рсош а также их уровень")
    bot.send_message(message.chat.id,
                     "Нажав кнопку 'Какие вузы принимают мои олимпиады' вы увидите список вузов которые принимают ваши олимпиады по профильным предметам")
    bot.send_message(message.chat.id ,
                     "Нажав кнопку 'Удалить олимпиаду' вы сможете выбрать олимпиаду которую захотите удалить из базы данных ")
    bot.send_message(message.chat.id , "ВАЖНО")
    bot.send_message(message.chat.id , "Бот работает не со всеми вузами ")
    bot.send_message(message.chat.id , "Бот берет информацию с официальных сайтов вузов")
    bot.send_message(message.chat.id , "Бот может гайти не все ваши достижения для этого вам придется добавить их вручную")

def reg_admin(message):
    global name
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()
    name = message.chat.username
    info = cur.execute("SELECT * FROM users WHERE name='%s'" % (name))
    if info.fetchone() is None:
        cur.execute("INSERT INTO users (name , list) VALUES ('%s' , '%s')" % (name, ' '))
        conn.commit()
    cur.close()
    conn.close()
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



bot.polling(none_stop=True)
