list_1 = [1, 2, 3, 4, 5]
k = 3

diff = float('inf')
result = None

for i in list_1:
    if temp := abs(k - i) < diff:
        result = i
        diff = temp

print(result)