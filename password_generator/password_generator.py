import random

# Задаем наборы символов для разных категорий
numbers = '1234567890'                    # Цифры
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'   # Заглавные буквы
lower_case = 'qwertyuiopasdfghjklzxcvbnm'  # Строчные буквы
special_characters = '!@#$%^&*()?'         # Специальные символы

def generate_password(length):
    characters = numbers + uppercase + lower_case + special_characters  # Общий набор символов
    if length >= 4:  # Минимальная длина пароля (1 символ из каждой категории и еще хотя бы один)
        password = (
            random.choice(numbers) +
            random.choice(uppercase) +
            random.choice(lower_case) +
            random.choice(special_characters)  # Выбираем по одному символу из каждой категории
        )
        for _ in range(length - 4):
            password += random.choice(characters)  # Добавляем остальные символы, чтобы достичь заданной длины
        password_list = list(password)
        random.shuffle(password_list)  # Перемешиваем символы пароля
        return ''.join(password_list)  # Преобразуем список символов обратно в строку
    else:
        return "Длина пароля должна быть больше или равна 4."

desired_length = int(input("Введите желаемую длину пароля: "))
password = generate_password(desired_length)
print("Сгенерированный пароль:", password)

