n = int(input())

for i in range(n):
    p = 1    
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    for j in range(a, b + 1):
        p *= j
    print(p)

print()