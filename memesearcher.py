import os
import shutil
import requests
import random


def search_meme(folder, meme_name):
    url = f"https://knowyourmeme.com/search?context=images&sort=relevance&q={folder.replace(' ', '+')}"
    print(url)
    data = get_data_from_url(url)
    save_image(folder, meme_name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    data = response.raw

    return data


def save_image(folder, meme_name, data):
    file_name = os.path.join(folder, meme_name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
