input_str = input()
target_str = input()
cnt = 0
n, m = len(input_str), len(target_str)
for i in range(n):
    if i + m - 1 >= n:
        continue
    
    is_matched = True
    for j in range(m):
        if input_str[i + j] != target_str[j]:
            is_matched = False
            
    if is_matched:
        cnt += 1          


print(cnt)