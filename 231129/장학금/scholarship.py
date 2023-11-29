score = input().split()
middle = int(score[0])
end = int(score[1])

if middle >= 90:
    if end >= 95:
        print(100000)
    elif end >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)