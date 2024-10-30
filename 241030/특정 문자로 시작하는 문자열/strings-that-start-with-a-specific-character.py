n = int(input())
num = []
cnt = 0
total = 0

for q in range(n):
    num.append(input())
txt = input()

for i in range(n):
    total += len(num[i])
    if num[i][0] == txt:
        cnt += 1
qwer = round(total / n, 0)
print(f'{cnt} {qwer:.2f}')