from random import randint

N = int(input('Number of bushes: '))

bushes, berries_gathered = [], []

for _ in range(N):
    bushes.append(randint(100, 500))

print(bushes)

# Solution 1
bushes.insert(0, bushes[-1])
bushes.append(bushes[1])

# print(bushes)

for i in range(1, N + 1):
    berries_gathered.append(sum(bushes[i-1:i+2]))

# Solution 2

# for i in range(N-1):
#     berries_gathered.append(bushes[i-1] + bushes[i] + bushes[i+1])
# else:
#     berries_gathered.append(bushes[i] + bushes[i + 1] + bushes[0])


print(berries_gathered)
print(max(berries_gathered))