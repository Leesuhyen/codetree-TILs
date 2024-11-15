n = input()
m = input()
cnt = 0
if n.find(m) == -1:
    print(n.find(m))


for i in range(len(n)):
    if n[i:i+2] == m:
        cnt += 1
print(cnt)