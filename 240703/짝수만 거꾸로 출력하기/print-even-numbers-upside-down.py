n = int(input())
n_num = []
even_num = []
for i in range(n):
    n_num.append(int(input()))
    if n_num[i] % 2 == 0:
        even_num.append(n_num[i])
    for elem in even_num[::-1]:
        print(elem)