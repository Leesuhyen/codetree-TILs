n = input().split()

start = int(n[0])
end = int(n[1])
cnt = 0
t_cnt = 0

for i in range(start, end + 1):
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
            if cnt == 3:
                t_cnt += 1
print(t_cnt)