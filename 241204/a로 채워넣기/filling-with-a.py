n = list(input())
n[1] = 'a'
n[len(n)-2] = 'a'
for elem in n:
    print(elem, end='')