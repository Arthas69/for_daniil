from math import sqrt
from random import randint

a = randint(1, 1000)
b = randint(1, 1000)

s = a + b
p = a * b


# Система уравнений

# 1) выделяем a -> a = s - b
# 2) подставляем a во второе уравнение и открываем скобки

# p = (s - b) * b = sb - b^2 

# 3) Переносим p и получаем квадратное уравнение
# -b^2 + sb - p = 0

def calculate(x, y):
    D = x * x + 4 * y  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = sqrt(D) // 2
        p = x // 2
        root1 = p - sq
        root2 = p + sq
        return [root1, root2]

x, y = calculate(s, -p)
print(x, y)