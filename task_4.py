a, b, c = 3, 2, 4 # yes
#a, b, c = 3, 2, 1 # no


if c <= a * b and (c % a == 0 or c % b == 0):
    print('Yes')
else:
    print('No')