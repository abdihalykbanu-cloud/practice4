# 1. Квадраты чисел до N
def squares(n):
    for i in range(n):
        yield i**2

# 2. Четные числа до N
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# 3. Числа, делящиеся на 3 и 4
def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 4. Квадраты от a до b
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i**2

# 5. Обратный отсчет от N до 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
