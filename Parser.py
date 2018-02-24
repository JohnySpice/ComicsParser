import os
import requests
from bs4 import BeautifulSoup

url = 'http://unicomics.ru/comics/online/amazing-spider-man-653'
#url = 'http://unicomics.ru/comics/online/deadpool-vs-thanos-1'


def get_urlNext(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    a = soup.find('a', string="Вперед")
    return a.get('href')


def get_urlPage(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    img = soup.find('img', class_="img_tmhover image_online")
    return img.get('src')


def parse(urlSite):
    for i in range(1, 26):
        urlPage = get_urlPage(urlSite)
        r = requests.get(urlPage)
        name = str(i)
        foldername = url[34::]
        create_folder(foldername)
        with open(foldername+"/" + name + '.jpg', 'bw') as f:
            f.write(r.content)
        urlSite = 'http://unicomics.ru' + get_urlNext(urlSite)


def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)


parse(url)

