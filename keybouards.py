import telebot


class Keybouards:
    """
    Тут содержатся клавиатуры бота
    """

    def keyboard_go(self):
        keyb_markup = telebot.types.ReplyKeyboardMarkup()
        button_genre = telebot.types.KeyboardButton('Жанры фильмов')
        button_random_populer_serial = telebot.types.KeyboardButton('Случайный популярный сериал')
        button_random_populer_films = telebot.types.KeyboardButton('Случайный популярный фильм')
        keyb_markup.row(button_genre)
        keyb_markup.row(button_random_populer_serial)
        keyb_markup.row(button_random_populer_films)
        return keyb_markup

    def keyboard_genre(self):
        keyb_gener_reply = telebot.types.InlineKeyboardMarkup()
        key_comedy = telebot.types.InlineKeyboardButton(text='Комедии', callback_data='comedy')
        key_mult = telebot.types.InlineKeyboardButton(text='Мультфильмы', callback_data='mult')
        key_fantasy = telebot.types.InlineKeyboardButton(text='Фентази', callback_data='fantasy')
        key_horror = telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='horror')
        keyb_gener_reply.add(key_comedy, key_mult, key_fantasy, key_horror)
        return keyb_gener_reply
