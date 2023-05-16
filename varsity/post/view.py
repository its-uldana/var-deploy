from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def show_internships(request):
    url = 'https://ru.studyqa.com/internships'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        internships = soup.find_all('div', class_="cards__item-block")
        internship_titles = [internship.text.strip() for internship in internships]

        # links = soup.find_all('a', class_='cards__item-title')
        # internship_titles = [links.text.strip() for link in links]
        context = {'internships': internship_titles}
        return render(request, 'post/internships.html', context)
    else:
        error_message = 'Ошибка при получении страницы: {}'.format(response.status_code)
        context = {'error': error_message}
        return render(request, 'error.html', context)
