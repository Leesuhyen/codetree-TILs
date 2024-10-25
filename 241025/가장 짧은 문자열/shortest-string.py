n = input()
b = input()
c = input()

for i in range(1):
    if len(n) > len(b) and len(n) > len(c):
        if len(b) > len(c):
            print(len(n) - len(c))
        else:
            print(len(n) - len(b))       
    if len(b) > len(n) and len(b) > len(c):
        if len(n) > len(c):
            print(len(b) - len(c))
        else:
            print(len(b) - len(n))  
    if len(c) > len(n) and len(c) > len(b):
        if len(n) > len(b):
            print(len(c) - len(b))
        else:
            print(len(c) - len(n))