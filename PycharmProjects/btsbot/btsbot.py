import telebot
import random

bot = telebot.TeleBot('5742569815:AAHVt2YEr_PvnObPM68mSv8DV2N0Ko8VF_A')

pose = ["тебе отлижет", "тебе сделает петтинг", "тебе подрочит", "тебя выебет в рот", "на тебе попрыгает", "тебя поцелует в щёчку", "тебя выебет раком", "тебя трахнет в попку", "тебе кончит на грудь", "тебе отсосет", "тебя заберет в Корею", "ты будешь секс-рабом"]
bts = ["Джонгук", "Чимин", "Шуга", "Тхэхён", "Джин", "Намджун", "Хосок", "Хёндэ Солярис", "Киа Рио", "Рамён", "Доши Рак", "Кич Чин Ын", "Сон Хын Мин", "Парк Джи Сун", "Ядерная боеголовка Ким Чин Ына", "рандомный модный кореец"]
text = ["в восточной лавке", "на заднем сиденье Хёндэ Солярис", "у себя дома", "в ванной полной рамёна", "на премьере фильма о Ким Чин Ыне", "на свадьбе Чимина и Бекхэма", "на лысине Джейсона Стэтхэма", "в коробке из под Самнсунг Гэлэкси Зэт Фолд", "на яхте от Сяоми", "на вечернке по случаю его камин-аута"]
sex = lambda: random.choice(pose)
name = lambda: random.choice(bts)
txt = lambda: random.choice(text)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, f"{name()} {sex()} {txt()}")
    else:
        bot.send_message(message.chat.id, "Напиши: /start")

bot.polling(non_stop=True)