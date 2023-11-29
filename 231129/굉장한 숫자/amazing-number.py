n = int(input())

'''
if n % 3 == 0 and n // 2 != 0:
    print("true")
elif n % 5 == 0 and n // 2 != 0:
    print("true")
else:
    print("false")
'''
if n % 2 != 0 and n % 3 == 0 or n % 2 == 0 and n % 5 == 0:
    print("true")
else:
    print("false")