num = input().split()

arr = []
arr.append(int(num[0]))
arr.append(int(num[1]))

for i in range(2, 10):
    arr.append(2 * arr[(i - 2)] + arr[i - 1])

for elem in arr:
    print(elem, end=' ')