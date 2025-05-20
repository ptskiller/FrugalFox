import telebot

bot = telebot.TeleBot(7519194105:AAEuScnXthxWVgO8b9TRScwyC_wVP44Ktzc)
API = 'token'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Cześć miło cie widzieć, podaj nazwę miasta')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()

bot.polling(none_stop=True)

