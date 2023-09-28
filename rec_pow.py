def rec_pow(x, y):
    if y <= 0:
        return 1
    return x * rec_pow(x, y - 1)


#a = 3; b = 5
a = 2; b = 3

print(rec_pow(a, b))
