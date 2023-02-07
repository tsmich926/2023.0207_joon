T = int(input())
for tc in range(T):
    n = int(input())
    nn = n * n
    nn = str(nn)
    n = str(n)
    lst = []
    if nn[-len(n):] == n :
        print('Yes')
    else :
        print('No')
