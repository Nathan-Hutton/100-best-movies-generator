import requests
from bs4 import BeautifulSoup

html_file = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(html_file, 'html.parser')
h3_list = soup.find_all(name='h3', class_='title')
title_list = [title.text for title in h3_list]

with open('movies.txt', 'a', encoding='utf-8') as file:
    file.truncate(0)
    for title in reversed(title_list):
        file.write(title + "\n")


