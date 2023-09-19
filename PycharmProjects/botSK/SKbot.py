import telebot

TOKEN = '5980205780:AAG6JHYIRRHzYBTvHZtH2fyOVqyX2R4Z2WI'

bot = telebot.TeleBot(TOKEN)

#команды
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f"ку, {message.chat.username}. я самый душный бот. создан по образу и подобию лучшего друга разаботчика который меня создал. вы можете написать мне, отправить мем чтобы я его заценил, голосовуху, музыку и все чо ток можете. только мне ничего не понравится, я очень душный")

# Обрабатывается все фотки
@bot.message_handler(content_types=['photo'])
def handle_picture(message: telebot.types.Message):
    bot.reply_to(message, "баян")

@bot.message_handler(content_types=['voice'])
def handle_voice(message: telebot.types.Message):
    bot.reply_to(message, "норм")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'привет' or message.text == 'ку' or message.text == 'здарова' or message.text == 'здорова'  or message.text == 'здаров' or message.text == 'здоров':
        bot.send_message(message.chat.id, 'ку')
    else:
        bot.reply_to(message, 'понятно, а я заебался')

@bot.message_handler(message=['привет', 'ку', 'здарова', 'здорова', 'здаров', 'здоров'])
def handle_message(message: telebot.types.Message):
    bot.reply_to(message, 'ку')

bot.polling(none_stop=True)