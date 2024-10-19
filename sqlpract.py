import sqlite3

global name
name = 'user'


def pr():
    conn = sqlite3.connect('dbf.sql')
    cur = conn.cursor()
    maino = ''
    cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
    d = cur.fetchone()
    print(d[0], d[1], d[2])

    cur.close()
    conn.close()


conn = sqlite3.connect('dbf.sql')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY , name UNIQUE, list TEXT )")
conn.commit()

cur.close()
conn.close()
print("All good")

pr()
olymp = str(input())
conn = sqlite3.connect('dbf.sql')
cur = conn.cursor()
maino = ''
cur.execute("SELECT * FROM users WHERE name = '%s'" % (name))
d = cur.fetchone()
maino = d[2] + ' , ' + olymp

cur.close()
conn.close()
print("All good")

conn = sqlite3.connect('dbf.sql')
cur = conn.cursor()

cur.execute("UPDATE users set list = '%s' WHERE name = '%s'" % (maino, name))
conn.commit()
cur.close()
conn.close()
pr()
'''@bot.message_handler(commands=['start'])
def stert(message):
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()


    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER  primary key , name TEXT , pass TEXT)')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id , "Text your name")
    bot.register_next_step_handler(message , user_name)
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Text your password")
    bot.register_next_step_handler(message, user_pass)
def user_pass(message):

    password = message.text.strip()
    conn = sqlite3.connect('dbase.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name , pass) VALUES('%s' , '%s')" % (name, password))
    conn.commit()

    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Users list" , callback_data='seeall'))
    bot.send_message(message.chat.id , "All good" , reply_markup=markup)
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if(callback.data == 'seeall'):
        conn = sqlite3.connect('dbase.sql')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        inf=''

        users=cur.fetchall()
        for i in users:
            inf+=f'Name : {i[1]} , Pass : {i[2]}\n'

        bot.send_message(callback.message.chat.id , inf)

        cur.close()
        conn.close()'''