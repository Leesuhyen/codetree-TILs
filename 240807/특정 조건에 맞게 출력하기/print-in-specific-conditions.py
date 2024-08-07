num = list(map(int, input().split()))

for elem in num:
    if elem == 0:
        break
    if elem % 2 == 0:
        elem //= 2
    else:
        elem += 3
    print(elem, end=' ')