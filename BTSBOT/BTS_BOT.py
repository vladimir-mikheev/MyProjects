import random
import telebot


bot = telebot.TeleBot('5742569815:AAHVt2YEr_PvnObPM68mSv8DV2N0Ko8VF_A')

sexx = ["отлижет тебе", "сделает тебе петтинг", "подрочит тебе", "выебет тебя в рот", "попрыгает на тебе", "поцелует тебя в щёчку", "выебет тебя раком", "трахнет тебя в попку", "кончит тебе на грудь", "отсосет тебе", "сделает тебя секс-рабом"]
btss = ["Чёнгук", "Чимин", "Шуга", "Тэхён", "Джин", "Намджун", "Хосок", "Хёндэ Солярис", "Киа Рио", "Рамён", "Доши Рак", "Ким Чин Ын", "Сон Хын Мин", "Парк Джи Сун", "рандомный модный кореец"]
phrases = ["в восточной лавке", "на заднем сиденье Хёндэ Солярис", "в своем корейском пентхаусе из палочек для еды", "в ванной полной рамёна", "на премьере фильма о Ким Чин Ыне", "на свадьбе Чимина и Бекхэма", "на лысине Джейсона Стэтхэма", "в коробке из под Самнсунг Гэлэкси Зэт Фолд", "на яхте от Сяоми", "на вечернке по случаю его камин-аута"]
sex = lambda: random.choice(sexx)
bts = lambda: random.choice(btss)
phrase = lambda: random.choice(phrases)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, f"{bts()} {sex()} {phrase()}")
    else:
        bot.send_message(message.chat.id, "Напиши: /start")

bot.polling(non_stop=True)