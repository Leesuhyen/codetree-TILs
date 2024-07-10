num = list(map(int, input().split()))

n = len(num)
even_num = 0
odd_num = 0

for i in range(n):
    if i % 2 == 0:
        odd_num += num[i]
    else:
        even_num += num[i] 

if even_num < odd_num:
    print(odd_num - even_num)
else:
    print(even_num - odd_num)