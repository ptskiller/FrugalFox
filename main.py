import requests
import telebot
import json

bot = telebot.TeleBot('7519194105:AAEuScnXthxWVgO8b9TRScwyC_wVP44Ktzc')
API = '9c943d9e2da1bd731fec4834691cae2e'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Cześć! Podaj nazwę miasta, a pokażę ci pogodę 🌦️')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    if res.status_code == 200:
        data = res.json()

        temp = data['main']['temp']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        weather_main = data['weather'][0]['main']

        # Эмодзи по погоде
        weather_icons = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Drizzle': '🌦️',
            'Thunderstorm': '⛈️',
            'Snow': '❄️',
            'Mist': '🌫️',
            'Fog': '🌫️'
        }

        weather_icon = weather_icons.get(weather_main, '🌈')

        # Определяем картинку по погоде
        image_files = {
            'Clear': 'clear.png',
            'Clouds': 'clouds.png',
            'Rain': 'rain.png',
            'Drizzle': 'rain.png',
            'Thunderstorm': 'storm.png',
            'Snow': 'snow.png',
            'Mist': 'fog.png',
            'Fog': 'fog.png'
        }

        image_name = image_files.get(weather_main, 'default.png')

        lat = data['coord']['lat']
        lon = data['coord']['lon']

        # Получаем UV индекс
        one_call_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API}&units=metric'
        one_call_res = requests.get(one_call_url)
        if one_call_res.status_code == 200:
            one_data = one_call_res.json()
            uvi = one_data['current']['uvi']
        else:
            uvi = 'n/a'

        msg = (
            f"{weather_icon} Pogoda w {city.title()}:\n"
            f"🌡️ Temperatura: {temp}°C\n"
            f"🌬️ Wiatr: {wind_speed} m/s\n"
            f"🧭 Ciśnienie: {pressure} hPa\n"
            f"🔆 UV Index: {uvi}"
        )

        bot.reply_to(message, msg)

        try:
            with open('./' + image_name, 'rb') as file:
                bot.send_photo(message.chat.id, file)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "⚠️ Brakuje obrazka pogodowego.")

    else:
        bot.reply_to(message, '❗ Błąd: nieprawidłowa nazwa miasta.')

bot.polling(none_stop=True)
