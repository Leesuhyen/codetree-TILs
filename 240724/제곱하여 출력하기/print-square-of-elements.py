n = int(input())
num = list(map(int, input().split()))

new_num = [elem * elem for elem in num]
for elem in new_num:
    print(elem, end=' ')