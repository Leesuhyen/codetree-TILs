num = int(input())

n = []
cnt = 0
for i in range(12):
    n.append(num * (1 + i))
    if n[i] % 5 == 0:
        cnt += 1
    print(n[i], end=' ')        
    if cnt == 2:
        break