n = input().split()
s = n[0]
q = int(n[1])


for i in range(q):
    quest = input().split()
    if quest[0] == '1':
        #첫번째와 두번째를 서로 바꿈
        #s[int(quest[1]-1)]
    elif quest[0] == '2':
        #퀘스트 1번의 문자를 2번의 문자로 모두 변경
    print(quest)
