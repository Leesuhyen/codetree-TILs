num = list(map(int, input().split()))

cnt = 0
for elem in num:
    if elem % 3 == 0:

        break
    cnt += 1        
print(num[cnt - 1])