import random

print('Добро пожаловать в игру "Угадай слово"! '
      'В списке есть 5 слов, у тебя 5 есть жизней.'
      'Если буквы в слове нет у тебя сгорает 1 жизнь'
      'За 1 отгаданное слово ты восстанавливаешь 5 жизней.'
      'Победа наступает после всех отгаданных слов. Удачи!')

words = ['машина', 'питон', 'яйцо', 'корова', 'самолет']


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '*'
    return display


life = 5

guess_words = 0

user_word = ''

word1 = random.choice(words)

while life != 0:
    user = input('Введите букву: ')
    if len(user) != 1 or not user.isalpha():
        print('Пожалуйста, введите только одну букву.')
        continue

    if user in word1:
        user_word += user
        print('Буква есть: ', display_word(word1, user_word))

        if display_word(word1, user_word) == word1:
            life = 5
            guess_words += 1
            user_word = ''
            words.remove(word1)
            print('Вы угадали слово: ', word1, 'Пополнение жизней: ', life)

            if len(words):
                word1 = random.choice(words)
            else:
                print('Вы отгадали все слова!')
                break
    else:
        life -= 1
        user_word = ''
        print('Буквы нет. Осталось жизней: ', life)

if life == 0:
    print('Все жизни потеряны. Game over')
