s_num = int(input())
cnt = 0
for i in range(s_num):
    total = 0
    avg = 0

    score = list(map(int, input().split()))
    for elem in score:
        total += elem
    avg =  total / len(score)
    if avg >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(cnt)