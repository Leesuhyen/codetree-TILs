s_score = list(map(float, input().split()))
sum_val = 0
avg = 0
for elem in s_score:
    sum_val += elem
avg = sum_val / len(s_score)
print(f"{avg:.1f}")