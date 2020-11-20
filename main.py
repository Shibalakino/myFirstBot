import telebot
import config
from rex import MWT

bot = telebot.TeleBot(config.TOKEN)
number = 0
name = ''
arr1 = []
arr2 = []
arr3 = []
counter = 0
intro1 = "Привіт, {0.first_name}! \n Я <b>{1.first_name}</b>, бот для створення черг( ͡° ͜ʖ ͡°)."
intro2 = "Даний бот має декілька команд : \n 1) /start_queue - привітатись за ботом ))))0)))000)0 \n 2) /join_queue " \
         "- записуєш себе у чергу \n 3) /show_queue - показати чергу \n 4) /clear_queue - очистити список \n 5) " \
         "/help_pls_queue - говорить сама за себе ;) "
intro3 = "Привіт, {0.first_name}, якщо бажаєте скинути молодому інженеру на хліб-ось мої реквізити \n " \
         "5375414113694276 ;) "


# команда початку

@bot.message_handler(commands=['start_queue'])
def welcome(message):
    sti = open('images/sticker3.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, intro1.format(message.from_user, bot.get_me()), parse_mode='html')


# раз у дві години формує списки адмінів і записує їх у список

@MWT(timeout=60 * 60)
def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]


# команда допомоги

@bot.message_handler(commands=['help_queue'])
def helping(message):
    bot.send_message(message.chat.id, intro2)


# функція для перевірки. чи є людина у списку

def check(message):
    for i in range(len(arr1)):
        if "{0.first_name}".format(message.from_user, bot.get_me()) == arr1[i]:
            bot.send_message(message.chat.id, "Ви вже зареєстровані")
            break


# бере глобальні змінні. та записує кожну людину в масив імен

@bot.message_handler(commands=['join_queue'])
def start(message):
    global number
    global name
    global counter
    global arr1
    global arr2
    number = counter
    check(message)
    for i in range(len(arr1)):
        if "{0.first_name}".format(message.from_user, bot.get_me()) == arr1[i]:
            quit()
            bot.send_message(message.chat.id, "Ви вже зареєстровані")
    name = "{0.first_name}".format(message.from_user, bot.get_me())
    arr1.append(name)
    bot.send_message(message.chat.id, "Ви успішно зареєстровані")


# показати список

@bot.message_handler(commands=['show_queue'])
def cont(message):
    for i in range(len(arr1)):
        result = str(i + 1) + " - " + arr1[i]
        bot.send_message(message.chat.id, result)


# просто вивід

@bot.message_handler(commands=['help_pls_queue'])
def helping(message):
    bot.send_message(message.chat.id, intro3.format(message.from_user, bot.get_me()), parse_mode='html')
    sti2 = open('images/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti2)


# якщо користувач є адміністратором - то він може очистити списки

@bot.message_handler(commands=['clear_queue'])
def end(message):
    user_id = message.from_user.id
    if user_id in get_admin_ids(bot, bot):
        bot.send_message(message.chat.id, "увійшов в цикл")
        global number
        global name
        global counter
        global arr1
        global arr2
        name = ''
        number = 0
        arr1 = []
        arr2 = []
        counter = 0
    else:
        bot.send_message(message.chat.id, "у тебе немає прав.лол")


# програма працює

bot.polling(none_stop=True, interval=0)
