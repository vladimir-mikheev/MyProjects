import telebot
from config import keys, TOKEN
from Exception import APIException, CurrencyConvertor


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты>\
<в какую валюту перевести>\
<кол-во переводимой валюты>\
\nНапример: доллар рубль 100\
\nУвидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():\
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException("Неверное количество параметров")
        quote, base, amount = message.text.split(' ')
        total_base = CurrencyConvertor.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)





bot.polling(none_stop=True)