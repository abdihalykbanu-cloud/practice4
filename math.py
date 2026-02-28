import math

# 1. Градусы в радианы
degree = 15
radian = math.radians(degree)

# 2. Площадь трапеции
def area_trapezoid(h, a, b):
    return 0.5 * (a + b) * h

# 3. Площадь правильного многоугольника
def area_polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

# 4. Площадь параллелограмма
def area_parallelogram(base, height):
    return float(base * height)

# 5. Факториал числа
fact = math.factorial(5) # 120
