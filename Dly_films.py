from bs4 import BeautifulSoup as bs
import requests
import random


class populer_films:
    """
    Тут все,что связано с парсингом фильмов
    """

    def spisok_best_films(self):
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


spisok_films = []
