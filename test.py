list_1 = [1, 2, 3, 4, 5]
res = []
for i in range(len(list_1)):
    res.append(sum(list_1[i-1:i+2]))
print(res)