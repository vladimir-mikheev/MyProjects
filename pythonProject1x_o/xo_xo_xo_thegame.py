a1 = ["-", "-", "-"] # игровое поле 3х3 из 3х списков
b2 = ["-", "-", "-"]
c3 = ["-", "-", "-"]

print(" ", "1", "2", "3")
print("1", *a1)
print("2", *b2)
print("3", *c3)
print("")


def gamer_1(): # ход первого игрока
    print("<<Игрок 1: Ваш ход>>")
    print("")
    user = input("По горизонтали:")
    user2 = input("По вертикали:")

    if user == "1" and user2 == "1" and a1[0] == "-":
        a1[0] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "1" and user2 == "2" and a1[1] == "-":
        a1[1] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "1" and user2 == "3" and a1[2] == "-":
        a1[2] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "2" and user2 == "1" and b2[0] == "-":
        b2[0] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "2" and user2 == "2" and b2[1] == "-":
        b2[1] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "2" and user2 == "3" and b2[2] == "-":
        b2[2] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "3" and user2 == "1" and c3[0] == "-":
        c3[0] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "3" and user2 == "2" and c3[1] == "-":
        c3[1] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif user == "3" and user2 == "3" and c3[2] == "-":
        c3[2] = "o"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    else:
        print("")
        print("<<Ячейка уже занята!>>")
        print("<<Попробуйте еще раз>>")
        print("")
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)
        gamer_1() # вызывается для повторной попытки хода, в случае если первый игрок выберет занятую ячейку на игровом поле

    if a1.count("o") == 3 or b2.count("o") == 3 or c3.count("o") == 3: # проверка комбинаций выигрыша после хода первого игрока
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1.count("x") == 3 or b2.count("x") == 3 or c3.count("x") == 3:
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "x" and b2[0] == "x" and c3[0] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[1] == "x" and b2[1] == "x" and c3[1] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "x" and b2[2] == "x" and c3[2] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "x" and b2[1] == "x" and c3[2] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "x" and b2[1] == "x" and c3[0] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "o" and b2[0] == "o" and c3[0] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[1] == "o" and b2[1] == "o" and c3[1] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "o" and b2[2] == "o" and c3[2] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "o" and b2[1] == "o" and c3[2] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "o" and b2[1] == "o" and c3[0] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    else:
        gamer_2() # сразу после хода первого игрока, вызывается функция хода3 второго игрока


def gamer_2(): # ход второго игрока
    print("")
    print("<<Игрок 2: Ваш ход>>")
    print("")
    player1 = input("По горизонтали:")
    player2 = input("По вертикали:")

    if player1 == "1" and player2 == "1" and a1[0] == "-":
        a1[0] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "1" and player2 == "2" and a1[1] == "-":
        a1[1] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "1" and player2 == "3" and a1[2] == "-":
        a1[2] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "2" and player2 == "1" and b2[0] == "-":
        b2[0] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "2" and player2 == "2" and b2[1] == "-":
        b2[1] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "2" and player2 == "3" and b2[2] == "-":
        b2[2] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "3" and player2 == "1" and c3[0] == "-":
        c3[0] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "3" and player2 == "2" and c3[1] == "-":
        c3[1] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)

    elif player1 == "3" and player2 == "3" and c3[2] == "-":
        c3[2] = "x"
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)
    else:
        print("")
        print("<<Ячейка уже занята!>>")
        print("<<Попробуйте еще раз>>")
        print("")
        print(" ", "1", "2", "3")
        print("1", *a1)
        print("2", *b2)
        print("3", *c3)
        gamer_2() # вызывается для повторной попытки хода, в случае если второй игрок выберет занятую ячейку на игровом поле

    if a1.count("o") == 3 or b2.count("o") == 3 or c3.count("o") == 3: # проверка комбинаций выигрыша после хода второго игрока
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1.count("x") == 3 or b2.count("x") == 3 or c3.count("x") == 3:
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "x" and b2[0] == "x" and c3[0] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[1] == "x" and b2[1] == "x" and c3[1] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "x" and b2[2] == "x" and c3[2] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "x" and b2[1] == "x" and c3[2] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "x" and b2[1] == "x" and c3[0] == "x":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 2")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "o" and b2[0] == "o" and c3[0] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[1] == "o" and b2[1] == "o" and c3[1] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "o" and b2[2] == "o" and c3[2] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[0] == "o" and b2[1] == "o" and c3[2] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    elif a1[2] == "o" and b2[1] == "o" and c3[0] == "o":
        print("ИГРА ОКОНЧЕНА. ПОБЕДИЛ ИГРОК 1")
        input("Нажимите Enter, чтобы закрыть")
    else:
        gamer_1() # сразу после хода первого игрока, вызывается функция хода второго игрока




gamer_1()