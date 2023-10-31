import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        'Clear': 'Ясно ☀',
        'Clouds': 'Облачно ☁',
        'Rain': 'Дождь ☔',
        'Drizzle': 'Дождь ☔',
        'Thunderstorm': 'Гроза ⚡',
        'Snow': 'Снег ❄',
        'Mist': 'Туман 🌫'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        pprint(data)

        city = data['name']

        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно!\nНе пойму, что там происходит."

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        sunrise_times = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        hour_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        print(f'========\n'
              f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}\n'
              f'{datetime.datetime.now().strftime("%A")}\n'
              f'========\n'
              f'Погода в городе: {city}\n'
              f'Температура: {cur_weather}°C {wd}\n'
              f'Влажность: {humidity}%\n'
              f'Ветер: {wind} м/с\n'
              f'Продолжительность дня: {hour_day}\n'
              f'Восход солнца: {sunrise_timestamp}\n'
              f'Заход солнца: {sunrise_times}\n'
              f'========\n'
              f'Удачного дня тебе =)'
              )

    except Exception as ex:
        print(ex)
        print('Проверте название города')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
