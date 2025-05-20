import telebot
import requests
bot = telebot.TeleBot(config.token)
API = 'token'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Cześć miło cie widzieć, podaj nazwę miasta')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    requests.get('ссылка на сайт')

bot.polling(none_stop=True)

