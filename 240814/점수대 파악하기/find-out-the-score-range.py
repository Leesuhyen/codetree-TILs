num = list(map(int, input().split()))
score = [0] * 11
for elem in num:
    if elem == 0:
        break
    sc = 0
    sc = elem // 10
    score[sc] += 1
for i in range(10, 0, -1):
    print(f"{i}0 - {score[i]}")