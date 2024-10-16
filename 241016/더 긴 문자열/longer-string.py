n = input().split()
txt1 = n[0]
txt2 = n[1]
if len(txt1) < len(txt2):
    print(txt2, len(txt2))
elif len(txt1) == len(txt2):
    print(same)
else:
    print(txt1, len(txt1))