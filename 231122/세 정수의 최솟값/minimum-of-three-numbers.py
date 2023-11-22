num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

S_num = b if b < c else c
S_num = a if a < S_num else S_num



print(S_num)