num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

S_num = b if b < c else c
s_num = a if a < b else S_num



print(s_num)