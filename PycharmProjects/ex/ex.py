# Функция для нахождения корня элемента в множестве
def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])  # Оптимизация: сжатие пути
    return parents[x]

# Функция для объединения двух множеств
def union(parents, sizes, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    if root_x != root_y:
        if sizes[root_x] < sizes[root_y]:
            root_x, root_y = root_y, root_x
        parents[root_y] = root_x
        sizes[root_x] += sizes[root_y]

# Считываем количество духов и вопросов
n, m = map(int, input().split())

parents = list(range(n))  # Изначально каждый дух в своей банде
sizes = [1] * n  # Размеры банд

answers = []

# Обрабатываем каждый вопрос
for _ in range(m):
    query = input().split()
    if query[0] == '1':
        x, y = map(int, query[1:])
        union(parents, sizes, x - 1, y - 1)
    elif query[0] == '2':
        x, y = map(int, query[1:])
        if find(parents, x - 1) == find(parents, y - 1):
            answers.append("YES")
        else:
            answers.append("NO")
    elif query[0] == '3':
        x = int(query[1])
        root_x = find(parents, x - 1)
        answers.append(str(sizes[root_x]))

# Выводим ответы
for ans in answers:
    print(ans)
