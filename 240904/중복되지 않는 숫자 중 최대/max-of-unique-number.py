n = int(input())
num = list(map(int, input().split()))

max_val = -1
 for  curr_val in num:
    if max_val < curr_val:
        cnt = 0
        for elem in num:
            if elem == curr_val:
                cnt += 1

        if cnt == 1:
            max_val = curr_val
print(max_val)