a = input()
b = input()
c = input()
d = input()

num = list([a, b, c, d])

for elem in num[-1: -5: -1]:
    print(elem)