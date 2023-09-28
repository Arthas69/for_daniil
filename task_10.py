from random import randint

coins = {0: 0, 1: 0}

n = int(input('Number of coins: '))

for i in range(n):
    coins[randint(0, 1)] += 1

print(f'Need to swap {min(coins.values())} coins')
