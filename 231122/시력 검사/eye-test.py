l_y = float(input())
r_y = float(input())

if l_y >= 1.0 and r_y >= 1.0:
    print("High")
elif l_y >= 0.5 and r_y >= 0.5:
    print("Middle")
else:
    print("Low")