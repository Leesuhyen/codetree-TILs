n = list(input())
b = input()
cnt = 0
for i in range(len(n)):
    if b == n[i]:
        cnt += 1
print(cnt)