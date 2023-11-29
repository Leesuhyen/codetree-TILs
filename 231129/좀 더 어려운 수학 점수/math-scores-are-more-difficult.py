score_a = input().split()
m_a = int(score_a[0])
e_a = int(score_a[1])
score_b = input().split()
m_b = int(score_b[0])
e_b = int(score_b[1])

if m_a < m_b:
    print("B")
elif m_a == m_b:
    if e_a < e_b:
        print("B")
    else:
        print("A")
else:
    print("A")