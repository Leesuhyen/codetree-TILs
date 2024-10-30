num = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
cnt =0
for i in range(5):
    for j in range(2, 4):
        if num[i][j] == n:
            cnt += 1
            print(num[i])
print(cnt)