one = input().split()
two = input().split()
third = input().split()

a_one = one[0]
b_one = int(one[1])

a_two = two[0]
b_two = int(two[1])

a_third = third[0]
b_third = int(third[1])

if a_one == 'Y' and b_one >= 37:
    if a_two == 'Y' and b_two >= 37:
        if a_third == 'Y' and b_third >= 37:
            print('E')
        else:
            print("E")
    else:
        if a_third == 'Y' and b_third >= 37:
            print('E')
        else:
            print('N')
else:
    if a_two == 'Y' and b_two >= 37:
        if a_third == 'Y' and b_third >= 37:
            print('E')
        else:
            print('N')
    else:
        print('N')