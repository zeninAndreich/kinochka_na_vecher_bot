import telebot
from config import token
from keybouards import Keybouards
from Dly_films import populer_films
from Dly_serials import populer_serials


bot = telebot.TeleBot(token)
name = ''


@bot.message_handler(commands=['start'])
def start_com(message):
    privetcvie = 'Приветсвую в моем боте! :)\nКак тебя зовут?'
    bot.send_message(message.chat.id, privetcvie)
    bot.register_next_step_handler(message,
                                   reg_name)  # прописываем,что нужно вызвать функцию сразу после сообщения "как тебя зовут"


@bot.message_handler(commands=['help'])
def help_com(message):
    help_text = """ 
    "Для того чтобы начать введите команду /go" \n"Для получения помощи введите команду /help" \n"Для того чтобы заново запустить бота введите /start"
    \n"При работе с ботом используйте клавиатуру, которая появится после отправки команды /go"
    """
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['go'])
def go_com(message):
    bot.send_message(message.chat.id, 'Поехали', reply_markup=Keybouards.keyboard_go(Keybouards))


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Приятно познакомиться,{name}.\nЧтобы начать, отправь /go'
                                      f'\nЕсли тебе нужна помощь,то отправь /help')


@bot.message_handler(content_types=['text'])
def genre_reply(message):
    if message.text == 'Жанры фильмов':
        bot.send_message(message.chat.id, 'Выберите один из жанров: ', reply_markup=Keybouards.keyboard_genre(Keybouards))
    if message.text == 'Случайный популярный сериал':
        bot.send_message(message.chat.id, populer_serials.spisok_best_serials(populer_serials))
    if message.text == 'Случайный популярный фильм':
        bot.send_message(message.chat.id, populer_films.spisok_best_films(populer_films))


@bot.callback_query_handler(func=lambda call: True)
def genre_reply_but(call):
    if call.data == 'comedy':
        bot.send_message(call.message.chat.id, 'Вы выбрали Комедии!')
    if call.data == 'mult':
        bot.send_message(call.message.chat.id, 'Вы выбрали Мультфильмы!')
    if call.data == 'fantasy':
        bot.send_message(call.message.chat.id, 'Вы выбрали Фэнтези!')
    if call.data == 'horror':
        bot.send_message(call.message.chat.id, 'Вы выбрали Ужасы!')


bot.polling()  # запускаем бота
