n = input()
m = input()
idx = 0
if n.find(m) == -1:
    print(n.find(m))
elif m in n:
    for i in range(len(n)):
        if n[i:i+2] == m:
            idx = i
print(idx)