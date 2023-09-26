n = 385916

first, last = n // 1000, n % 1000

sum_1 = sum_2 = 0

while first:
    x, first = first % 10, first // 10
    sum_1 += x

while last:
    x, last = last % 10, last // 10
    sum_2 += x


if sum_1 == sum_2:
    print('Yes')
else:
    print('No')