#coding=utf-8
def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+ \
    qsort([ge for ge in L[1:] if ge >= L[0]])

def formula(a):
    a=qsort(a)
    n=0
    #print(a)
    for i in range(len(a)-2):
        if a[i]+a[i+1]>a[i+2]:
            n =1
            #return n
    return n


if __name__=='__main__':
    n=int(input())
    long = list(map(int, input().split()))
    q=[]
    m=int(input())
    for i in range(m):
       q.append(list(map(int, input().split())))

    ssum=0
    for i in range(len(q)):
        a=q[i][0]
        b=q[i][1]
        num=0
        num=formula(long[a-1:b])
        ssum += num
    print(ssum)
