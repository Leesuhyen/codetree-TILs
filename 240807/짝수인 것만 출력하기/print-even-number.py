n = int(input())
num = list(map(int, input().split()))

new_num = []
for elem in num:
    if elem % 2 == 0:
        new_num.append(elem)
for elem in new_num:
    print(elem, end=' ')