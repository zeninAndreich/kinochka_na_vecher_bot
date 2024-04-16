from bs4 import BeautifulSoup as bs
import requests
import random

class populer_serials:
    """
    Тут все,что связано с парсингом фильмов
    """

    def spisok_best_serials(self):
        global spisok_serials
        if len(spisok_serials) == 0:
            for i in range(1, 2):
                response_get = requests.get(f'https://w140.zona.plus/tvseries?page={i}')
                soup = bs(response_get.text, features='html.parser')
                quotes_films = soup.find_all('div', class_='results-item-title')
                for film in quotes_films:
                    spisok_serials.append(film.text)
            return random.choice(spisok_serials)
        else:
            return random.choice(spisok_serials)


spisok_serials = []
