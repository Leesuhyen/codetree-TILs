p_a = input().split()
a_a = int(p_a[0])
s_a = p_a[1]
p_b = input().split()
a_b = int(p_b[0])
s_b = p_b[1]

if a_a >= 19 and s_a == 'M' or a_b >= 19 and s_b =='M':
    print(1)
else:
    print(0)