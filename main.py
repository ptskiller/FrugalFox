import telebot
<<<<<<< HEAD

bot = telebot.TeleBot(7519194105:AAEuScnXthxWVgO8b9TRScwyC_wVP44Ktzc)
=======
import requests
bot = telebot.TeleBot(config.token)
>>>>>>> 8f1c93a8b9a8a0f33a6af224595908983a387a54
API = 'token'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Cześć miło cie widzieć, podaj nazwę miasta')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    requests.get('ссылка на сайт')

bot.polling(none_stop=True)

