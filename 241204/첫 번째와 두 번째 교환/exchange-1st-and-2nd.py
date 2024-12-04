n = list(input())
str1 = n[0]
str2 = n[1]
for i in range(len(n)):
    if n[i] == str1:
        n[i] = str2
    elif n[i] == str2:
        n[i] = str1
print(''.join(n))
    