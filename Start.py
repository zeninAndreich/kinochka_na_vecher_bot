import random

import telebot
from config import token
from bs4 import BeautifulSoup as bs
import requests
from keybouards import Keybouards


bot = telebot.TeleBot(token)
name = ''

spisok_films = []


def spisok_best_films():
    global spisok_films
    if len(spisok_films) == 0:
        for i in range(1, 2):
            response_get = requests.get(f'https://w140.zona.plus/movies?page={i}')
            soup = bs(response_get.text, features='html.parser')
            quotes_films = soup.find_all('div', class_='results-item-title')
            for film in quotes_films:
                spisok_films.append(film.text)
        return random.choice(spisok_films)
    else:
        return random.choice(spisok_films)


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
        pass
    if message.text == 'Случайный популярный фильм':
        bot.send_message(message.chat.id, spisok_best_films())


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


bot.polling()  # запускаем бота 1
