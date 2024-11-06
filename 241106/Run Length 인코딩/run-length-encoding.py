n = input()
txt = '0'
cnt = 0
num =[]
for i in range(len(n)):
    if txt =='0':
        txt = n[i]
        cnt += 1
        num.append(txt)
    elif txt ==n[i]:
        cnt += 1
    else:
        num.append(cnt)
        cnt = 1
        txt = n[i]
        num.append(txt)
num.append(cnt)
print(len(num))
for elem in num:
    print(str(elem), end='')