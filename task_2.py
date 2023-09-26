n = 60

for i in range(1, n // 3):
    a = i * 2
    b = a * 2
    if b == n - a:
        print(i, b, i)
        break