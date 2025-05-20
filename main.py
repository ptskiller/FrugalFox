import requests
import telebot
import json
bot = telebot.TeleBot('7519194105:AAEuScnXthxWVgO8b9TRScwyC_wVP44Ktzc')
API = 'token'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Cześć miło cie widzieć, podaj nazwę miasta')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
       data = json.loads(res.text)
       temp = data['main']['temp']
       bot.reply_to(message, f'Pogoda jest taka: {temp}')

       image = 'kartinka.1' if temp > 5.0 else 'kartinka.2'
       file = open('./' + image, 'rb')
       bot.send_photo(message.chat.id, file)
    else :
         bot.reply_to(message, f'Nazwa miasta wpisana nie prawidłowo')

    bot.polling(none_stop=True)

