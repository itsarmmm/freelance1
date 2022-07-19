import json
import requests

#Сюда API токен с сайта
API_KEY = '5d58af2dd39fa143003a80100cac8e23a641b642'
#базовый URL для запросов
BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/'


def find_INN(resource, query):
    url = BASE_URL + resource
    headers = {
        'Authorization': 'Token ' + API_KEY,
        'Content-Type': 'application/json',
        'Accept':'application/json'
    }
    data = {
        'query': query
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()



# получаем данные юр.лица по ИНН

# название компании
# print('Название: ' + data['suggestions'][0]['value'])