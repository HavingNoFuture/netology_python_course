import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def read_files(path_source):
    list_for_translate = []
    files = os.listdir(path_source)
    for file in files:
        if ".txt" in file:
            with open(os.path.join(path_source, file), 'r') as f:
                text = f.read()
                list_for_translate.append(text)
    return list_for_translate


def write_file(translate):
    with open(os.path.join(path_source,"translate.txt"), "a") as f:
        f.write(translate)

def translate_it(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params_key = {
        'key': API_KEY,
        'text': text,
        'hint': ['fr', 'de', 'es']
    }

    lang = requests.get(URL, params=params_key)

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    return ''.join(json_['text'])


path_source = r"E:\python_projects\netology_3.2"
list_for_translate = read_files(path_source)


for i in list_for_translate:
    write_file(translate_it(i))
    print(translate_it(i))
