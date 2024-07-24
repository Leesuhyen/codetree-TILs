num = list(map(int, input().split()))

new_num = []
new_num.append(num[0])
new_num.append(num[1])

for i in range(2, 10):
    new_num.append((new_num[i - 1] + new_num[i- 2]) % 10) 
for elem in new_num:
    print(elem, end=' ')